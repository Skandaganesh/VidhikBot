import React from 'react';
import { Link } from 'react-router-dom';
import { Box, Button, AppBar, Toolbar, Typography } from '@mui/material';

const Navbar = ({ closeNavbarAndChatBot }) => {
  return (
    <AppBar
      position="sticky"
      sx={{
        background: 'linear-gradient(to right,rgb(21, 21, 21), #333, #1a1a1a)', 
      }}
    >
      <Toolbar>
        <Typography
          variant="h6"
          sx={{ flexGrow: 1, color: 'red', fontWeight: 'bold', cursor: 'pointer' }}
          onClick={closeNavbarAndChatBot}
        >
          VidhikBot
        </Typography>
        <Box sx={{ display: 'flex', gap: 3 }}>
          <Button
            component={Link}
            to="/"
            sx={{ color: 'white' }}
            onClick={closeNavbarAndChatBot}
          >
            Home
          </Button>
          <Button component={Link} to="/about" sx={{ color: 'white' }}>
            About Us
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
