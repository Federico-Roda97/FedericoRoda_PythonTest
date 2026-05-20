
function Signup({ login }) {

  async function handleSubmit(event) {
    event.preventDefault()
    let form = event.target
    let data = new FormData(form)
    let temp = Object.fromEntries(data)
    let body = JSON.stringify(temp)

    let resp = await fetch("/api/signup",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: body
      })
    let json = await resp.json()

    if (json.success)
      login()
    else {
      alert("Dati non ammissibili")
    }
  }

  return (
    <>
      <form onSubmit={handleSubmit} className="login">
        <input name="username" />
        <input name="password" type="password" />
        <button>Signup</button>
      </form>
    </>
  )
}

export default Signup