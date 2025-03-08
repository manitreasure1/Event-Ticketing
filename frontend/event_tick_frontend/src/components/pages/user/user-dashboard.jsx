
import { Link, Route, Routes} from 'react-router-dom';
import styles from './user.module.css'
import UserDashboardData, { TableData } from './user-dashboard-data';

function UserDashboard() {
    const loopDetails = ()=>{
        const dmore = [];
        for(let i=0; i<=50; i++){
            dmore.push(<TableData key={i}/>)
        }
        return dmore
    }
    const OrganizationData =()=>{
      return(
        <>
      <UserDashboardData lable1="ORG's" lable1Data={2} lable2='Tickets' lable2Data={34} lable3='Active' lable3Data={89} lable4='Visitors' lable4Data={99}/>
        <hr />
        <h1>Hi</h1>
        </>
      )
    }
    const EventData =() =>{
      return(
      <>
      <UserDashboardData lable1='Event' lable1Data={78} lable2='Booked' lable2Data={34} lable3='Active' lable3Data={89} lable4='Archieve' lable4Data={99}/>
        <hr />
      <section className={styles.table_container}>
        <table>
          <thead>
            <tr>
              <th>Event</th>
              <th>Attendee Type</th>
              <th>Starts</th>
              <th>Ends</th>
              <th>Day</th>
              <th>Booked</th>
              <th>status</th>
            </tr>      
          </thead>
          <tbody>
            {loopDetails()}              
          </tbody>
        </table>
        
      </section>
      <hr />
      </>
      )
    }

    
  return (
    <div>
      
      <nav className={styles.user_dashbord_nav}>
        <ul>
          
          <li><Link to="/events">Event</Link></li>
          <li><Link to="/organizations">Organization</Link></li>
          
        </ul>
      </nav>

      <hr />
    <Routes>
      <Route index path="/events" element={<EventData/>}/>
      <Route path="/organizations" element={<OrganizationData/>}/>
    </Routes>
      
    </div>
  )
}

export default UserDashboard;