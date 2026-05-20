import { useEffect, useRef, useState } from "react"

function Chat() {

  const [chat, setChat] = useState([])

  useEffect(() => { getData() }, [])

  async function getData() {
    let resp = await fetch("/api/chat") // metodo GET
    let json = await resp.json()
    // se nel json c'è la chat la scrivo in uno useState [] array
    setChat(json)
  }

  async function handleSubmit(event) {
    event.preventDefault()
    let form = event.target
    let data = new FormData(form)
    let temp = Object.fromEntries(data)
    let body = JSON.stringify(temp)

    let resp = await fetch("/api/chat",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: body
      })
    let json = await resp.json()

    if (json.success) {
      setChat( [...chat, json.data] )
      casella.current.value = ""
    }
  }

  const casella = useRef()

  return (
    <>
      <div className="messages">
        {chat.map((x, i) =>
          <div key={i} className="message">
            <h3>{x.username}</h3>
            <p>{x.message}</p>
          </div>
        )}
      </div>

      <div className="sidebar">
      </div>

      <form onSubmit={handleSubmit} className="chat">
        <textarea ref={casella} name="message">
        </textarea>
        <button>Invia</button>
      </form>
    </>
  )
}

export default Chat