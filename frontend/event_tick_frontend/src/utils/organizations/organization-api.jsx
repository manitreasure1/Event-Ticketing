
import { useEffect, useState } from "react";
import DataTable from "../data-table";
import api from "../../../api";

function GetOrganizationApi() {
    const [loading, setLoading] = useState(true);
    const [organizationData, setOrganizationData] = useState([]);

    const fetchOrganizations = async ()=>{
        setLoading(true)
        await api.get('/organizations/v1')
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
        {loading && <div className="loading">Loading ...</div>}
        <DataTable responseData={organizationData}/>
    </div>
  )
}

export { GetOrganizationApi};
