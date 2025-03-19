import './App.css'
import EventCard from './components/pages/event/event-card'
// import AdminApi from './components/utils/admin/admin-api'

import { Routes, Route, useLocation} from 'react-router-dom'

import Discover from './components/extra/discover'
import Live from './components/extra/live'
import Navbar from './components/partial/navbar'
import Footer from './components/partial/footer'
import UserDashboard from './components/pages/user/user-dashboard'
// import EventApi from './components/utils/events/event-api'
import { useEffect, useState } from 'react'
import api from './api'



function App() {    
  const location = useLocation();
  const isDashboardRoute = location.pathname.startsWith('/dashboard');

  const token = sessionStorage.getItem('accessToken');
  const isToken = token ? true : false;

  const [events, SetEvents] =useState([])

  const getEvents = async()=>{
    try{

      await api.get('/events/v1/')
      .then((response)=>{
        SetEvents(response.data)
      })
    }catch(err){
      console.log(err)
    }
  }
  console.log(events)
  useEffect(()=>{
    getEvents()
  }, [])

  return (
    <>
        {!isDashboardRoute && <Navbar isLogin={isToken}/>}
        <Routes>
          <Route path='/' element={<Discover/>}/>
          <Route path='/tickets' element={""}/>
          <Route path='/events' element={<EventCard  responseData={events}/>}/>
          <Route path='/live' element={<Live/>}/>
          <Route path="/dashboard/*" element={<UserDashboard/>} />
        </Routes>
        {!isDashboardRoute && <Footer/> }
      
        
    </>
  )
}

export default App;

