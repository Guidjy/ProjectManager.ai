import api from "./makeRequestWithAuth";

/*gets all of the projects that the current user is a part of*/
export async function getUserProjects() {
    try {
        const response = await api.get('get-user-projects/')
        console.log(response.data);
    } catch (error) {
        console.error("request failed: ". error);
    }
}