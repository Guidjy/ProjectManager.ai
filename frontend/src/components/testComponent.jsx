import { useEffect } from "react";
import api from "../services/makeRequestWithAuth";

export default function TestComponent() {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get("/accounts/me/");
        console.log("Fetched user:", response.data);
      } catch (err) {
        console.error("Failed to fetch user:", err);
      }
    };
    fetchData();
  }, []);

  return <div>Testing request</div>;
}
