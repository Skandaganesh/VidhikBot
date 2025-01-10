import React from 'react'

import HistoryList from '../ui/HistoryList'

const SideBar = ({ history }) => {
  return (
    <div className='border-r-2 border-slate-500 w-72 bg-slate-900 p-2 hidden sm:flex flex-col gap-4'>
        <HistoryList history={history} />
        
    </div>
  )
}

export default SideBar