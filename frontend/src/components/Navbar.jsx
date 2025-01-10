import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar = ({ closeNavbarAndChatBot }) => {
  return (
    <nav className="sticky z-10 bg-blue-500 bg-opacity-30 backdrop-filter backdrop-blur-lg fixed top-0 left-0 w-full">
      <div className="flex items-center justify-between px-6 py-4">
        <h1
          className="text-lg font-bold text-yellow-400 cursor-pointer"
          onClick={closeNavbarAndChatBot}
        >
          VidhikBot
        </h1>
        <div className="flex gap-6">
          <NavLink
            to="/"
            onClick={closeNavbarAndChatBot}
            className="text-white hover:text-yellow-300 transition duration-300"
          >
            Home
          </NavLink>
          <NavLink
            to="/about"
            className="text-white hover:text-yellow-300 transition duration-300"
          >
            About Us
          </NavLink>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
