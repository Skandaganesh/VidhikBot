import React, { useState } from 'react'

import SideBar from './SideBar'
import ChatSection from './ChatSection'

const ChatBotFrame = () => {
  const MAX_NUMBER_OF_CHAT_REQUESTS = 2;

  const [history, setHistory] = useState(1);
  const [maxChatRequests, setMaxChatRequests] = useState(MAX_NUMBER_OF_CHAT_REQUESTS);

  return (
    <div className='h-full w-screen flex flex-col'>
      <div className='flex h-full'>
        {
          maxChatRequests === 0 ? (
            <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-20">
              <div className="bg-white rounded-lg p-6 max-w-xs text-center">
                <p className="text-lg font-semibold">Free Tier Limit Reached</p>
                <p className="mt-2 text-gray-600">
                  Please try again in 24 hours.
                </p>
              </div>
            </div>
          ) : <>
            <SideBar history={history} />
            <ChatSection remainingChatRequests={maxChatRequests} chatRequested={() => setMaxChatRequests(p => Math.max(0, p - 1))} handleHistory={() => setHistory(p => p + 1)} />
          </>}
      </div>
    </div>
  )
}

export default ChatBotFrame