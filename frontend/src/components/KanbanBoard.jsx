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
        <div className="bg-neutral h-full overflow-auto px-2 pt-2">
          <h1 className="text-center mb-4 text-3xl font-semibold">to do</h1>
          <KanbanCard status="to do" task="task 1" />
        </div>
        <div className="bg-neutral h-full overflow-auto px-2 pt-2">
          <h1 className="text-center mb-4 text-3xl font-semibold">in progress</h1>
          <KanbanCard status="in progress" task="task 2"/>
        </div>
        <div className="bg-neutral h-full overflow-auto px-2 pt-2">
          <h1 className="text-center mb-4 text-3xl font-semibold">done</h1>
          <KanbanCard status="done" task="task 3"/>
        </div>
      </div>
    </>
  );
}