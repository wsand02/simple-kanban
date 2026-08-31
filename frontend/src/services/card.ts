import { fetchClient } from "../utils/fetchClient";

export async function getCards(boardId: number, listId: number) {
  const response = await fetchClient(`/api/boards/${boardId}/lists/${listId}/cards/`);
  return response.json();
}
export async function createCard(boardId: number, listId: number, title: string) {
  const response = await fetchClient(`/api/boards/${boardId}/lists/${listId}/cards/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });
  return response.json();
}

export async function updateCard(boardId: number, listId: number, cardId: number, title: string) {
  const response = await fetchClient(`/api/boards/${boardId}/lists/${listId}/cards/${cardId}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });
  return response.json();
}

export async function deleteCard(boardId: number, listId: number, cardId: number) {
  await fetchClient(`/api/boards/${boardId}/lists/${listId}/cards/${cardId}/`, {
    method: "DELETE",
  });
}