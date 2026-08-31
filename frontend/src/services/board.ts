import { fetchClient } from "../utils/fetchClient";

export const getBoards = async () => {
  const response = await fetchClient("/api/boards/");
  return response.json();
};

export const createBoard = async (title: string) => {
  const response = await fetchClient("/api/boards/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });
  return response.json();
};

export const getBoard = async (boardId: number) => {
  const response = await fetchClient(`/api/boards/${boardId}/`);
  return response.json();
};

export const updateBoard = async (boardId: number, title: string) => {
  const response = await fetchClient(`/api/boards/${boardId}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });
  return response.json();
};

export const deleteBoard = async (boardId: number) => {
  await fetchClient(`/api/boards/${boardId}/`, {
    method: "DELETE",
  });
};
