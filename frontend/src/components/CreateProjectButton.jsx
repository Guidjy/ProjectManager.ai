// components
import { Form } from "./Form";
import { createProject } from "../services/createProject";
// hooks
import { useState } from "react";


export default function CreateProjectButton({ onProjectCreate }) {

  const [projectName, setProjectName] = useState("");

  const fields = [
    { label: "Name", type: "text", placeholder: "Project name", onChange: (event) => {setProjectName(event.target.value)} },
  ];
  
  return (
    <>
      <button className="btn btn-circle btn-outline border-0" onClick={()=>document.getElementById('create-project-form').showModal()}>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-8">
          <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
        </svg>
      </button>
      <dialog id="create-project-form" className="modal">
        <div className="modal-box w-11/12 max-w-5xl">
          <div className="w-full flex justify-center">
            <Form
            title="Create Project"
            fields={fields}
            onSubmit={async () => {await createProject(projectName); onProjectCreate();}}
            buttonText="Create Project"
            />
          </div>
        </div>
        <form method="dialog" className="modal-backdrop">
          <button>close</button>
        </form>
      </dialog>
    </>
  )
}