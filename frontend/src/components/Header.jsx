import React, { useState } from 'react'
import ReminderList from './ReminderList'

const Header = () => {
  const [openNotifications, setOpenNotifications] = useState(false);

  const handleNotifications = () => {
    setOpenNotifications(p => !p);
  }

  return (
    <div className='h-10 border-b-2 border-slate-500 bg-slate-900 text-white flex items-center py-1 px-3 justify-between'>
        <p>VidhikBot</p>
        <div className='flex items-center gap-6'>
        <span className='text-lg'><i className="fa-solid fa-location-dot"></i></span>
          <div className='relative' onClick={handleNotifications}>
            <span className='text-lg'><i className="fa-solid fa-bell"></i></span>
            <span className='absolute top-0 -right-1 w-2 h-2 bg-red-500 rounded-full'></span>
            {openNotifications?<span className='absolute top-4 right-0 z-10'><ReminderList /></span>:null}
          </div>
        <span className='text-lg'><i className="fa-solid fa-bars"></i></span>
        </div>
    </div>
  )
}

export default Header