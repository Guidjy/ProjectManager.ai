// components
import { Link } from "react-router-dom";
// hooks
import { useState } from "react"


export default function ProjectButton({ id, name, role }) {
  
  const [projectId, setProjectId] = useState(id);

  return (
    <>
      <Link to={`/project/${projectId}`}>
        <button className="btn btn-block btn-soft btn-primary rounded-3xl mb-1">
          {name}
          <div className="ms-2 badge badge-outline badge-accent">{role}</div>
        </button>
      </Link>
    </>
  )
}