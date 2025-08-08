// hooks
import { useState } from "react";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
// services
import { getProjectData } from "../services/getProjectData";
// components
import { BigKanbanBoard } from "../components/KanbanBoard";

export default function ProjectPage() {

  const { projectId } = useParams();
  const [projectData, setProjectData] = useState({});
  

 useEffect(() => {
    async function fetchProjectData(id) {
      const response = await getProjectData(id);
      if (response) {
        console.log(response);
        setProjectData(response);
      }
    }
    fetchProjectData(projectId);
  }, [projectId]);

  return (
    <div className="w-full grid grid-cols-3">
      {/* current status */}
      <div className="col-span-3 md:col-span-1">
        <div className="m-5 h-full">
          <textarea
            readOnly
            placeholder="upload a status report to get a summary of the project's cuurrent status"
            className="textarea textarea-lg textarea-primary h-full w-full"
            value={projectData.current_status}
          />
        </div>
      </div>
      {/* kanban board & stats */}
      <div className="col-span-3 md:col-span-2 h-100">
        {/* kanban board */}
        <div className="bg-base-200 m-5 h-2/3">
          <BigKanbanBoard/>
        </div>
        {/* stats */}
        <div className="bg-primary m-5 h-1/3">
          0-0
        </div>
      </div>
    </div>
  );
}
