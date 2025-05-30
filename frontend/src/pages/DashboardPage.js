import React, { useEffect, useState } from "react";
import { Typography, Container, Tabs, Tab, Box, CircularProgress } from "@mui/material";
import { getProfile } from "../api/auth";
import Birthdays from "../components/Birthdays";
import Meetings from "../components/Meetings";
import Todos from "../components/Todos";
import Suggestions from "../components/Suggestions";

function DashboardPage() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [tab, setTab] = useState(0);

  useEffect(() => {
    async function fetchUser() {
      try {
        const token = localStorage.getItem("token");
        const u = await getProfile(token);
        setUser(u);
      } catch {
        setUser(null);
      }
      setLoading(false);
    }
    fetchUser();
  }, []);

  if (loading) return <CircularProgress />;

  return (
    <Container>
      <Typography variant="h4" gutterBottom>Dashboard</Typography>
      {user && <Typography>Welcome, {user.name || user.email}!</Typography>}
      <Box sx={{ borderBottom: 1, borderColor: 'divider', mt: 3 }}>
        <Tabs value={tab} onChange={(_, v) => setTab(v)}>
          <Tab label="Birthdays" />
          <Tab label="Meetings" />
          <Tab label="Todos" />
          <Tab label="Suggestions" />
        </Tabs>
      </Box>
      <Box sx={{ mt: 2 }}>
        {tab === 0 && <Birthdays />}
        {tab === 1 && <Meetings />}
        {tab === 2 && <Todos />}
        {tab === 3 && <Suggestions />}

      </Box>
    </Container>
  );
}
export default DashboardPage;
