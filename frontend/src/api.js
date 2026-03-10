import axios from "axios"

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
})

export const getStudents = () => API.get("/students")

export const addStudent = (data) => API.post("/students", data)

export const deleteStudent = (id) => API.delete(`/students/${id}`)

export const getStats = () => API.get("/stats")

export const exportCSV = () =>
  window.open("http://127.0.0.1:8000/export")