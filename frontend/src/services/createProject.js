import api from "./makeRequestWithAuth";


export async function createProject(name) {

    let memberId, newProjectId;

    // creates a new project
    try {
        const response = await api.post("/projects/", {
            name: name,
            creator: localStorage.getItem("userId")
        });
        console.log(response);
        newProjectId = response.data.id;
    } catch (error) {
        console.error(error);
        return false;
    }

    // gets the member model associated with the current user
    try {
        const response = await api.get("/get-member-by-current-user/");
        memberId = response.data.id;
    } catch (error) {
        console.error(error);
        return false;
    }

    // makes the current user a manager in that project
    try {
        const response = await api.post("/roles/", {
            role: "manager",
            project: newProjectId,
            member: memberId
        })
        console.log(response);
        return response;
    } catch (error) {
        console.error(error);
        return false;
    }
}