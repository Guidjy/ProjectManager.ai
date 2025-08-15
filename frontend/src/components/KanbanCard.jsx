export default function KanbanCard({ task, status }) {

  // peep this: using objects to conditionally change component styling
  const bgColorMap = {
    "to do": "bg-info",
    "in progress": "bg-warning",
    done: "bg-success",
  };

  const btnColorMap = {
    "to do": "btn-info",
    "in progress": "btn-warning",
    done: "btn-success",
  };

  return (
    <>
      <div className={`md:h-40 w-full p-1 mb-4 ${bgColorMap[status]}`}>
        <p className="w-full h-3/4">{task}</p>
        <div>
          {(status === "in progress" || status === "done") && (
            <button className={`btn btn-soft ${btnColorMap[status]}`}>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5 8.25 12l7.5-7.5" />
              </svg>
            </button>
          )}
          {(status === "to do" || status === "in progress") && (
            <button className={`btn btn-soft ${btnColorMap[status]}`}>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
              </svg>
            </button>
          )}
        </div>
      </div>
    </>
  );
}