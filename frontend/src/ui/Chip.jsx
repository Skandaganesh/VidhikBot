import React from 'react'

const Chip = ({ label,handleClick }) => {
  return (
    <div className='border border-sky-500 text-sky-500 rounded-2xl py-[2px] px-3 capitalize hover:bg-sky-500 hover:text-white' onClick={handleClick}>
        {label}
    </div>
  )
}

export default Chip