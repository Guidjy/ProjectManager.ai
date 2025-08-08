import api from "./makeRequestWithAuth";


/*fetches data of porject by id*/
export async function getProjectData(projectId) {
    try {
        const response = await api.get(`/projects/${projectId}`);
        return response.data;
    } catch (error) {
        console.error("request failed: ", error);
        return false;
    }
}