// components
import Navbar from "../components/Navbar"
// hooks
import { useBreakpoint } from "../hooks/useBreakpoint"


export default function HomeLayout({ children }) {

  const breakPoint = useBreakpoint();
  
  return (
    <>
      <div className="">
        {breakPoint === "xs" || breakPoint === "sm" ? (
          <h1>MOBILE LAYOUT</h1>
        ) : (
          <Navbar />
        )}
        {children}
      </div>
    </>
  )
}