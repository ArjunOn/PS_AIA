from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import Meeting
from app.schemas import MeetingCreate, MeetingOut
from app.api.users import get_current_user

router = APIRouter()

@router.get('/', response_model=list[MeetingOut])
def list_meetings(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Meeting).filter(Meeting.user_id == user.id).all()

@router.post('/', response_model=MeetingOut)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_meeting = Meeting(user_id=user.id, title=meeting.title, datetime=meeting.datetime, location=meeting.location, description=meeting.description)
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

@router.delete('/{meeting_id}')
def delete_meeting(meeting_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id, Meeting.user_id == user.id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    db.delete(meeting)
    db.commit()
    return {"ok": True}
