// layout
import HomeLayout from "../layouts/HomeLayout";
// components
import ProjectButton from "../components/ProjectButton";
// hooks
import { useEffect } from "react";
import { useState } from "react";
// services
import { getUserProjects } from "../services/getUserProjects";

export default function HomePage() {

  const [projects, setProjects] = useState([]);
  const [projectCreated, setProjectCreated] = useState(false);

  // gets all of the user's projects
  useEffect(() => {
    async function fetchProjects() {
      const response = await getUserProjects();
      if (response) {
        setProjects(response);
      }
    }
    setProjectCreated(false);
    fetchProjects();
  }, [projectCreated]);

  return (
    <>
      <HomeLayout onProjectCreate={() => setProjectCreated(true)}>
        <ul>
          {projects.map((project) => {
            return (
            <li key={project.id}>
              <ProjectButton
              id={project.id}
              name={project.name}
              role={project.role}
              />
            </li>
            );
          })}
        </ul>
      </HomeLayout>
    </>
  );
}