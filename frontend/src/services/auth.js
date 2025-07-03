import axios from "axios";


const API_BASE_URL = import.meta.env.VITE_API_BASE;

// attempts to log user in with username and password
export async function login(username, password) {
  
  // authenticates user
  try {
    // fetches refresh and acces tokens
    const response = await axios.post(`${API_BASE_URL}/accounts/api/token/`, {
      username: username,
      password: password
    });
    // saves username and tokens to local storage
    localStorage.setItem("user", username);
    localStorage.setItem("accessToken", response.data.access);
    localStorage.setItem("refreshToken", response.data.refresh);
  } catch (error) {
    // handle exception
    console.error("Login failed:", error);
    throw error;
  }

  // gets relevant user data
  try {
    // fetches user data
    const response = await axios.get(`${API_BASE_URL}/accounts/me/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
      },
    });
    // saves user id to local storage
    localStorage.setItem("userId", response.data.id);
  } catch (error) {
    console.error("Fetch current user data failed:", error);
    throw error;
  }
}