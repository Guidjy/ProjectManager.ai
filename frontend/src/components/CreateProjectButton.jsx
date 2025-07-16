import { Form } from "./Form";


export default function CreateProjectButton() {

  const fields = [
    { label: "Username", type: "text", placeholder: "username", onChange: (event) => {setUsername(event.target.value)} },
    { label: "Password", type: "password", placeholder: "password", onChange: (event) => {setPassword(event.target.value)} },
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
            onSubmit={console.log('project created')}
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