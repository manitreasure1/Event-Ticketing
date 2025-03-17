import { useState } from "react"
import PropTypes from 'prop-types'
import axios from "axios"

export default function RegisterOrg({onClose}) {
    const [orgForm, SetOrgForm] = useState({
        name:"",
        email:"",
        description:""

    })

    const OnSubmit = async(e)=>{
        e.preventDefault()
        const token = sessionStorage.getItem('accessToken')
        try{
            await axios.post('http://127.0.0.1:8000/users/v1/register/organization/', orgForm,{
                headers :{
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'multipart/form-data'
                }}
            ).then((res)=>console.log(res))
        }catch(err){
            console.error(err)
        }
    }

    const handleOnChange =(e)=>{
        const {name, value} = e.target
        SetOrgForm((preForm)=>({
            ...preForm,
            [name]:value
        }))
    }
  return (
    <>

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
                    style={{resize:'none', width:'500px'}}
                        name="description" 
                         rows="7" 
                        value={orgForm.description}
                        onChange={handleOnChange}
                        placeholder="Description ...">
                    </textarea>
                </div>
                <div>
                    <button type="submit">Create Organization</button>
                </div>
            </form>
        </fieldset>
    </div>
    <div className="overlay" onClick={onClose}></div>
    </>
    
  )
}
RegisterOrg.propTypes ={
    onClose: PropTypes.func
}
