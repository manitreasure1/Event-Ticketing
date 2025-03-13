
import styles from './user.module.css'


import PropTypes from 'prop-types';

export function UserDashboardData({lable1, lable1Data, lable2, lable2Data, lable3, lable3Data,lable4, lable4Data, }) {
  return (
    <>
    <section className={styles.circle__notice}>
            <div>
              {lable1}
              <span>{lable1Data}</span>
            </div>
            <div>
              {lable2}
              <span>{lable2Data}</span>
            </div>
            <div>
              {lable3}
              <span>{lable3Data}</span>
            </div>
            <div>
              {lable4}
              <span>{lable4Data}</span>
            </div>
          </section>

    </>
  );
}

export const OrganizationTableData = ({orgData}) =>{
  return(
    <>
    {orgData.map((org) => (
          <tr key={org.id}>
            <td>{org.id}</td>
            <td>{org.name}</td>
            <td>
              {org.image_url}
            </td>
            <td>{org.email}</td>
            <td>{org.description}</td>
            <td>{org.created_by}</td>
            <td>{org.events ? org.events.length : 0}</td>
          </tr>
        ))}
    </>
  )
}

export const EventTableData =({tableData})=>{
    return (
        <>

        {
          tableData.map((data)=>(
          <tr key={data.id}>
                <td>{data.event}</td>
                <td>{data.attendeeType}</td>
                <td>{data.starts}</td>
                <td>{data.ends}</td>
                <td>{data.day}</td>
                <td>{data.booked}</td>
                <td>{data.status}</td>
            </tr>   
          ))
        }
        </>
    )

}
UserDashboardData.propTypes = {
    lable1: PropTypes.string.isRequired,
    lable1Data: PropTypes.string.isRequired,
    lable2: PropTypes.string.isRequired,
    lable2Data: PropTypes.string.isRequired,
    lable3: PropTypes.string.isRequired,
    lable3Data: PropTypes.string.isRequired,
    lable4: PropTypes.string.isRequired,
    lable4Data: PropTypes.string.isRequired,
    
};

EventTableData.propTypes = {
  tableData: PropTypes.any
}
OrganizationTableData.propTypes = {
  orgData : PropTypes.any
}

