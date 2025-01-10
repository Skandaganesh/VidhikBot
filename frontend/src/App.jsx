import React, { useState } from 'react'
import ChatBotFrame from './components/ChatBotFrame'
import ChatBotIcon from './ui/ChatBotIcon';


const App = () => {
  const [openChatBot, setOpenChatBot] = useState(false);

  const handleOpenChatBot = () => {
    setOpenChatBot(true);
  }

  return (
    <div className='bg-cover h-screen relative'>
      {
        openChatBot?<ChatBotFrame />:<div className='flex items-center justify-center h-full'><p className='text-5xl font-semibold'>Department of Technical Education, Rajasthan Homepage</p><ChatBotIcon handleOpenChatBot={handleOpenChatBot} /></div>
      }
    </div>
  )
}

export default App