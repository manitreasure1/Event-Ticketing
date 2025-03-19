import { useState } from 'react';

const AdminForm = () => {
    const [AdminForm, setAdminForm] = useState({
        email: "",
        password: ""
    });
    
   
    const handleSubmit = (e) => {
        e.preventDefault();
        window.location.reload();
        
    };

    const handleOnChange =(e)=>{
        const {name, value} = e.target
        setAdminForm((preForm)=>({
            ...preForm,
            [name]: value
        }))
    }

    return (
        <div className='form_container register_form'>
            <h2>Admin Login</h2>
            <form action="" encType="multipart/form-data" onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        name='email'
                        value={AdminForm.email}
                        onChange={handleOnChange}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={AdminForm.password}
                        onChange={handleOnChange}
                        required
                    />
                </div>
                <button type="submit" style={{marginTop:"2rem"}}>Login</button>
            </form>
        </div>
    );
};

export default AdminForm;