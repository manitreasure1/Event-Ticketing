import  './create-event.css'
import { useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios'


function PaymentMethod({ onPaymentSelect }) {
  const [selectedPayment, setSelectedPayment] = useState(null);

  const paymentOptions = [
    { id: "visa", name: "Visa", img: "/visa.png" },
    { id: "paypal", name: "PayPal", img: "/paypal.png" },
    { id: "mastercard", name: "MasterCard", img: "/mastercard.png" }
  ];

  const handleSelect = (option) => {
    setSelectedPayment(option.id);
    onPaymentSelect(option.id);
  };

  return (
    <div className="payment-container">
      <h3>Select Payment Method</h3>
      <div className="payment-options">
        {paymentOptions.map((option) => (
          <img
            key={option.id}
            src={option.img}
            alt={option.name}
            className={`payment-img ${selectedPayment === option.id ? "selected" : ""}`}
            onClick={() => handleSelect(option)}
          />
        ))}
      </div>

      {selectedPayment && (
        <div className="payment-form">
          <h4>{selectedPayment} Payment</h4>
          <input type="text" placeholder="Card Number" required />
          <input type="text" placeholder="Cardholder Name" required />
          <input type="month" placeholder="Expiry Date" required />
          <input type="password" placeholder="CVV" required />
        </div>
      )}
    </div>
  );
}

PaymentMethod.propTypes = {
  onPaymentSelect: PropTypes.func.isRequired
};


export const CardDetails = ({data, onClose})=>{
    const [selectedPayment, setSelectedPayment] = useState(null);
    const [registerData, SetRegisterData] = useState({
        email: "",
        tel: ""
    })
    
    const handleSubmit = async (e)=>{
        e.preventDefault()
        try{
            const response = await axios.post('http://127.0.0.1:8000/tickets/v1/purchase',{
                email:registerData.email,
                tel: registerData.tel,
                PaymentMethod: selectedPayment
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
                        <p> <b>start date</b>: <span> <u>{data.startDate}</u></span></p>
                        <p><b>end date</b>: <span> <u>{data.endDate}</u> </span></p>
                    </div>
                </div>  
                <PaymentMethod onPaymentSelect={setSelectedPayment}/>
                
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
    <div style={{display:'flex', flexWrap:'wrap', justifyContent:'center'}}>
        {responseData.length > 0
        ? responseData.map((data) => (
            <div key={data.id}>
                <div className='event-card-background'>
                    <div className="event-card" style={{backgroundImage:"url(/image.png)"}}>
                        <div className='event-card__text'>

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
                </div>
                {showDetails && showDetails.id === data.id && <CardDetails data={showDetails} onClose={handleCloseClick}/>}
            </div>
        )) : <h1>No Content</h1>
        }
    </div>
  )
}

EventCard.propTypes = {
    responseData : PropTypes.any.isRequired
}

CardDetails.propTypes = {
    data : PropTypes.any.isRequired,
    onClose : PropTypes.func.isRequired
}



