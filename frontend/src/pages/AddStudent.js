import { useState } from "react"
import { addStudent } from "../api"

export default function AddStudent(){

const [form,setForm]=useState({
student_id:"",
name:"",
birth_year:"",
major:"",
gpa:"",
class_id:""
})

const handleChange=(e)=>{
setForm({...form,[e.target.name]:e.target.value})
}

const handleSubmit = async (e) => {
  e.preventDefault()

  const data = {
    ...form,
    birth_year: parseInt(form.birth_year),
    gpa: parseFloat(form.gpa)
  }

  await addStudent(data)
  alert("Student added")
}

return(
<div>

<h2>Add Student</h2>

<form onSubmit={handleSubmit}>

<input name="student_id" placeholder="Student ID" onChange={handleChange}/>
<input name="name" placeholder="Name" onChange={handleChange}/>
<input name="birth_year" placeholder="Birth Year" onChange={handleChange}/>
<input name="major" placeholder="Major" onChange={handleChange}/>
<input name="gpa" placeholder="GPA" onChange={handleChange}/>
<input
  placeholder="Class ID"
  name="class_id"
  value={form.class_id}
  onChange={handleChange}
/>
<button type="submit">
Add Student
</button>

</form>

</div>
)
}