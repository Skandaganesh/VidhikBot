import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar = ({ closeNavbarAndChatBot }) => {
  return (
    <nav className="sticky z-10 top-0 bg-gradient-to-r from-gray-700 via-gray-800 to-black text-white shadow-lg">
      <div className="flex items-center justify-between px-6 py-4">
        <h1
          className="text-lg font-bold text-yellow-400 cursor-pointer metamorphous-regular"
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
