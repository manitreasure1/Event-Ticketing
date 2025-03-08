
import './partial.css'
import { Link } from 'react-router-dom';


function Navbar() {
  return (
    <>
    <nav className='topnav'>
        <ul>
            <li>
               <Link to='/dicover'>Discover</Link> 
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
        <picture>
            <img src="/image.png" alt="user-profile"  />
        </picture>
    </nav>
    </>
  )
}

export default Navbar;