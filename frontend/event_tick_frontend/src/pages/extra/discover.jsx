

import Highlights from '../../utils/discovery/highlights'
import LeaguesCard from '../../utils/discovery/leagues';
import './extra.css'


function Discover() {


  
  const API_KEY = import.meta.env.VITE_API_KEY;

  return (
    <>
    <LeaguesCard API_KEY={API_KEY} num1={5} num2={14}/>
    <Highlights API_KEY={API_KEY}/>
    <LeaguesCard API_KEY={API_KEY} num1={14} num2={28}/>
    <Highlights API_KEY={API_KEY}/>
    <LeaguesCard API_KEY={API_KEY} num1={28} num2={46}/>
    </>
  )
}

export default Discover;