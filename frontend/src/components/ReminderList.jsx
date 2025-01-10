import React, { useState } from 'react'
import ReminderTab from '../ui/ReminderTab'

const ReminderList = () => {
  const [reminders, setReminders] = useState([
    'admission in jodhpur college',
    'scholarship for polytechnic students',
    'latest notifications released from DTE'
  ]);
  return (
    <ul className='bg-white rounded shadow flex flex-col overflow-hidden w-40'>
        {
            reminders.map((reminder,ind) => <ReminderTab key={ind} reminder={reminder} />)
        }
    </ul>
  )
}

export default ReminderList