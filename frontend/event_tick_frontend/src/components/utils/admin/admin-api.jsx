
import { useEffect, useState } from "react";
import DataTable from "../data-table";
import api from "../../../api";

function AdminApi() {
    const [dashBoardData, setDashBoardData] = useState([])
    const [loading, setLoading] = useState(false)

    const fetchDashBoardData = async()=>{
        setLoading(true)
         await api.get("/admin/v1/dashboard")
         .then(response => {
             try{
                 setDashBoardData(response.data)
             }catch(err){
                 console.log(err)
             }
             setLoading(false)
         })

    }
    useEffect(()=>{
        fetchDashBoardData()
    },[]);

  return (
    <div>
        {loading && <div>Loading ...</div>}
        <DataTable responseData={dashBoardData}/>
    </div>
  )
}

export default AdminApi;