import React, { useState } from 'react'

import SideBar from './SideBar'
import ChatSection from './ChatSection'

const ChatBotFrame = () => {
  const MAX_NUMBER_OF_CHAT_REQUESTS = 5;

  const [history, setHistory] = useState(1);
  const [maxChatRequests, setMaxChatRequests] = useState(MAX_NUMBER_OF_CHAT_REQUESTS);

  return (
    <div className='h-full w-screen flex flex-col'>
      <div className='flex h-full'>
            <SideBar history={history} />
            <ChatSection remainingChatRequests={maxChatRequests} chatRequested={() => setMaxChatRequests(p => Math.max(0, p - 1))} handleHistory={() => setHistory(p => p + 1)} />
      </div>
    </div>
  )
}

export default ChatBotFrame