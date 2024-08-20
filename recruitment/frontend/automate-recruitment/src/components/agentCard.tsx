import React from 'react'
import ResearchLogo from '../assets/research.png'

const AgentCard = ({logo}:{logo:string}) => {
  return (
    <div className='shadow-lg w-[140px] h-[120px] rounded-lg flex justify-center items-center'>
        <img src={logo} width={80} height={80} alt="" />
    </div>
  )
}

export default AgentCard