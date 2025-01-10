import React, { useState } from 'react'
import Chip from '../ui/Chip'

const SelectionBox = ({ colleges,selectCollege }) => {

  return (
    <div className='flex flex-col gap-1'>
        <p className='text-sm font-semibold'>Select the college for which you want to ask queries</p>
        {
            colleges.map((college,ind) => <Chip key={ind} label={college} handleClick={() => selectCollege(ind)} />)
        }
    </div>
  )
}

export default SelectionBox