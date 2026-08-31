import React, { useEffect, useState } from "react";
import { getBoards, createBoard, deleteBoard } from "../services/board";

interface BoardListProps {
  onSelectBoard?: (boardId: number) => void;
}

const BoardList: React.FC<BoardListProps> = ({ onSelectBoard }) => {
  const [boards, setBoards] = useState<{ id: number; title: string }[]>([]);
  const [newBoardTitle, setNewBoardTitle] = useState("");

  useEffect(() => {
    fetchBoards();
  }, []);

  const fetchBoards = async () => {
    const data = await getBoards();
    setBoards(data);
  };

  const handleCreateBoard = async () => {
    if (newBoardTitle.trim() === "") return;
    await createBoard(newBoardTitle);
    setNewBoardTitle("");
    fetchBoards();
  };

  const handleDeleteBoard = async (boardId: number) => {
    await deleteBoard(boardId);
    fetchBoards();
  };

  return (
    <div>
      <h2>Boards</h2>
      <ul>
        {boards.map((board) => (
          <li key={board.id}>
            <span onClick={() => onSelectBoard?.(board.id)} style={{ cursor: 'pointer', textDecoration: 'underline' }}>
              {board.title}
            </span>{" "}
            <button onClick={() => handleDeleteBoard(board.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <input
        type="text"
        value={newBoardTitle}
        onChange={(e) => setNewBoardTitle(e.target.value)}
        placeholder="New board title"
      />
      <button onClick={handleCreateBoard}>Create Board</button>
    </div>
  );
};

export default BoardList;