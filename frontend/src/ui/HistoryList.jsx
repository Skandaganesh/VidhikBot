import React from 'react'
import HistoryTab from './HistoryTab'

const HistoryList = ({ history }) => {
  return (
    <ul className='border border-slate-500 rounded text-white p-2 flex flex-col gap-2 flex-1 overflow-scroll'>
        <li className='flex items-center justify-between font-semibold'>History<span className='text-lg text-white'><i className="fa-solid fa-chevron-down"></i></span></li>
        {
            Array(history).fill(5).map((val,ind) => <HistoryTab key={ind} value={ind+1} />)
        }
    </ul>
  )
}

export default HistoryList