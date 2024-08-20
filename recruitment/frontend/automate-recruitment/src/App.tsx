import { useState } from 'react'

import './App.css'
import AgentCard from './components/agentCard'
import ResearchLogo from './assets/research.png'
import LinkLogo from './assets/link.png'
import ConversationLogo from './assets/speech-bubble.png'
import ReporterLogo from './assets/reporter.png'



function App() {
  const [count, setCount] = useState(0)

  return (
    <main className='w-full h-screen flex flex-col justify-between text-blue-600'>
          <div>
      <h1 className='text-3xl font-bold'>
      HR Recruitment Automated Recruitment Process
      </h1>
          </div>
          <div className='flex justify-center w-full gap-10 '>
            <AgentCard logo={ResearchLogo}/>
          <AgentCard logo={LinkLogo}/>
          <AgentCard logo={ConversationLogo}/>
          <AgentCard logo={ReporterLogo}/>

          </div>
          <div></div>
    
    </main>
  )
}

export default App
