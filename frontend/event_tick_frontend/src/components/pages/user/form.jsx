
import { useState } from "react"
import styles from './user.module.css'
import axios from 'axios'
import PropTypes from 'prop-types'

export default function UserForm({onClose}){

    const [isSignUp, setIsSingUp] = useState(false)
    const fields = isSignUp
     ? {
        email: "",
        password: "",
    }
     :{
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        confirmPassword: ""
    }


    const [formfields, setFormfields] = useState(fields)
    const toggleForm = ()=>{
        setIsSingUp(!isSignUp)
        setFormfields(fields)
    }

    const handleSubmit = async(e) => {
        e.preventDefault()
        if(isSignUp){
            const {password, confirmPassword } = formfields;
            if(confirmPassword !== password){
                alert("Password must match! ")
                return;
                
            }
        }
        try{
            delete formfields.confirmPassword

            const requesUrl = isSignUp
            ? 'http://127.0.0.1:8000/auth/v1/register/' 
            : 'http://127.0.0.1:8000/auth/v1/login/'

            const res = await axios.post(requesUrl, formfields,{
                  headers: {
                'Content-Type': 'multipart/form-data'
            }})
            sessionStorage.setItem('accessToken', res.data['access_token'])
        }catch(err){
            console.error(err)
        }
    }
    
    const handleChange = (e) =>{
        const {name, value} = e.target;
        setFormfields((prevForm)=>({
            ...prevForm,
            [name]: value
        }))

    }
    
  return (
    <>
        <div className="form_container register_form"> 
        <fieldset>
            <legend>{isSignUp? "Sign Up" : "Login"}</legend>

        <div className={styles.toggleForm}>
            
            <span onClick={toggleForm}
                style={{backgroundColor: isSignUp ? "black": "white", color: !isSignUp && 'black'}}>
                    Login
            </span>
            <span onClick={toggleForm}
                style={{backgroundColor: !isSignUp ? "black": "white", color: isSignUp && 'black'}}>
                    SignUp
            </span>
        </div>
        
        <form action="" method="post" onSubmit={handleSubmit}>
            {
                isSignUp 
                &&( 
                <input 
                className={styles.input}
                    type="text" 
                    placeholder="firstname" 
                    value={formfields.firstname} 
                    name="firstname" required
                    onChange={handleChange}
                />
                )
            }
            {
                isSignUp 
                &&( 
                    <input 
                    className={styles.input}
                        type="text" 
                        placeholder="lastname" 
                        value={formfields.lastname}
                        name="lastname" required
                        onChange={handleChange}

                    />
                )
            }
            <input
                className={styles.input}
                type="email" 
                name="email"
                placeholder="email"
                value={formfields.email}
                required
                onChange={handleChange}

            />
            <input
                className={styles.input}
                type="password"
                name="password"
                placeholder="password"
                value={formfields.password}
                required
                onChange={handleChange}

            />
            {
                isSignUp 
                &&( 
                    <input
                        className={styles.input}
                        type="password" 
                        name="confirmPassword" 
                        value={formfields.confirmPassword}
                        placeholder="confirm password"
                        required
                        onChange={handleChange}
                    />
                )
            }    
            <button>{isSignUp? "Sign Up" : "Login"}</button>        
        </form>
        </fieldset>
        </div>
        <div className="overlay" onClick={onClose}>
        </div>
    </>
  )
}




UserForm.propTypes = {
    onClose : PropTypes.func.isRequired
}