import React, { useState } from 'react';
import ChatBotFrame from './components/ChatBotFrame';
import ChatBotIcon from './ui/ChatBotIcon';
import Navbar from './components/Navbar';

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
          <div className="flex items-center justify-center h-full">
            <p className="text-5xl text-white font-semibold">
              VidhikBot : Your AI Legal Guide
            </p>
            <ChatBotIcon handleOpenChatBot={handleOpenChatBot} />
          </div>
        )}
      </div>
  );
};

export default App;
