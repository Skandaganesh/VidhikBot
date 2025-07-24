import React, { useEffect, useRef, useState } from "react";
import Input from "./Input";
import Response from "../ui/Response";
import ResponseLoader from "../loaders/ResponseLoader";
import {
  addToLocalStorage,
  clearLocalStorage,
  getFromLocalStorage,
} from "../helpers/localStorageHelper";
// import { textToSpeech } from "../helpers/textToSpeech";

const ChatSection = ({ remainingChatRequests, chatRequested, handleHistory }) => {
  const chatRef = useRef(null);

  const initialChats = [
    {
      content: "Hey there!, How can I assist you today? 😊",
      isUser: false,
    }
  ];

  const [chats, setChats] = useState(initialChats);
  const [isBotThinking, setIsBotThinking] = useState(false);
  const [canChat, setCanChat] = useState(remainingChatRequests === 0);

  const scrollToBottom = () => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [chats]);

  const getUserInput = async (value) => {
    if(remainingChatRequests === 0) {
      setCanChat(false);
      return;
    }
    setChats((prev) => [...prev, { content: value, isUser: true }]);
    setIsBotThinking(true);
    await getChatBotResponse(value);
  };

  const getChatBotResponse = async (userInput) => {
    try {
      setIsBotThinking(true);
      const res = await fetch(`${process.env.REACT_APP_SITE_URL}/chat/answer`, {
        headers: { "Content-Type": "application/json" },
        method: "POST",
        body: JSON.stringify({
          user_id: getFromLocalStorage("user_id"),
          query: userInput
        }),
      });

      if (!res.ok) {
        // Try to parse server-provided error details
        let errorText = `HTTP ${res.status}`;
        try {
          const errJson = await res.json();
          errorText = errJson.error || errJson.message || JSON.stringify(errJson);
        } catch (_) {
          errorText = res.statusText;
        }
        throw new Error(errorText);
      }

      const data = await res.json();
      setChats((prev) => [...prev, { content: data.data.answer, isUser: false }]);
    } catch (err) {
      console.error("Chatbot response error:", err);
      setChats((prev) => [
        ...prev,
        { content: 'Sorry, something went wrong. Please try again.', isUser: false }
      ]);
    } finally {
      setIsBotThinking(false);
      chatRequested();
    }
  };

  const createNewConversation = async () => {
    try {
      // End existing session
      const endRes = await fetch(`${process.env.REACT_APP_SITE_URL}/chat/end_session`, {
        headers: { "Content-Type": "application/json" },
        method: "POST",
        body: JSON.stringify({ user_id: getFromLocalStorage("user_id") }),
      });

      if (endRes.status === 500) {
        throw new Error(`End session failed: ${endRes.status} ${endRes.statusText}`);
      }
      const endData = await endRes.json();
      console.log("End session response:", endData);

      // Clear session
      clearLocalStorage();

      // Start a new session
      const startRes = await fetch(`${process.env.REACT_APP_SITE_URL}/chat/start_session`);
      if (!startRes.ok) {
        throw new Error(`Start session failed: ${startRes.status} ${startRes.statusText}`);
      }
      const startData = await startRes.json();
      console.log("Start session response:", startData);
      addToLocalStorage("user_id", startData.data.user_id);

      // Reset chats
      setChats(initialChats);
      handleHistory();

    } catch (err) {
      console.error("createNewConversation error:", err);
      // Optionally notify the user
      alert(`Could not reset chat session: ${err.message}`);
    }
  };

  const handleSpeak = async (text) => {};

  if(!canChat) {
    return (
            <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-20" onClick={() => setCanChat(true)}>
              <div className="bg-white rounded-lg p-6 max-w-xs text-center">
                <p className="text-lg font-semibold">Free Tier Limit Reached</p>
                <p className="mt-2 text-gray-600">
                  Please try again in 24 hours.
                </p>
              </div>
            </div>
          )
  }

  return (
    <div className="flex-1 flex flex-col relative p-2 bg-violet-50 bg-contain bg-no-repeat bg-center">
      <div
        className="flex flex-col gap-2 overflow-y-scroll overflow-x-hidden scroll-smooth pb-28"
        ref={chatRef}
      >
        {chats.map((response, ind) => (
          <Response
            key={ind}
            response={response.content}
            isUser={response.isUser}
            handleSpeak={handleSpeak}
          />
        ))}
        {isBotThinking ? <ResponseLoader /> : null}
      </div>
      <div className="flex items-center justify-center absolute bottom-12 right-0 left-0 pb-4 px-2">
        <Input getUserInput={!isBotThinking ? getUserInput : async () => {}} disabled={isBotThinking} placeholder={`Enter your queries... ${remainingChatRequests} queries remaining in free tier`} />
      </div>
      <span
        className="text-lg text-slate-700 absolute top-0 right-0 flex items-center gap-1 bg-white rounded shadow py-1 px-2"
        onClick={() => !isBotThinking ? createNewConversation() : null}
      >
        <i className="fa-solid fa-pen-to-square"></i>
        <p className="text-sm font-semibold">New Conversation</p>
      </span>
    </div>
  );
};

export default ChatSection;
