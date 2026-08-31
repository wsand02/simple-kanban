import React, { useEffect, useState } from "react";
import { getCards } from "../services/card";
import { getLists } from "../services/list";

interface CardType {
  id: number;
  title: string;
  list: number;
}

interface ListType {
  id: number;
  title: string;
}

const BoardDetail: React.FC<{ boardId: number }> = ({ boardId }) => {
  const [lists, setLists] = useState<ListType[]>([]);
  const [cards, setCards] = useState<CardType[]>([]);
  
  useEffect(() => {
    getLists(boardId).then((data: ListType[]) => {
      setLists(data);
      // Fetch cards for all lists
      Promise.all(data.map(list => getCards(boardId, list.id)))
        .then(allCards => {
          const flatCards = allCards.flat();
          setCards(flatCards);
        });
    });
  }, [boardId]);

  return (      
    <div>
      <h2>Board Details</h2>
      {lists.map(list => (
        <div key={list.id} className="list">
          <h3>{list.title}</h3>
          <div className="cards">
            {cards.filter(card => card.list === list.id).map(card => (
              <div key={card.id} className="card">
                {card.title}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default BoardDetail;