const api =
  process.env.NODE_ENV === "productions"
    ? "http://webtemplate-flask:8080"
    : "http://localhost:8080";
export default api;
