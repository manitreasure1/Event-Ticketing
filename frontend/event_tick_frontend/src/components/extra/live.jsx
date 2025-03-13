import './extra.css'

import LiveEvent from "../utils/live/live-event";

export default function Live(){

  const API_KEY = import.meta.env.VITE_API_KEY;
  return(
    <>
      <LiveEvent API_KEY={API_KEY}/>
    </>
  )
}