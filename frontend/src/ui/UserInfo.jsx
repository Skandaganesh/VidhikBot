import React from 'react'
import person from '../assets/person1.jpg'

const UserInfo = () => {
  return (
    <div className='border rounded mt-auto bg-white flex items-center justify-between p-2'>
        <div className='flex items-center'>
        <img src={person} alt="user avatar" className='w-16 h-16 rounded-full' />
        <div>
            <p className='capitalize'>welcome back</p>
            <p className='capitalize text-lg font-semibold'>nishant</p>
        </div>
        </div>
        <span className='text-lg text-slate-900'><i className="fa-solid fa-gear"></i></span>
    </div>
  )
}

export default UserInfo