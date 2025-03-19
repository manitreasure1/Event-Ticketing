
import { Link, Route, Routes} from 'react-router-dom';
import styles from './user.module.css'
import {UserDashboardData, EventTableData, OrganizationTableData } from './user-dashboard-data';
import api from '../../../api';
import { useEffect, useState } from 'react';



export default function UserDashboard() {
  const [userOrg, SetUserOrg] = useState([])
  const [userAttend, SetAttend] = useState([])

  const token = sessionStorage.getItem('accessToken')

  const fetchUserOrg = async() =>{
    try{
      await api.get("/users/v1/me/organizations/", {headers:{'Authorization': `Bearer ${token}`}})
      .then((res)=>{
        SetUserOrg(res.data)  
        console.log(`my organizations ${JSON.stringify(res.data)}`)
      })
    }catch(err){
      console.error(err)
    }
  }

  const fetchUserAttendingEvents = async() =>{
    try{
      await api.get("/users/v1/me/events/", {headers:{'Authorization': `Bearer ${token}`}})
      .then((res)=>{
        SetAttend(res.data)
      })

    }catch(err){
      console.error(err)
    }

  }

  
  useEffect(()=>{
    fetchUserAttendingEvents();
    fetchUserOrg();
  }, [])


  

  const OrganizationData =()=>{
    return(
    <>
      <UserDashboardData lable1="ORG's" lable1Data='2' lable2='Tickets' lable2Data='34' lable3='Active' lable3Data='89' lable4='Visitors' lable4Data='99'/>
        <hr />
      <OrganizationTableData orgData={userOrg}/>
        
    </>
    );
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
            <th>Venue</th>
            <th>Starts</th>
            <th>Ends</th>
            <th>Days</th>
            <th>Booked</th>
            <th>status</th>
          </tr>      
        </thead>
        <tbody>
          <EventTableData tableData={userAttend}/>          
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
          
          <li><Link to="/dashboard/events">Event</Link></li>
          <li><Link to="/dashboard/organizations">Organization</Link></li>
        </ul>
      </nav>
      <hr />
    <Routes>
      <Route index element={<EventData />} />
      <Route path="events" element={<EventData />} />
      <Route path="organizations" element={<OrganizationData/>}/>
    </Routes>
      
    </div>
  )
}

