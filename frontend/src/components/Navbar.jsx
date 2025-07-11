export default function Navbar() {
  return (
    <>
      <div className="navbar bg-base-100 shadow-sm">
        {/* Logo */}
        <div className="flex me-2 md:me-5">
          <a className="btn btn-outline border-0 text-xl">ProjectManager.ai</a>
        </div>
        {/* Create new project */}
        <div className="flex-1">
          <div className="tooltip tooltip-bottom" data-tip="create new project">
            <button className="btn btn-circle btn-outline border-0">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-8">
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
              </svg>
            </button>
          </div>
        </div>
        {/* Profile */}
        <div className="flex-none">
          <button className="btn btn-circle btn-outline border-0">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-10">
              <path strokeLinecap="round" strokeLinejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
            </svg>
          </button>
        </div>
      </div>
    </>
  );
}
