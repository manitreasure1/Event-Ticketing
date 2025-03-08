import { useEffect, useState } from "react"
import axios from 'axios'
import DataTable from "../data-table";

function EventApi() {
    const [loading, setLoading] = useState(true);
    const [eventdata, setEventData] = useState([])

    const fetchEvents = async () => {
        setLoading(true)
        await axios.get('http://127.0.0.1:8000/events/v1/')
        .then(response=>{
            try{
                setEventData(response.data)
            }
            catch(error){
                console.error(error)
            }
            setLoading(false)
        })
    }
    useEffect(()=>{
        fetchEvents()
    }, [])

  return (
    
    <div>
        {loading && <div>Loading ...</div>}
        <DataTable responseData={eventdata}/>
    </div>
  )
}

export default EventApi;