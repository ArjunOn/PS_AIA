import React, { useEffect, useState } from "react";
import { Typography, Container, TextField, Button, Alert } from "@mui/material";
import { getProfile } from "../api/auth";

function ProfilePage() {
  const [user, setUser] = useState(null);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchUser() {
      try {
        const token = localStorage.getItem("token");
        const u = await getProfile(token);
        setUser(u);
        setName(u.name || "");
        setEmail(u.email || "");
      } catch {
        setError("Could not fetch profile");
      }
    }
    fetchUser();
  }, []);

  // Add update logic as needed

  return (
    <Container maxWidth="xs">
      <Typography variant="h5" gutterBottom>Profile</Typography>
      {error && <Alert severity="error">{error}</Alert>}
      <TextField fullWidth label="Name" margin="normal" value={name} disabled />
      <TextField fullWidth label="Email" margin="normal" value={email} disabled />
      {/* Add edit/save logic as needed */}
    </Container>
  );
}
export default ProfilePage;
