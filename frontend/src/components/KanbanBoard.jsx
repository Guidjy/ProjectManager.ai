// hooks
import { useState } from "react";
import { useEffect } from "react";
// components
import KanbanCard from "./KanbanCard";
// services
import { getKanbanCardsByProjectId } from "../services/getKanbanCards";


export function BigKanbanBoard({ projectId }) {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    async function fetchCards(projectId) {
      const response = await getKanbanCardsByProjectId(projectId);
      setCards(response);
      console.log(response)
    }
    fetchCards(projectId);
  }, []);

  return (
    <>
      <div className="w-full h-full grid grid-cols-3 gap-x-4">
        <div className="bg-neutral h-full overflow-auto px-4 pt-4">
          <KanbanCard/>
          <KanbanCard/>
          <KanbanCard/>
          <KanbanCard/>
        </div>
        <div className="bg-neutral h-full overflow-auto px-2 pt-2">1-1</div>
        <div className="bg-neutral h-full overflow-auto px-2 pt-2">2-2</div>
      </div>
    </>
  );
}