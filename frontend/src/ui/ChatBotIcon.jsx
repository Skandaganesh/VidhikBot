import React from 'react'
import chatbot1 from '../assets/chatbot1.jpg'

const ChatBotIcon = ({ handleOpenChatBot }) => {
  return (
    <img src={chatbot1} alt="chatbot image" className='absolute bottom-4 right-4 w-16 h-16 rounded-full shadow-2xl border border-black' onClick={handleOpenChatBot} />
  )
}

export default ChatBotIcon