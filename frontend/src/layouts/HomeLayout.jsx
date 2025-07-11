// components
import Navbar from "../components/Navbar"


export default function HomeLayout({ children }) {
  return (
    <>
      <div className="">
        <Navbar />
        {children}
      </div>
    </>
  )
}