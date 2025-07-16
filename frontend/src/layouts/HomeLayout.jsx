// components
import Navbar from "../components/Navbar"
import Dock from "../components/Dock";
// hooks
import { useBreakpoint } from "../hooks/useBreakpoint"


export default function HomeLayout({ children, onProjectCreate }) {

  const breakPoint = useBreakpoint();
  
  return (
    <>
      {breakPoint === "xs" || breakPoint === "sm" ? (
        <Dock onProjectCreate={onProjectCreate} />
      ) : (
        <Navbar onProjectCreate={onProjectCreate} />
      )}
      <div className="flex justify-center w-full">
        <div className="flex flex-col justify-center justify-items-center w-full md:w-4/5 lg:w-2/3 xl:w-1/2 p-5 md:p-10">
          {children}
        </div>
      </div>
    </>
  )
}