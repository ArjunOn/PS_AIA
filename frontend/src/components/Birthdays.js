import React, { useEffect, useState } from "react";
import { Typography, Box, TextField, Button, List, ListItem, IconButton } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import api from "../api/axios";

function Birthdays() {
  const [birthdays, setBirthdays] = useState([]);
  const [name, setName] = useState("");
  const [date, setDate] = useState("");
  const token = localStorage.getItem("token");

  const fetchBirthdays = async () => {
    const res = await api.get("/birthdays/", { headers: { Authorization: `Bearer ${token}` } });
    setBirthdays(res.data);
  };

  useEffect(() => { fetchBirthdays(); }, []);

  const addBirthday = async (e) => {
    e.preventDefault();
    await api.post("/birthdays/", { name, date }, { headers: { Authorization: `Bearer ${token}` } });
    setName(""); setDate("");
    fetchBirthdays();
  };

  const deleteBirthday = async (id) => {
    await api.delete(`/birthdays/${id}`, { headers: { Authorization: `Bearer ${token}` } });
    fetchBirthdays();
  };

  return (
    <Box>
      <Typography variant="h6">Add Birthday</Typography>
      <form onSubmit={addBirthday} style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
        <TextField label="Name" value={name} onChange={e => setName(e.target.value)} size="small" required />
        <TextField type="date" value={date} onChange={e => setDate(e.target.value)} size="small" required InputLabelProps={{ shrink: true }} />
        <Button type="submit" variant="contained">Add</Button>
      </form>
      <Typography variant="h6">Your Birthdays</Typography>
      <List>
        {birthdays.map(b => (
          <ListItem key={b.id} secondaryAction={
            <IconButton edge="end" aria-label="delete" onClick={() => deleteBirthday(b.id)}>
              <DeleteIcon />
            </IconButton>
          }>
            {b.name} — {new Date(b.date).toLocaleDateString()}
          </ListItem>
        ))}
      </List>
    </Box>
  );
}
export default Birthdays;
