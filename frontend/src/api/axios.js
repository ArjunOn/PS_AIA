import axios from "axios";

const api = axios.create({
  baseURL: "https://ps-aia.onrender.com", // Backend URL
});

export default api;
