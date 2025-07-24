import React, { useEffect, useState } from 'react';
import ChatBotFrame from './components/ChatBotFrame';
import ChatBotIcon from './ui/ChatBotIcon';
import Navbar from './components/Navbar';
import homeimg from './assets/homeimg.jpg';
import { addToLocalStorage, clearLocalStorage, getFromLocalStorage } from './helpers/localStorageHelper';

const App = () => {
  
  useEffect(() => {
    // On load/refresh: check if there was a previous session
    const existingUser = getFromLocalStorage('user_id');
    console.log(existingUser);
    
    if (existingUser) {
      // end that session
      setIsLoading(true);
      fetch(`${process.env.REACT_APP_SITE_URL}/chat/end_session`, {
        headers: { "Content-Type": "application/json" },
        method: "POST",
        body: JSON.stringify({ user_id: existingUser })
      })
      .then(res => {
        if (res.status === 500) {
          console.warn('Failed to auto-end session:', res.status);
        }else clearLocalStorage();
        return res.json().catch(() => null);
      })
      .then(errData => {
        console.log('Auto end_session result:', errData);
      })
      .catch(err => {
        console.error('Network error ending session:', err);
      })
      .finally(() => {
        setStatusMsg("Get Started");
        setIsLoading(false);
      });
    } else setStatusMsg("Get Started");
  }, []);

  const [openChatBot, setOpenChatBot] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [statusMsg, setStatusMsg] = useState("Getting it ready...");

  const handleOpenChatBot = async () => {
    try {
      setIsLoading(true);
      setStatusMsg("Creating Session...");
      const res = await fetch(`${process.env.REACT_APP_SITE_URL}/chat/start_session`);

      if (!res.ok) {
        // Try to extract error message from server response
        let errorMsg = `Error ${res.status}`;
        try {
          const errJson = await res.json();
          errorMsg = errJson.message || JSON.stringify(errJson);
        } catch (_) {
          // ignore JSON parse error
        }
        throw new Error(errorMsg);
      }

      const data = await res.json();
      console.log("Session started:", data);
      addToLocalStorage("user_id", data.data.user_id);
      setOpenChatBot(true);
    } catch (error) {
      console.error("Failed to start chat session:", error);
      setOpenChatBot(false);
      // Optionally, show a user-friendly notification
      alert(`Could not open chatbot`);
    } finally {
      setIsLoading(false);
      setStatusMsg("Get Started");
    }
  };

  const closeNavbarAndChatBot = () => {
    setOpenChatBot(false);
  };

  return (
    <>
      <div
        className={`
        bg-black text-black relative h-screen
        ${openChatBot ? '' : 'overflow-hidden'}
      `}
      >
        <Navbar closeNavbarAndChatBot={closeNavbarAndChatBot} />

        {openChatBot ? (
          <ChatBotFrame />
        ) : (
          <div
            className="
            flex items-start justify-start h-full w-full bg-cover bg-center
            sm:bg-center md:bg-right
          "
            style={{ backgroundImage: `url(${homeimg})` }}
          >
            <div
              className="
              bg-purple-800/70 p-6 sm:p-8 md:p-12
              rounded-lg w-full sm:w-4/5 md:w-1/2 lg:w-1/3
              mx-4 sm:mx-8 md:mx-16 mt-20 sm:mt-24 md:mt-32
            "
            >
              <p className="text-4xl sm:text-5xl md:text-6xl text-white font-bold mb-4 metamorphous-regular">
                VidhikBot
              </p>
              <p className="text-2xl sm:text-3xl md:text-4xl text-white font-semibold mb-6">
                Your Indian Legal AI Guide
              </p>
              <button
                className="
                w-full sm:w-auto block sm:inline-block
                px-6 py-3 text-lg font-medium
                text-white bg-purple-600 rounded-lg shadow-md
                hover:border-2 hover:border-purple-500 hover:bg-transparent
                hover:scale-105 transition duration-300
              "
                onClick={handleOpenChatBot}
                disabled={isLoading}
              >
                {statusMsg}
              </button>
              {/* Only show chatbot icon when not loading */}
              {!isLoading && (
                <div className="mt-4 flex justify-center sm:justify-start">
                  <ChatBotIcon handleOpenChatBot={handleOpenChatBot} />
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </>
  );
};

export default App;
