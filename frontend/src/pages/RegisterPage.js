import React, { useState } from "react";
import { Typography, Container, TextField, Button, Alert } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { register } from "../api/auth";

function RegisterPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const res = await register(email, password, name);
      localStorage.setItem("token", res.access_token);
      navigate("/dashboard");
    } catch (err) {
      setError("Registration failed: " + (err.response?.data?.detail || "Unknown error"));
    }
  };

  return (
    <Container maxWidth="xs">
      <Typography variant="h5" gutterBottom>Register</Typography>
      {error && <Alert severity="error">{error}</Alert>}
      <form onSubmit={handleSubmit}>
        <TextField fullWidth label="Name" margin="normal" value={name} onChange={e => setName(e.target.value)} />
        <TextField fullWidth label="Email" margin="normal" value={email} onChange={e => setEmail(e.target.value)} />
        <TextField fullWidth label="Password" type="password" margin="normal" value={password} onChange={e => setPassword(e.target.value)} />
        <Button fullWidth variant="contained" color="primary" sx={{ mt: 2 }} type="submit">Register</Button>
      </form>
    </Container>
  );
}
export default RegisterPage;
