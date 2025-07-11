// layout
import HomeLayout from "../layouts/HomeLayout";
// components
import ProjectButton from "../components/ProjectButton";

export default function HomePage() {
  return (
    <>
      <HomeLayout>
        <ul>
          <li>
            <ProjectButton name="project 1" />
          </li>
          <li>
            <ProjectButton name="project 2" />
          </li>
        </ul>
      </HomeLayout>
    </>
  );
}