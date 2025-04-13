import './App.css'
import { Routes, Route, useLocation} from 'react-router-dom'
import { useEffect, useState } from 'react'
import api from './api'


import Navbar from './components/partial/navbar'
import EventCard from './components/forms/event-card'
import Footer from './components/partial/footer'

import Discover from './pages/extra/discover'
import Live from './pages/extra/live'
import UserDashboard from './utils/users/user-dashboard'



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
// <Navbar isLogin={isToken}/>
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

