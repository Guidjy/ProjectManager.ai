export default function KanbanCard({ task, status }) {

  let bgColor;

  return (
    <>
      <div className="h-30 w-full mb-4 bg-success">
        <p>{task}</p>
      </div>
    </>
  );
}