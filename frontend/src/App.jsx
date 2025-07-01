// React
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
// stles
import './styles/App.css'
// pages
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/login' element={<LoginPage />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
