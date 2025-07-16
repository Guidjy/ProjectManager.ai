import { useParams } from "react-router-dom";

export default function ProjectPage() {
  const { projectId } = useParams();

  return (
    <div className="w-full grid grid-cols-3">
      {/* current status */}
      <div className="col-span-3 md:col-span-1">
        <div className="m-5 bg-accent h-160">
          0-0
        </div>
      </div>
      {/* kanban board & stats */}
      <div className="col-span-3 md:col-span-2">
        {/* kanban board */}
        <div className="bg-success m-5 h-110">
          0-0
        </div>
        {/* stats */}
        <div className="bg-primary m-5 h-46">
          0-0
        </div>
      </div>
    </div>
  );
}
