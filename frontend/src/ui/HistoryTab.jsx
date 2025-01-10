import React from 'react'

const HistoryTab = ({ value }) => {
  return (
    <li className={`border border-slate-500 rounded p-2 ${value === 1?'bg-slate-900':'bg-slate-800'} relative`}>
        <p>Chat {value}</p>
        <p className='text-xs absolute right-1 top-1'>Today</p>
    </li>
  )
}

export default HistoryTab