import React from 'react'
import '../loaders/ResponseLoader.css'
import chatbot1 from '../assets/chatbot1.jpg'

const ResponseLoader = () => {
  return (
    <div className='flex items-end gap-1'>
    <img src={chatbot1} alt="avatar" className='rounded-full shadow-sm w-8 h-8 animate-pulse' />
    <div className='border bg-white rounded shadow-sm py-1 px-2 border-l-4 border-l-slate-900'>
    <div className="loader w-16"></div>
    </div>
    </div>
  )
}

export default ResponseLoader