import React from 'react'

const ReminderTab = ({ reminder }) => {
  return (
    <li className='text-slate-500 text-sm font-semibold border-b py-1 px-2 text-wrap break-words hover:bg-slate-50'>{reminder}</li>
  )
}

export default ReminderTab