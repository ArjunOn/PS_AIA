import React, { useEffect, useState } from "react";
import { Typography, Box, TextField, Button, List, ListItem, IconButton } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import api from "../api/axios";

function Suggestions() {
  const [suggestions, setSuggestions] = useState([]);
  const [text, setText] = useState("");
  const token = localStorage.getItem("token");

  const fetchSuggestions = async () => {
    const res = await api.get("/suggestions/", { headers: { Authorization: `Bearer ${token}` } });
    setSuggestions(res.data);
  };

  useEffect(() => { fetchSuggestions(); }, []);

  const addSuggestion = async (e) => {
    e.preventDefault();
    await api.post("/suggestions/", { text }, { headers: { Authorization: `Bearer ${token}` } });
    setText("");
    fetchSuggestions();
  };

  const deleteSuggestion = async (id) => {
    await api.delete(`/suggestions/${id}`, { headers: { Authorization: `Bearer ${token}` } });
    fetchSuggestions();
  };

  return (
    <Box>
      <Typography variant="h6">Add Suggestion / Note</Typography>
      <form onSubmit={addSuggestion} style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
        <TextField label="Text" value={text} onChange={e => setText(e.target.value)} size="small" required />
        <Button type="submit" variant="contained">Add</Button>
      </form>
      <Typography variant="h6">Your Suggestions</Typography>
      <List>
        {suggestions.map(s => (
          <ListItem key={s.id} secondaryAction={
            <IconButton edge="end" aria-label="delete" onClick={() => deleteSuggestion(s.id)}>
              <DeleteIcon />
            </IconButton>
          }>
            {s.text} — {new Date(s.created_at).toLocaleString()}
          </ListItem>
        ))}
      </List>
    </Box>
  );
}
export default Suggestions;
