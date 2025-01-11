import React, { useEffect, useRef, useState } from "react";
import Input from "./Input";
import Response from "../ui/Response";
import ResponseLoader from "../loaders/ResponseLoader";
import SelectionBox from "./SelectionBox";
import {
  addToLocalStorage,
  clearLocalStorage,
  getFromLocalStorage,
} from "../helpers/localStorageHelper";
import { textToSpeech } from "../helpers/textToSpeech";

const ChatSection = ({ handleHistory }) => {
  const chatRef = useRef(null);
  // const [audioSrc, setAudioSrc] = useState(null);

  const colleges = [];

  const selectCollege = (collegeInd) => {
    const message = `I got it, now you can ask me about ${colleges[collegeInd]}`;
    setChats((prev) => [
      ...chats.slice(0, 1),
      { content: message, isUser: false },
    ]);
  };

  const initialChats = [
    {
      content: "Hey there!, How can I assist you today? 😊",
      isUser: false,
    },
    // {
    //   content:<SelectionBox colleges={colleges} selectCollege={selectCollege} />,
    //   isUser:false
    // }
  ];

  const [chats, setChats] = useState(initialChats);
  const [isBotThinking, setIsBotThinking] = useState(false);

  const scrollToBottom = () => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [chats]);

  const getUserInput = (value) => {
    setChats((prev) => [...prev, { content: value, isUser: true }]);
    setIsBotThinking(true);

    getChatBotResponse(value);
  };

  const getChatBotResponse = async (userInput) => {
    const res = await fetch(`http://localhost:8000/answer`,{
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify({ user_id: getFromLocalStorage("user_id"), query: userInput }),
    });
    const data = await res.json();
    setChats((prev) => [...prev, { content: data?.answer, isUser: false }]);
    setIsBotThinking(false);
  };

  const createNewConversation = async () => {
    const res = await fetch("http://localhost:8000/end_session", {
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify({ user_id: getFromLocalStorage("user_id") }),
    });
    const data = await res.json();
    console.log(data);
    if (data.status === "success") {
      console.log("Session ended successfully");
      clearLocalStorage();
      const res = await fetch(`http://localhost:8000/start_session`);
      const data = await res.json();
      console.log(data);
      addToLocalStorage("user_id", data.user_id);
    }
    setChats(initialChats);
    // handleHistory();
  };

  const handleSpeak = async (text) => {
    try {
      const audio = await textToSpeech(text);
      audio.play();
      // setAudioSrc(audio); // Set the audio source for playback
  } catch (error) {
      console.error('Failed to generate speech:', error);
  }
  };

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
        <Input getUserInput={getUserInput} />
        {/* {<audio className="opacity-0" controls autoPlay src={audioSrc} />} */}
      </div>
      <span
        className="text-lg text-slate-700 absolute top-0 right-0 flex items-center gap-1 bg-white rounded shadow py-1 px-2"
        onClick={createNewConversation}
      >
        <i className="fa-solid fa-pen-to-square"></i>
        <p className="text-sm font-semibold">New Conversation</p>
      </span>
    </div>
  );
};

export default ChatSection;
