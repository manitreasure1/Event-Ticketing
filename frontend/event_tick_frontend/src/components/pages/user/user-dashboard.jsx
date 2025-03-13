
import { Link, Route, Routes} from 'react-router-dom';
import styles from './user.module.css'
import {UserDashboardData, EventTableData, OrganizationTableData } from './user-dashboard-data';



export default function UserDashboard() {
  const tableData = [
    {
      "id": 1,
      "event": "Tech Summit",
      "attendeeType": "Developer",
      "starts": "09:30 AM",
      "ends": "04:30 PM",
      "day": "Monday",
      "booked": "Yes",
      "status": "Confirmed"
    },
    {
      "id": 2,
      "event": "Marketing Webinar",
      "attendeeType": "Marketer",
      "starts": "11:00 AM",
      "ends": "12:30 PM",
      "day": "Tuesday",
      "booked": "Yes",
      "status": "Confirmed"
    },
      {
      "id": 3,
      "event": "Design Thinking Workshop",
      "attendeeType": "Designer",
      "starts": "01:00 PM",
      "ends": "03:00 PM",
      "day": "Wednesday",
      "booked": "Yes",
      "status": "Confirmed"
    },
    {
      "id": 4,
      "event": "Financial Planning Seminar",
      "attendeeType": "Investor",
      "starts": "02:30 PM",
      "ends": "04:00 PM",
      "day": "Thursday",
      "booked": "Yes",
      "status": "Confirmed"
    },
    {
      "id": 5,
      "event": "Customer Service Training",
      "attendeeType": "Representative",
      "starts": "10:00 AM",
      "ends": "12:00 PM",
      "day": "Friday",
      "booked": "Yes",
      "status": "Completed"
    },
    {
      "id": 6,
      "event": "Community Cleanup",
      "attendeeType": "Volunteer",
      "starts": "09:00 AM",
      "ends": "11:00 AM",
      "day": "Saturday",
      "booked": "Yes",
      "status": "Confirmed"
    },
    {
      "id": 7,
      "event": "Family Movie Night",
      "attendeeType": "General",
      "starts": "07:00 PM",
      "ends": "09:00 PM",
      "day": "Sunday",
      "booked": "Yes",
      "status": "Confirmed"
    },
      {
      "id": 8,
      "event": "Sales Kickoff",
      "attendeeType": "Sales",
      "starts": "08:30 AM",
      "ends": "05:30 PM",
      "day": "Monday",
      "booked": "Yes",
      "status": "Confirmed"
    },
     {
       "id": 9,
       "event": "HR Onboarding",
       "attendeeType": "New Hire",
       "starts": "10:30 AM",
       "ends": "01:30 PM",
       "day": "Tuesday",
       "booked": "Yes",
       "status": "Confirmed"
     },
     {
       "id": 10,
       "event": "Legal Compliance",
       "attendeeType": "Manager",
       "starts": "02:00 PM",
       "ends": "04:00 PM",
       "day": "Wednesday",
       "booked": "Yes",
       "status": "Confirmed"
     }
  ]
  const organizationData = [
    {
      "id": 1,
      "name": "Tech Innovators Inc.",
      "image_url": "https://example.com/tech_innovators.jpg",
      "email": "info@techinnovators.com",
      "description": "A leading organization in technological advancements and innovation.",
      "created_by": "John Doe",
      "events": [
        {
          "id": 101,
          "event": "AI Summit 2024",
          "attendeeType": "Developer",
          "starts": "09:00 AM",
          "ends": "05:00 PM",
          "day": "Monday",
          "booked": "Yes",
          "status": "Confirmed"
        },
        {
          "id": 102,
          "event": "Cloud Computing Workshop",
          "attendeeType": "Engineer",
          "starts": "10:00 AM",
          "ends": "12:00 PM",
          "day": "Tuesday",
          "booked": "Yes",
          "status": "Confirmed"
        }
      ]
    },
    {
      "id": 2,
      "name": "Global Marketing Solutions",
      "image_url": "https://example.com/global_marketing.png",
      "email": "contact@globalmarketing.net",
      "description": "Providing cutting-edge marketing strategies and solutions worldwide.",
      "created_by": "Jane Smith",
      "events": [
        {
          "id": 201,
          "event": "Digital Marketing Webinar",
          "attendeeType": "Marketer",
          "starts": "11:00 AM",
          "ends": "12:30 PM",
          "day": "Wednesday",
          "booked": "Yes",
          "status": "Confirmed"
        },
        {
          "id": 202,
          "event": "Social Media Strategy Seminar",
          "attendeeType": "Manager",
          "starts": "02:00 PM",
          "ends": "04:00 PM",
          "day": "Thursday",
          "booked": "Yes",
          "status": "Pending"
        }
      ]
    },
    {
      "id": 3,
      "name": "Community Builders Foundation",
      "image_url": "https://example.com/community_builders.jpeg",
      "email": "info@communitybuilders.org",
      "description": "Dedicated to building stronger communities through various initiatives.",
      "created_by": "David Lee",
      "events": [
        {
          "id": 301,
          "event": "Volunteer Cleanup Day",
          "attendeeType": "Volunteer",
          "starts": "09:00 AM",
          "ends": "11:00 AM",
          "day": "Saturday",
          "booked": "Yes",
          "status": "Confirmed"
        },
        {
          "id": 302,
          "event": "Community Food Drive",
          "attendeeType": "General",
          "starts": "12:00 PM",
          "ends": "02:00 PM",
          "day": "Sunday",
          "booked": "Yes",
          "status": "Confirmed"
        }
      ]
    }
  ]



  

  const OrganizationData =()=>{
    return(
    <>
      <UserDashboardData lable1="ORG's" lable1Data={2} lable2='Tickets' lable2Data={34} lable3='Active' lable3Data={89} lable4='Visitors' lable4Data={99}/>
        <hr />
        <section className={styles.table_container}>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Image</th>
              <th>Email</th>
              <th>Description</th>
              <th>Created By</th>
              <th>Event Count</th>
            </tr>     
          </thead>
          <tbody>
            <OrganizationTableData orgData={organizationData}/>
          
          </tbody>
        </table>
        </section>
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
            <th>Attendee Type</th>
            <th>Starts</th>
            <th>Ends</th>
            <th>Day</th>
            <th>Booked</th>
            <th>status</th>
          </tr>      
        </thead>
        <tbody>
          <EventTableData tableData={tableData}/>          
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
          
          <li><Link to="/my/events">Event</Link></li>
          <li><Link to="/my/organizations">Organization</Link></li>
        </ul>
      </nav>
      <hr />
    <Routes>
      <Route index path="/my/events" element={<EventData/>}/>
      <Route path="/my/organizations" element={<OrganizationData/>}/>
    </Routes>
      
    </div>
  )
}

