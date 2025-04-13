import PropTypes from 'prop-types';

export default function DataTable({responseData}) {

  return (
    <div>
        { 
        (responseData.length > 0) 
        ? (responseData.map((data) => (
            <ul key={data.id}>
                <li>
                    <h2>{data.name}</h2>
                    <p>Ticket Price: ${data.ticket_price}</p>
                    <p>Tickets Available: {data.tickets_available}</p>
                    <p>Date: {new Date(data.date).toLocaleString()}</p>
                    <p>Venue: {data.venue}</p>
                </li>
            </ul>
        )))
        :<h1>No Content</h1>
        }
        
    </div>
  )
}

DataTable.propTypes = {
    responseData : PropTypes.any.isRequired,
    id : PropTypes.any.isRequired

}