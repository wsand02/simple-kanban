import { fetchClient } from "../utils/fetchClient";

export async function getLists(boardId: number) {
  const response = await fetchClient(`/api/boards/${boardId}/lists/`);
  return response.json();
}
export async function createList(boardId: number, title: string) {
  const response = await fetchClient(`/api/boards/${boardId}/lists/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });
  return response.json();
}
    
export async function updateList(boardId: number, listId: number, title: string) {
  const response = await fetchClient(`/api/boards/${boardId}/lists/${listId}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });
  return response.json();
}

export async function deleteList(boardId: number, listId: number) {
  await fetchClient(`/api/boards/${boardId}/lists/${listId}/`, {
    method: "DELETE",
  });
}