import React from 'react'
import chatbot1 from '../assets/chatbot1.jpg'

const ChatBotIcon = ({ handleOpenChatBot }) => {
  return (
    <img src={chatbot1} alt="chatbot icon" className={`absolute bottom-4 right-4 w-18 h-16 rounded-full shadow-2xl border border-black ${false && "animate-bounce duration-200"} hover:animate-pulse duration-200`} onClick={handleOpenChatBot} />
  )
}

export default ChatBotIcon