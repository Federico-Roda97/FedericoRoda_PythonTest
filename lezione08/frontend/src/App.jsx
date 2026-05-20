import { useState } from 'react'
import './App.css'
import Login from './components/Login'
import Chat from './components/Chat'
import Signup from './components/Signup'

function App() {

  const [page, setPage] = useState("login")
  const toLogin = () => setPage("login")
  const toChat = () => setPage("chat")
  const toSignup = () => setPage("signup")

  return (
    <>
      {page == "login" &&
        <Login login={toChat}
          signup={toSignup} />}

      {page == "signup" &&
        <Signup login={toLogin} />}
        
      {page == "chat" && <Chat />}
    </>
  )
}

export default App
