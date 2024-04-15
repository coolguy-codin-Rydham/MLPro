import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Home from "./Components/Home"
import Result from "./Components/Result"
import { useState } from "react"
function App() {

  const [query, setQuery] = useState({});
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home setQuery={setQuery} query={query}/>}/>
        <Route path="/result" element={<Result/>}/>
      </Routes>
    </Router>
  )
}

export default App