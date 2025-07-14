// layout
import HomeLayout from "../layouts/HomeLayout";
// components
import ProjectButton from "../components/ProjectButton";
// hooks
import { useEffect } from "react";
// services
import { getUserProjects } from "../services/getUserProjects";

export default function HomePage() {

  useEffect(() => {
    getUserProjects();
  }, []);

  return (
    <>
      <HomeLayout>
        <ul>
          <li>
            <ProjectButton name="project 1" />
          </li>
          <li>
            <ProjectButton name="project 2" />
            0-0
          </li>
        </ul>
      </HomeLayout>
    </>
  );
}