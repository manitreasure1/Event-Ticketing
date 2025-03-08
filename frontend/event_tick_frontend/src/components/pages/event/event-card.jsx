import  './create-event.css'
import { useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios'


export const CardDetails = ({data, onClose})=>{

    const [registerData, SetRegisterData] = useState({
        email: "",
        tel: ""
    })
    
    const handleSubmit = async (e)=>{
        e.preventDefault()
        try{
            const response = await axios.post('http://127.0.0.1:8000/api/tickets',{
                email:registerData.email,
                tel: registerData.tel
        })
        console.log(response.data)
        }catch(err){
            console.error(err)
    }}


    const handleChange=(e)=>{
        const {name, value} = e.target;
        SetRegisterData((prevForm)=>({
            ...prevForm,
            [name]:value
        }))
    }

    return(       
        <div>
            <div className='more-info'>
                <div className="event-card-more-info">
                    <h3>{data.name}</h3>
                    <img src="/image.png" width='98%' height='180px' alt="event-img" loading='lazy'/>
                    <p>
                        {data.details}
                    </p>
                    <div className='mini-details'>
                        <p>Available Ticket <span>{data.availableTickets}</span></p>
                        <b>{data.venue}</b>
                        <address>
                            {data.address}
                        </address>
                    </div>
                    <div className='mini-details'>
                        <p>start date <span>{data.startDate}</span></p>
                        <p>end date <span>{data.endDate}</span></p>
                    </div>
                </div>  
                
                <div className='atetendee_form'>
                    <form onSubmit={handleSubmit} method="post" encType="multipart/form-data">
                        <input
                        type="email"
                        name="email"
                        value={registerData.email}
                        onChange={handleChange}
                        placeholder='eg. example@outlook.com'
                        />
                        <input
                        type="tel"
                        name="tel"
                        value={registerData.tel}
                        onChange={handleChange}
                        placeholder='055 XXX XXXX'
                        />
                        <button type="submit">
                            Buy Ticket
                        </button>
                    </form>
                </div>
            </div>
            <div className='overlay' onClick={onClose}></div>
        </div>
    )
}


export default function EventCard({ responseData }) {
    const [showDetails, setShowDetails] = useState(null);
    const handleButtonClick = (data)=>{
        setShowDetails(data)
    }
    const handleCloseClick = ()=>{
        setShowDetails(null)
    }
    
  return (
        responseData.length > 0
        ? responseData.map((data) => (
            <div key={data.id}>
                <div className='event-card-background'>
                    <div className="event-card" style={{backgroundImage:"url(/image.png)"}}>
                        <h3>{data.name}</h3>
                        <p>{data.details.trim().substring(0, 35)} ...</p>
                        <div>
                            <p>Available Ticket <span>{data.availableTickets}</span></p>
                            <b>{data.venue}</b>
                            <address>
                                {data.address}
                            </address>
                        </div>
                        <div>
                            <p>start date <span>{data.startDate}</span></p>
                            <p>end date <span>{data.endDate}</span></p>
                            <button onClick={()=>handleButtonClick(data)}>Buy Ticket</button>
                        </div>
                    </div>        
                </div>
                {showDetails && showDetails.id === data.id && <CardDetails data={showDetails} onClose={handleCloseClick}/>}
            </div>
        )) : <h1>No Content</h1>
  )
}

EventCard.propTypes = {
    responseData : PropTypes.any.isRequired
}

CardDetails.propTypes = {
    data : PropTypes.any.isRequired,
    onClose : PropTypes.func.isRequired
}



