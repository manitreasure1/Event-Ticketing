
import  './create-event.css'


export default function CreateEvent() {
  return (
    <div className=  "register_form form_container" >
        <fieldset>
            <legend>Add Event</legend>
        <form action="" method="post" encType="multipart/form-data">
            <div>
                <label htmlFor="name">Event Name</label>
                <input type="text" name="name" placeholder='My event name'/>
            </div>
            <div>
                <label htmlFor="description">Description</label>
                <textarea name="description"  cols="20" rows="7" placeholder="type here ..."></textarea>
            </div>
            <div className="box_input">
                <div>
                    <label htmlFor="ticketprice">Ticke tprice</label>
                    <input type="text" name="ticket_price" placeholder='ticket price' />
                </div>
                <div>
                    <label htmlFor="available_tickets">Available Tickets</label>
                    <input type="text" name="available_tickets" placeholder='number of tickets'  />
                </div>
            </div>
            
            <div>
                <label htmlFor="venue">Location</label>
                <input type="text" name="venue" placeholder='my event location' />
            </div>
            <div>
                <label htmlFor="address">Address</label>
                <input type="text" name="address" placeholder='address' />
            </div>
            <div>
                <label htmlFor="">Date of commence</label>
                <input type="datetime-local" name="" id="" />
            </div>
            <div>
                <button type="submit">Add Event</button>
            </div>
            
        </form>
        </fieldset>
    </div>
  )
}
