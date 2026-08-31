import { useState } from 'react'
import './App.css'
import BoardList from './components/BoardList'
import BoardDetail from './components/BoardDetail'

function App() {
  const [selectedBoardId, setSelectedBoardId] = useState<number | null>(null)

  return (
    <>
      {selectedBoardId ? (
        <>
          <button onClick={() => setSelectedBoardId(null)}>← Back to Boards</button>
          <BoardDetail boardId={selectedBoardId} />
        </>
      ) : (
        <BoardList onSelectBoard={setSelectedBoardId} />
      )}
    </>
  )
}

export default App
