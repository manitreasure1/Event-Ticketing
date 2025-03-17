
import { useState } from 'react';
import styles from './user.module.css'


import PropTypes from 'prop-types';
import CreateEvent from '../event/create-event';
import RegisterOrg from '../organization/register-org';

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
  const [selectedorg, SetSelectedorg] = useState(null);
  const [showOrgForm, SetShowOrgForm] = useState(false);

  const handleClick = ()=>{
    SetShowOrgForm(!showOrgForm)
  }

  return(
    <>
    <button style={{margin:'1rem'}} onClick={handleClick}>Create Oranization</button>
    {
      orgData.length > 0 ?
        selectedorg ? (
          <Moredetails orgData={selectedorg} onBack={()=>SetSelectedorg(null)}/>
        ) : (
          <div className={styles.org_container}>
            {orgData.map((org)=>(
              <OrgCard key={org.id} org={org} onorgClick={SetSelectedorg}/>
            ))}
          </div>
        )
      : <div style={{fontSize:'3rem', margin:'5rem 0'}}> No Organization</div>
    }
    {showOrgForm && <RegisterOrg onClose={handleClick}/>}
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
  orgData : PropTypes.any,
}


const OrgCard = ({org, onorgClick})=>{
  return(
    <>
      <div className={styles.org__card} onClick={()=> onorgClick(org)}>
        <h3>{org.name}</h3>
        <img src={org.image_url} alt="org-img"/>
        <div className={styles.org__card_bottom}>
          <div>
            <b>Created by: </b>
            <span>{org.created_by}</span>
          </div>
          <div>
            <b>Events: </b>
            <span>{org.events ? org.events.length : 0}</span>
          </div>
        </div>
      </div>
    </>
  )
}
OrgCard.propTypes = {
  org: PropTypes.any,
  onorgClick: PropTypes.func
}


const Moredetails = ({orgData, onBack}) =>{
  const [showForm, SetShowForm] = useState(false);

  const handleClick =()=> {
    SetShowForm(!showForm)
  }
  console.log(showForm)
  return(
    <>
      <div className={styles.details_container}>

        <div className={styles.details_card}>
          <div style={{display:'flex', justifyContent:'space-between'}}>
            <button className={styles.back_button} onClick={onBack}>
              Back
            </button>
            <button className={styles.back_button} onClick={handleClick}>
              Create Event
            </button>
          </div>
        
          <div key={orgData.id}>
            <p><b>ID:</b> {orgData.id}</p>
            <p><b>Name:</b> {orgData.name}</p>
            <p><b>Image URL:</b> <a href={orgData.image_url} target="_blank" rel="noopener noreferrer">{orgData.image_url}</a></p>
            <p><b>Email:</b> <a href={"mailto:" + orgData.email}>{orgData.email}</a> </p>
            <p><b>Description:</b> {orgData.description}</p>
            <p><b>Created by:</b> {orgData.created_by}</p>
            <p><b>Events:</b> {orgData.events ? orgData.events.length : 0}</p>
          </div>
        </div>
      </div>
      {
        showForm && <CreateEvent onClose={handleClick} orgId={orgData.id}/>
      }
      
    </>
  )
}

Moredetails.propTypes = {
  orgData : PropTypes.any,
  onBack: PropTypes.func
}