from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import Suggestion
from app.schemas import SuggestionCreate, SuggestionOut
from app.api.users import get_current_user
from datetime import datetime

router = APIRouter()

@router.get('/', response_model=list[SuggestionOut])
def list_suggestions(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Suggestion).filter(Suggestion.user_id == user.id).all()

@router.post('/', response_model=SuggestionOut)
def create_suggestion(suggestion: SuggestionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    # Placeholder for AI integration
    db_suggestion = Suggestion(user_id=user.id, text=suggestion.text, created_at=datetime.utcnow())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

@router.patch('/{suggestion_id}', response_model=SuggestionOut)
def update_suggestion(suggestion_id: int, suggestion: SuggestionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_suggestion = db.query(Suggestion).filter(Suggestion.id == suggestion_id, Suggestion.user_id == user.id).first()
    if not db_suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    db_suggestion.text = suggestion.text
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

@router.delete('/{suggestion_id}')
def delete_suggestion(suggestion_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    suggestion = db.query(Suggestion).filter(Suggestion.id == suggestion_id, Suggestion.user_id == user.id).first()
    if not suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    db.delete(suggestion)
    db.commit()
    return {"ok": True}
