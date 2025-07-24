import React from 'react';

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
      </div>
    </nav>
  );
};

export default Navbar;
