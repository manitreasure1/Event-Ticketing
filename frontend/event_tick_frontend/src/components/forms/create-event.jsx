
import { useState } from 'react'
import  '../../pages/event/create-event.css'
import PropTypes from 'prop-types'
import api from '../../api'
export default function CreateEvent({onClose, orgId}) {
    
    const [eventForm, setEventForm] = useState({
        title: "",
        description: "",
        ticket_price: "",
        available_tickets: "",
        venue: "",
        address: "",
        start_date: "",
        end_date: ""
    })

    const onSubmit = async(e)=>{
        e.preventDefault();
        try{
            const token = sessionStorage.getItem('accessToken')
            eventForm["organization_id"] = orgId
            console.log("Event Form Data:", eventForm); 

            await api.post('/organizations/v1/create/event/', eventForm, {
                headers:{
                    "Authorization": `Bearer ${token}`,
                    'Content-Type': 'multipart/form-data'
                }
            })
            window.location.reload();
            console.log(eventForm)
        }catch(err){
            console.error(err)
        }
    }
    console.log(eventForm)
    

    const handelChange =(e)=>{
        const {name, value} = e.target;
        setEventForm((preForm)=>({
                ...preForm,
            [name] : value 
        }))

    }


  return (
    <>

    <div className=  "register_form form_container" >
        
            <legend>Add Event</legend>
        <form action="" method="post" onSubmit={onSubmit}>
            <div>
                <label htmlFor="name">Event Name</label>
                <input 
                type="text"
                name="title"
                value={eventForm.title}
                required
                onChange={handelChange}
                placeholder='My event name'/>
            </div>
            <div>
                <label htmlFor="description">Description</label>
                <textarea style={{resize:'none', width:'500px'}}
                    name="description"
                    rows="7"
                    value={eventForm.description}
                    required
                    
                    onChange={handelChange}
                    placeholder="type here ...">
                    
                </textarea>
            </div>
            <div className="box_input">
                <div>
                    <label htmlFor="ticketprice">Ticket price</label>
                    <input
                    type="text"
                    name="ticket_price"
                    required
                    value={eventForm.ticket_price}
                    onChange={handelChange}
                    placeholder='ticket price' />
                </div>
                <div>
                    <label htmlFor="available_tickets">Available Tickets</label>
                    <input
                    type="text"
                    name="available_tickets"
                    value={eventForm.available_tickets}
                    required
                    onChange={handelChange}
                    placeholder='number of tickets'  />
                </div>
            </div>
            
            <div>
                <label htmlFor="venue">Location</label>
                <input
                type="text"
                name="venue"
                value={eventForm.venue}
                onChange={handelChange}
                required
                placeholder='my event location' />
            </div>
            <div>
                <label htmlFor="address">Address</label>
                <input
                type="text"
                name="address"
                value={eventForm.address}
                required
                onChange={handelChange}
                placeholder='address' />
            </div>
            <div>
                <label htmlFor="">Date of commence</label>
                <input
                type="datetime-local" 
                name="start_date"
                value={eventForm.start_date}
                onChange={handelChange}
                required
                placeholder='date of commence'
                />
            </div>
            <div>
                <label htmlFor="">End Date</label>
                <input
                type="datetime-local" 
                name="end_date"
                value={eventForm.end_date}
                onChange={handelChange}
                required
                placeholder='end date'
                />
            </div>
            <div>
                <button type="submit">Add Event</button>
            </div>
            
        </form>
        
    </div>
        <div className='overlay' onClick={onClose}></div>
    </>
  )
}

CreateEvent.propTypes ={
    onClose: PropTypes.func.isRequired,
    orgId : PropTypes.any
}