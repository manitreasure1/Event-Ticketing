
import './partial.css'
import { Link } from 'react-router-dom';
import Sidenav from './sidenav';
import { useState } from 'react';
import PropTypes from 'prop-types'
import UserForm from './../forms/form'



export default function Navbar({isLogin}) {
    console.log(`user has login : ${isLogin}`)

    

    const [showSidenav, SetShowSidenav] = useState(false)
    const [showForm, setShowForm] = useState(false)

    const handleSideNavClick= ()=>{
        SetShowSidenav(!showSidenav)
    }
    const handleUserFormClick = ()=>{
        setShowForm(!showForm)

    }

    const LoginOrSignUp = () =>{
        return(
            <>
                <ul style={{marginRight:'2rem',padding: '0 5px', backgroundColor:"rgb(141, 172, 170)", borderRadius:'5px'}} onClick={handleUserFormClick}>
                    <li>Login</li>
                </ul>
                
            </>

        )
    }
    
  return (
    <>
    {showForm &&<UserForm onClose={handleUserFormClick}/>}
    
    <nav className='topnav'>
        <ul>
            <li>
               <Link to='/'>Discover</Link> 
            </li>
            <li>
                <Link to='/Tickets'>Tickets</Link>
            </li>
            <li>
                <Link to='/events'>Events</Link>
            </li>
            <li>
                <Link to='/live'>Live</Link>
            </li>
        </ul>

        {isLogin ? 
            (
            <picture>
                <img src="/image.png" alt="user-profile" onClick={handleSideNavClick} />
            </picture>
            ): <LoginOrSignUp/> 
        }
    </nav>
    {showSidenav && <Sidenav onClose={handleSideNavClick}/>}
    </>
  )
}

Navbar.propTypes = {
    isLogin : PropTypes.bool.isRequired,
};