import { useEffect, useState } from "react"
import DataTable from "../data-table";
import api from '../../../api'

function EventApi() {
    const [loading, setLoading] = useState(true);
    const [eventdata, setEventData] = useState([])

    const fetchEvents = async () => {
        setLoading(true)
        await api.get('/events/v1/')
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
        {loading && <div className="Loading">Loading ...</div>}
        <DataTable responseData={eventdata}/>
    </div>
  )
}

export default EventApi;