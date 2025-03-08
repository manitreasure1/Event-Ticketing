
import { useState } from 'react'
import  './create-event.css'


export default function CreateEvent() {
    const [eventForm, setEventForm] = useState({
        name:"",
        description:"",
        ticket_price:"",
        available_tickets: "",
        venue:"",
        address:"",
        date:""
    })

    const onSubmit = (e)=>{
        e.preventDefault()

    }

    const onChange =(e)=>{
        const {name, value} = e.target;
        setEventForm((preForm)=>({
                ...preForm,
            [name] : value 
        }))

    }


  return (
    <div className=  "register_form form_container" >
        <fieldset>
            <legend>Add Event</legend>
        <form action="" method="post" onSubmit={onSubmit} encType="multipart/form-data">
            <div>
                <label htmlFor="name">Event Name</label>
                <input 
                type="text"
                name="name"
                value={eventForm.name}
                onChange={onChange}
                placeholder='My event name'/>
            </div>
            <div>
                <label htmlFor="description">Description</label>
                <textarea
                    name="description"
                    cols="20" rows="7"
                    value={eventForm.description}
                    onChange={onchange}
                    placeholder="type here ...">
                </textarea>
            </div>
            <div className="box_input">
                <div>
                    <label htmlFor="ticketprice">Ticket price</label>
                    <input
                    type="text"
                    name="ticket_price"
                    value={eventForm.ticket_price}
                    onChange={onChange}
                    placeholder='ticket price' />
                </div>
                <div>
                    <label htmlFor="available_tickets">Available Tickets</label>
                    <input
                    type="text"
                    name="available_tickets"
                    value={eventForm.available_tickets}
                    onChange={onChange}
                    placeholder='number of tickets'  />
                </div>
            </div>
            
            <div>
                <label htmlFor="venue">Location</label>
                <input
                type="text"
                name="venue"
                value={eventForm.venue}
                onChange={onChange}
                placeholder='my event location' />
            </div>
            <div>
                <label htmlFor="address">Address</label>
                <input
                type="text"
                name="address"
                value={eventForm.address}
                onChange={onChange}
                placeholder='address' />
            </div>
            <div>
                <label htmlFor="">Date of commence</label>
                <input
                type="datetime-local" 
                name="date"
                value={eventForm.date}
                onChange={onChange}
                placeholder='date of commence'
                />
            </div>
            <div>
                <button type="submit">Add Event</button>
            </div>
            
        </form>
        </fieldset>
    </div>
  )
}
