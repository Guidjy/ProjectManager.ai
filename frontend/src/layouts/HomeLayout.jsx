// components
import Navbar from "../components/Navbar"
import Dock from "../components/Dock";
// hooks
import { useBreakpoint } from "../hooks/useBreakpoint"


export default function HomeLayout({ children }) {

  const breakPoint = useBreakpoint();
  
  return (
    <>
      <div className="">
        {breakPoint === "xs" || breakPoint === "sm" ? (
          <Dock />
        ) : (
          <Navbar />
        )}
        {children}
      </div>
    </>
  )
}