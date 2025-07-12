// layout
import HomeLayout from "../layouts/HomeLayout";
// components
import ProjectButton from "../components/ProjectButton";
// hooks
import { useEffect } from "react";
// services
import { getUserProjects } from "../services/getUserProjects";

import TestComponent from "../components/testComponent";

export default function HomePage() {

  TestComponent();

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
          </li>
        </ul>
      </HomeLayout>
    </>
  );
}