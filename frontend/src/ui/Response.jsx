import React from 'react'
import person from '../assets/person1.jpg'
import chatbot1 from '../assets/chatbot1.jpg'

const Response = ({ response,isUser }) => {
  return (
    <div className={`flex items-end gap-1 ${isUser?'self-end flex-row-reverse':'self-start flex-row'} max-w-[50%]`}>
        <img src={isUser?person:chatbot1} alt="avatar" className='rounded-full shadow-sm w-8 h-8' />
        <p className={`border bg-white rounded shadow-sm py-1 px-2 ${isUser?'border-r-4 border-r-slate-900':'border-l-4 border-l-slate-900'} text-wrap break-words first-letter:capitalize`}>{response}</p>
    </div>
  )
}

export default Response