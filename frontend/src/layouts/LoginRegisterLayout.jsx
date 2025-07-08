export default function LoginRegisterLayout({ children, footer }) {
  return (
    <>
      <div className="flex flex-col justify-center items-center h-screen w-full">
        {children}
      </div>
    </>
  )
}