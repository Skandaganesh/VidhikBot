import React, { useState } from 'react';
import ChatBotFrame from './components/ChatBotFrame';
import ChatBotIcon from './ui/ChatBotIcon';
import Navbar from './components/Navbar';
import homeimg from './assets/homeimg.jpg';
const App = () => {
  const [openChatBot, setOpenChatBot] = useState(false);

  const handleOpenChatBot = () => {
    setOpenChatBot(true); 
  };



  const closeNavbarAndChatBot = () => {
    setOpenChatBot(false); 
  };

  return (
  //      <div className={`bg-gradient-to-br from-[#4169E1] via-[#ADD8E6] to-[#4169E1] text-black h-screen relative ${
  //   openChatBot ? '' : 'overflow-hidden'
  // }`}>
  <div className={`bg-black text-black h-screen relative ${
    openChatBot ? '' : 'overflow-hidden'
  }`}>


        <Navbar closeNavbarAndChatBot={closeNavbarAndChatBot} />
        {openChatBot ? (
          <ChatBotFrame />
        ) : (
          <div
  className="flex items-start justify-start h-screen bg-cover bg-center"
  style={{ backgroundImage: `url(${homeimg})` }}
>
  <div className=" from-purple-800 to-blue-900 bg-opacity-70 p-8 rounded-lg w-3/4 md:w-1/2 ml-10 mt-40">
    <p className="text-7xl text-white font-bold mb-6 text-left mt-16 metamorphous-regular ">
      VidhikBot 
    </p>
    <p className="text-5xl text-white font-semibold mb-6 text-left  ">
    Your AI Legal Guide
    </p>
    <button
      className="px-6 py-3 mx-28 text-lg font-medium text-white bg-purple-600 rounded-lg shadow-md hover:border-2 hover:border-purple-500 hover:bg-transparent hover:scale-105 transition duration-300"
      onClick={() => handleOpenChatBot()}
    >
      Get Started
    </button>
    <ChatBotIcon handleOpenChatBot={handleOpenChatBot} />
  </div>
</div>



        
        )}
      </div>
  );
};

export default App;
