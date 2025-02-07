
import { useState } from "react"
import styles from './form.module.css'

const UserForm = () => {
    const [isSignUp, setIsSingUp] = useState(false)
    const [formfields, setFormfields] = useState([{
        email: "",
        password: ""
    }])
    const toggleForm = ()=>{
        setIsSingUp(!isSignUp)
        setFormfields([{
            firstname: "",
            lastname: "",
            email: "",
            password: "",
            confirmPassword: ""

        }])
    }
    console.log(formfields)

    const handleSubmit =(e) => {
        e.preventDefault()
        if(isSignUp){
            const {password, confirmPassword } = formfields[0];
            if(confirmPassword !== password){
                alert("Password must match! ")
                return;
                
            }
        }
        
    }
    
    const handleChange = (e) =>{
        const {name, value} = e.target;
        const newField = [...formfields];
        newField[0][name] = value;
        setFormfields(newField)

    }
    
  return (
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
    
    <form action="" method="post" encType="multipart/form-data" onSubmit={handleSubmit}>
        {
            isSignUp 
            &&( 
            <input 
            className={styles.input}
                type="text" 
                placeholder="firstname" 
                value={formfields[0].firstname} 
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
                    value={formfields[0].lastname}
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
            value={formfields[0].email}
            required
            onChange={handleChange}

        />
        <input
            className={styles.input}
            type="password"
            name="password"
            placeholder="password"
            value={formfields[0].password}
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
                    value={formfields[0].confirmPassword}
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
  )
}

export default UserForm;