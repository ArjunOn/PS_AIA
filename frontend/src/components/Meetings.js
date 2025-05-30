import React, { useEffect, useState } from "react";
import { Typography, Box, TextField, Button, List, ListItem, IconButton } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import api from "../api/axios";

function Meetings() {
  const [meetings, setMeetings] = useState([]);
  const [title, setTitle] = useState("");
  const [datetime, setDatetime] = useState("");
  const [location, setLocation] = useState("");
  const [description, setDescription] = useState("");
  const token = localStorage.getItem("token");

  const fetchMeetings = async () => {
    const res = await api.get("/meetings/", { headers: { Authorization: `Bearer ${token}` } });
    setMeetings(res.data);
  };

  useEffect(() => { fetchMeetings(); }, []);

  const addMeeting = async (e) => {
    e.preventDefault();
    await api.post("/meetings/", { title, datetime, location, description }, { headers: { Authorization: `Bearer ${token}` } });
    setTitle(""); setDatetime(""); setLocation(""); setDescription("");
    fetchMeetings();
  };

  const deleteMeeting = async (id) => {
    await api.delete(`/meetings/${id}`, { headers: { Authorization: `Bearer ${token}` } });
    fetchMeetings();
  };

  return (
    <Box>
      <Typography variant="h6">Add Meeting</Typography>
      <form onSubmit={addMeeting} style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginBottom: 16 }}>
        <TextField label="Title" value={title} onChange={e => setTitle(e.target.value)} size="small" required />
        <TextField type="datetime-local" value={datetime} onChange={e => setDatetime(e.target.value)} size="small" required InputLabelProps={{ shrink: true }} />
        <TextField label="Location" value={location} onChange={e => setLocation(e.target.value)} size="small" />
        <TextField label="Description" value={description} onChange={e => setDescription(e.target.value)} size="small" />
        <Button type="submit" variant="contained">Add</Button>
      </form>
      <Typography variant="h6">Your Meetings</Typography>
      <List>
        {meetings.map(m => (
          <ListItem key={m.id} secondaryAction={
            <IconButton edge="end" aria-label="delete" onClick={() => deleteMeeting(m.id)}>
              <DeleteIcon />
            </IconButton>
          }>
            {m.title} — {new Date(m.datetime).toLocaleString()} ({m.location})
          </ListItem>
        ))}
      </List>
    </Box>
  );
}
export default Meetings;
