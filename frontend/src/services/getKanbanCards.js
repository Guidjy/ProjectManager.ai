import api from "./makeRequestWithAuth";


/*fetches kanban cards by project id*/
export async function getKanbanCardsByProjectId(projectId) {
    try {
        const response = await api.get(`/get-cards-by-project-id/${projectId}`);
        return response.data;
    } catch (error) {
        console.error("request failed: ", error);
        return false;
    }
}