import './App.css'
import EventCard from './components/pages/event/event-card'
// import AdminApi from './components/utils/admin/admin-api'

import {BrowserRouter, Routes, Route} from 'react-router-dom'

import Discover from './components/extra/discover'
import Live from './components/extra/live'
import Navbar from './components/partial/navbar'
import Footer from './components/partial/footer'
// import EventApi from './components/utils/events/event-api'


const responseData = [
  {
    "id": 1,
    "name": "Concert in the Park",
    "details": "A wonderful evening of music in the park.",
    "availableTickets": 100,
    "venue": "Central Park",
    "address": "123 Park Ave, New York, NY",
    "startDate": "2025-09-23T19:00:00Z",
    "endDate": "2025-09-23T22:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1514525253161-7a46d19cd809?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  },
  {
    "id": 2,
    "name": "Art Exhibition",
    "details": "An exhibition showcasing local artists.",
    "availableTickets": 50,
    "venue": "Art Gallery",
    "address": "456 Art St, New York, NY",
    "startDate": "2025-09-25T10:00:00Z",
    "endDate": "2025-09-25T18:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1513364776144-6098239c640a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80"
  },
  {
    "id": 3,
    "name": "Tech Conference 2025",
    "details": "The latest trends in technology and innovation.",
    "availableTickets": 200,
    "venue": "Innovation Center",
    "address": "789 Tech Blvd, San Francisco, CA",
    "startDate": "2025-10-10T09:00:00Z",
    "endDate": "2025-10-12T17:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1519389950473-473c88070438?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  },
  {
    "id": 4,
    "name": "Food Festival",
    "details": "A celebration of culinary delights from around the world.",
    "availableTickets": 300,
    "venue": "Festival Grounds",
    "address": "101 Food Lane, Miami, FL",
    "startDate": "2025-10-20T12:00:00Z",
    "endDate": "2025-10-22T21:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1563729781630-4e120c839560?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  },
  {
    "id": 5,
    "name": "Book Fair",
    "details": "A gathering of authors and book lovers.",
    "availableTickets": 150,
    "venue": "Convention Hall",
    "address": "222 Book Rd, Chicago, IL",
    "startDate": "2025-11-05T10:00:00Z",
    "endDate": "2025-11-07T19:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1544716278-ca5e3f42159a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  },
  {
    "id": 6,
    "name": "Classic Movie Night",
    "details": "Screening of timeless classic films.",
    "availableTickets": 80,
    "venue": "Cinema Paradiso",
    "address": "333 Film St, Los Angeles, CA",
    "startDate": "2025-11-15T20:00:00Z",
    "endDate": "2025-11-15T23:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1510172928929-1c9f1c9248b6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  },
  {
    "id": 7,
    "name": "Jazz Festival",
    "details": "Experience the smooth sounds of jazz music.",
    "availableTickets": 120,
    "venue": "Jazz Club",
    "address": "444 Jazz Ave, New Orleans, LA",
    "startDate": "2025-12-01T18:00:00Z",
    "endDate": "2025-12-03T23:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1511671782779-c97d3d27a469?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80"
  },
  {
    "id": 8,
    "name": "Holiday Market",
    "details": "Find unique gifts and holiday cheer.",
    "availableTickets": 250,
    "venue": "Town Square",
    "address": "555 Holiday Ln, Boston, MA",
    "startDate": "2025-12-15T10:00:00Z",
    "endDate": "2025-12-24T20:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1544665476-d92e593259a4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  },
  {
    "id": 9,
    "name": "Science Fair",
    "details": "Explore the wonders of scientific discovery.",
    "availableTickets": 180,
    "venue": "Science Museum",
    "address": "666 Science Dr, Seattle, WA",
    "startDate": "2026-01-10T09:00:00Z",
    "endDate": "2026-01-12T17:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1517677208170-18ee286d815a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  },
  {
    "id": 10,
    "name": "Fashion Show",
    "details": "A showcase of the latest fashion trends.",
    "availableTickets": 75,
    "venue": "Fashion Center",
    "address": "777 Style Blvd, Miami, FL",
    "startDate": "2026-02-05T19:00:00Z",
    "endDate": "2026-02-05T22:00:00Z",
    "imgUrl": "https://images.unsplash.com/photo-1515377905704-8f16b54b7aeb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
  }
]


function App() {    
  // console.log(`my secret key ${import.meta.env.API_KEY}`)

  return (
    <>
      <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Discover/>}/>
        <Route path='/tickets' element={""}/>
        <Route path='/events' element={<div style={{display:'flex', flexWrap:'wrap', justifyContent:'center'}}>
        <EventCard  responseData={responseData}/>
      </div>}/>
        <Route path='/live' element={<Live/>}/>
      </Routes>
        <Footer/> 
      </BrowserRouter>
    </>
  )
}

export default App

