import axios from "axios";
import { useEffect, useState } from "react";
import DataTable from "../data-table";


function GetOrganizationApi() {
    const [loading, setLoading] = useState(true);
    const [organizationData, setOrganizationData] = useState([]);

    const fetchOrganizations = async ()=>{
        setLoading(true)
        await axios.get('http://localhost:8000/organizations/')
        .then(response =>{
            try{
                setOrganizationData(response);
            }
            catch(error){
                console.log(error);
            }
            setLoading(false)
        })
    }

    useEffect(()=>{
        fetchOrganizations()
    }, [])

  return (
    <div>
        {loading && <div>Loading ...</div>}
        <DataTable responseData={organizationData}/>
    </div>
  )
}

export { GetOrganizationApi};
