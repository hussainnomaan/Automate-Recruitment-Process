import { useState } from 'react'

// import './App.css'
import AgentCard from './components/agentCard'
import ResearchLogo from './assets/research.png'
import LinkLogo from './assets/link.png'
import ConversationLogo from './assets/speech-bubble.png'
import ReporterLogo from './assets/reporter.png'



function App() {
  const [count, setCount] = useState(0)

  return (
    <main className='w-full max-h-screen h-screen flex flex-col justify-between text-blue-600 p-4'>
          <div>
      <h1 className='text-3xl font-bold text-center'>
      HR Recruitment Automated Recruitment Process
      </h1>
          </div>
          <div className='flex justify-center w-full gap-10 '>
            <AgentCard logo={ResearchLogo}/>
          <AgentCard logo={LinkLogo}/>
          <AgentCard logo={ConversationLogo}/>
          <AgentCard logo={ReporterLogo}/>

          </div>
          <div className='w-full max-w-[700px]  mx-auto  relative'>
          {/* <label
            htmlFor="message"
             className="block  text-sm font-medium "
           >
    Your message
  </label> */}
  <textarea
    id="message"
    rows={6}
    
    className="block p-2.5 w-full text-sm text-gray-900  rounded-lg border border-gray-300 focus:ring-blue-500 bg-[#d5e1f7] focus:border-blue-500    "
    placeholder="Write your job description here..."
    defaultValue={""}
  />
  <button className='absolute bottom-0 right-0 bg-blue-900 m-2 text-white rounded-full w-[40px] h-[40px]'>send</button>


          </div>
    
    </main>
  )
}

export default App
