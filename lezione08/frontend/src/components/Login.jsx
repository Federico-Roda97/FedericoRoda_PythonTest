function Login({ login, signup }) {

  async function handleSubmit(event) {
    event.preventDefault()
    let form = event.target
    let data = new FormData(form)
    let temp = Object.fromEntries(data)
    let body = JSON.stringify(temp)

    let resp = await fetch("/api/login",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: body
      })
    let json = await resp.json()

    if (json.success)
      login()
  }

  return (
    <>
      <form onSubmit={handleSubmit} className="login">
        <input name="username" />
        <input name="password" type="password" />
        <button>Login</button>
      </form>
      <div onClick={signup}>Signup</div>
    </>
  )
}

export default Login
