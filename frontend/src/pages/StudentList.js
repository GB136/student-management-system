import { useEffect, useState } from "react"
import { getStudents, deleteStudent, exportCSV, getStats } from "../api"
export default function StudentList(){

const [students,setStudents]=useState([])

const loadStudents = async()=>{
const res = await getStudents()
setStudents(res.data)
}

useEffect(()=>{
loadStudents()
},[])

const handleDelete = async(id)=>{
await deleteStudent(id)
loadStudents()
}

return(

<div>

<h2>Student List</h2>

<table border="1">

<thead>

<tr>
<th>ID</th>
<th>Name</th>
<th>Birth Year</th>
<th>Major</th>
<th>GPA</th>
<th>Class ID</th>
<th>Action</th>
</tr>

</thead>

<tbody>

{students.map(s=>(
<tr key={s.student_id}>

<td>{s.student_id}</td>
<td>{s.name}</td>
<td>{s.birth_year}</td>
<td>{s.major}</td>
<td>{s.gpa}</td>
<td>{s.class_id}</td>

<td>
<button onClick={()=>handleDelete(s.student_id)}>
Delete
</button>
</td>

</tr>
))}

</tbody>

</table>

</div>

)

}
<button onClick={exportCSV}>
Export CSV
</button>
const loadStats = async () => {
 const res = await getStats()
 console.log(res.data)
}