import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    // In a Docker environment, the frontend will call the backend
    // Since it runs in the browser, it needs to call localhost or the exposed port
    fetch('http://localhost:8000/api/hello')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch from backend')
        return res.json()
      })
      .then(data => {
        setData(data)
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <div className="App">
      <header className="header">
        <h1>Dockerized Fullstack App</h1>
        <p>FastAPI + React + Docker</p>
      </header>
      
      <main className="main-content">
        <div className="card">
          <h2>Backend Connection Status</h2>
          {loading && <p className="loading">Checking connection...</p>}
          {error && <p className="error">Error: {error}</p>}
          {data && (
            <div className="success">
              <p className="message">{data.message}</p>
              <p className="status">Status: <strong>{data.status}</strong></p>
            </div>
          )}
        </div>

        <section className="learning-steps">
          <h2>Docker Learning Steps</h2>
          <ol>
            <li>Create folders for services (frontend, backend)</li>
            <li>Write Dockerfiles for each</li>
            <li>Use docker-compose to link them</li>
            <li>Run <code>docker-compose up</code></li>
          </ol>
        </section>
      </main>
    </div>
  )
}

export default App
