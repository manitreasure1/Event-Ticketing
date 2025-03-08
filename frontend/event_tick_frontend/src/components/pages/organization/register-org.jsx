import { useState } from "react"


export default function RegisterOrg() {
    const [orgForm, SetOrgForm] = useState({
        name:"",
        email:"",
        description:""

    })

    const OnSubmit = (e)=>{
        e.preventDefault()
    }

    const handleOnChange =(e)=>{
        const {name, value} = e.target
        SetOrgForm((preForm)=>({
            ...preForm,
            [name]:value
        }))
    }
  return (

    
    <div className="register_form form_container">
        <fieldset>
            <legend>Register Organization</legend>
            <form action="" method="post" onSubmit={OnSubmit} encType="multipart/form-data">
                <div>
                    <label htmlFor="name">Name</label>
                    <input
                    type="text"
                    name="name"
                    value={orgForm.name}
                    onChange={handleOnChange}
                    placeholder="Organization name"/>
                </div>
                <div>
                    <label htmlFor="email">Email</label>
                    <input
                    type="email"
                    name="email"
                    value={orgForm.email}
                    onChange={handleOnChange}
                    placeholder="Organization email"/>
                </div>
                <div>
                    <label htmlFor="description">About the organization</label>
                    <textarea
                        name="description" 
                        cols="30" rows="10" 
                        value={orgForm.description}
                        onChange={handleOnChange}
                        placeholder="Description ...">
                    </textarea>
                </div>
                <div>
                    <button type="submit">Create</button>
                </div>
            </form>
        </fieldset>
    </div>
  )
}
