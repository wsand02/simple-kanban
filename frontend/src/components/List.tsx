import React from "react";

interface CardType {
  id: number;
  title: string;
  listId: number;
}

interface ListType {
  id: number;
  title: string;
}

interface ListProps {
  list: ListType;
  cards: CardType[];
}

const List: React.FC<ListProps> = ({ list, cards }) => {
  return (
    <div className="list">
      <h3>{list.title}</h3>
      <div className="cards">
        {cards.map(card => (
          <div key={card.id} className="card">
            {card.title}
          </div>
        ))}
      </div>
    </div>
  );
};

export default List;
