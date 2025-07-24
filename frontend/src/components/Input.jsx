import React, { useState } from 'react'

const Input = ({ getUserInput = async () => {}, disabled = false, placeholder = "Enter your queries..." }) => {
  const [userInput, setUserInput] = useState('');

  const handleInput = (e) => {
    setUserInput(e.target.value);
  }

  const handleSend = async () => {
    await getUserInput(userInput.trim());
    setUserInput('');
  }

  const handleKeyDown = (e) => {
    if (e.key.toLowerCase() === 'enter') {
      handleSend();
    }
  }

  return (
    <div className='flex items-center gap-3 rounded-3xl overflow-hidden border-2 border-slate-200 sm:w-10/12 w-full shadow-md py-1 px-4 bg-white' onKeyDown={handleKeyDown}>
    <input type="text" name='input' disabled={disabled} value={userInput} onChange={handleInput} placeholder={placeholder} required autoComplete='off' className='py-1 outline-none border-0 flex-1 text-lg' />
    <span className='text-lg text-slate-900'><i className="fa-solid fa-microphone"></i></span>
    <span className='text-lg text-slate-900' onClick={handleSend}><i className="fa-solid fa-paper-plane"></i></span>
    </div>
  )
}

export default Input