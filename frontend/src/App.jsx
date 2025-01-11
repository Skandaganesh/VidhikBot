import React, { useState } from 'react';
import ChatBotFrame from './components/ChatBotFrame';
import ChatBotIcon from './ui/ChatBotIcon';
import Navbar from './components/Navbar';
import homeimg from './assets/homeimg.jpg';
import { addToLocalStorage } from './helpers/localStorageHelper';
import TextToSpeechComponent from './components/TextToSpeech';
const App = () => {
  const [openChatBot, setOpenChatBot] = useState(false);

  const handleOpenChatBot = async () => {
    setOpenChatBot(true); 
    const res= await fetch(`http://localhost:8000/start_session`);
    const data = await res.json();
    console.log(data);
    addToLocalStorage("user_id",data.user_id);
  };



  const closeNavbarAndChatBot = () => {
    setOpenChatBot(false); 
  };

  return (<>
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
      </>
  );
};

export default App;
