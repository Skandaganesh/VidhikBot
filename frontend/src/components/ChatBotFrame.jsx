import React, { useState } from 'react'

import SideBar from './SideBar'
import ChatSection from './ChatSection'

const ChatBotFrame = () => {
  const [history, setHistory] = useState(1);

  return (
    <div className='h-screen w-screen flex flex-col'>
        
        <div className='flex h-full'>
            <SideBar history={history} />
            <ChatSection handleHistory={() => setHistory(p => p+1)} />
        </div>
    </div>
  )
}

export default ChatBotFrame