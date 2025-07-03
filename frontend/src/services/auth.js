import axios from "axios";


const API_BASE_URL = import.meta.env.VITE_API_BASE;

export async function login(username, password) {
  try {
    const response = await axios.get(API_BASE_URL);
    console.log("API test successful:", response.data);
    return response.data;
  } catch (error) {
    console.error("API test failed:", error);
    throw error;
  }
}