import React from "react";
import { Typography, Container, Button } from "@mui/material";
import { Link } from "react-router-dom";

function HomePage() {
  return (
    <Container>
      <Typography variant="h3" gutterBottom>
        Welcome to Your AI Secretary
      </Typography>
      <Typography>
        Organize your life with birthdays, meetings, to-dos, and more.
      </Typography>
      <Button variant="contained" color="primary" component={Link} to="/login">
        Get Started
      </Button>
    </Container>
  );
}
export default HomePage;
