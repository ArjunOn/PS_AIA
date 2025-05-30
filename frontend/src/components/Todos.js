import React, { useEffect, useState } from "react";
import { Typography, Box, TextField, Button, List, ListItem, Checkbox, IconButton } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import api from "../api/axios";

function Todos() {
  const [todos, setTodos] = useState([]);
  const [content, setContent] = useState("");
  const [dueDate, setDueDate] = useState("");
  const token = localStorage.getItem("token");

  const fetchTodos = async () => {
    const res = await api.get("/todos/", { headers: { Authorization: `Bearer ${token}` } });
    setTodos(res.data);
  };

  useEffect(() => { fetchTodos(); }, []);

  const addTodo = async (e) => {
    e.preventDefault();
    await api.post("/todos/", { content, due_date: dueDate, completed: false }, { headers: { Authorization: `Bearer ${token}` } });
    setContent(""); setDueDate("");
    fetchTodos();
  };

  const toggleComplete = async (todo) => {
    await api.patch(`/todos/${todo.id}`, { content: todo.content, due_date: todo.due_date, completed: !todo.completed }, { headers: { Authorization: `Bearer ${token}` } });
    fetchTodos();
  };

  const deleteTodo = async (id) => {
    await api.delete(`/todos/${id}`, { headers: { Authorization: `Bearer ${token}` } });
    fetchTodos();
  };

  return (
    <Box>
      <Typography variant="h6">Add Todo</Typography>
      <form onSubmit={addTodo} style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
        <TextField label="Task" value={content} onChange={e => setContent(e.target.value)} size="small" required />
        <TextField type="date" value={dueDate} onChange={e => setDueDate(e.target.value)} size="small" InputLabelProps={{ shrink: true }} />
        <Button type="submit" variant="contained">Add</Button>
      </form>
      <Typography variant="h6">Your Todos</Typography>
      <List>
        {todos.map(todo => (
          <ListItem key={todo.id} secondaryAction={
            <IconButton edge="end" aria-label="delete" onClick={() => deleteTodo(todo.id)}>
              <DeleteIcon />
            </IconButton>
          }>
            <Checkbox checked={todo.completed} onChange={() => toggleComplete(todo)} />
            {todo.content} {todo.due_date ? `— Due: ${new Date(todo.due_date).toLocaleDateString()}` : ""}
          </ListItem>
        ))}
      </List>
    </Box>
  );
}
export default Todos;
