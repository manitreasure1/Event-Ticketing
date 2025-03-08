
import { Link } from "react-router-dom"

import './partial.css'

function Sidenav() {
  return (
    <>
    <nav className="sidenav">
        <div style={{margin:'2rem 1rem', display:'flex', flexDirection:'column'}}>
            <picture>
                <img src="/image.png" alt="profile-img" width='50px' height='50px' />
                <span style={{marginLeft:'30px'}}>User Name</span>
            </picture>
            <span style={{display:'block'}}>Update Profile</span>

        </div>
        <ul>
            <div>
                
                <li>
                    <Link to='event'>Events</Link>
                </li>
                <li>
                    <Link to='organizations'>Organizations</Link>
                </li>
                <li>
                    <Link to='tickets'>Tickets</Link>
                </li>
                <li>
                    <Link to='achieve'>Achieve</Link>
                </li>
            </div>
            <div>
                <li>
                    <Link to='settings'>Settings</Link>
                </li>
            </div>
        </ul>
    </nav>
    </>
  )
}

export default Sidenav