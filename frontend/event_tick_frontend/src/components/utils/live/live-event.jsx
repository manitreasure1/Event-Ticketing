import axios from "axios";
import PropTypes from "prop-types";
import { useState, useEffect } from "react";


export default function LiveEvent({ API_KEY }) {
  const [live, setLive] = useState([]);
  const [selectedMatch, setSelectedMatch] = useState(null);
  const liveUrl = `https://apiv2.allsportsapi.com/football/?met=Livescore&APIkey=${API_KEY}`;

  const fetchLiveData = async () => {
    try {
      const response = await axios.get(liveUrl);
      setLive(response.data.result || []);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchLiveData();
  }, []);

  return (
    <div className="live-container">
      <h1 className="live-title">Live Matches</h1>
      {selectedMatch ? (
        <LiveDetails match={selectedMatch} onBack={() => setSelectedMatch(null)} />
      ) : (
        <div className="live-grid">
          {live.length > 0 ? (
            live.map((match) => (
              <LiveSummary key={match.event_key} match={match} onMatchClick={setSelectedMatch} />
            ))
          ) : (
            <p className="no-matches">No live matches at the moment.</p>
          )}
        </div>
      )}
    </div>
  );
}

LiveEvent.propTypes = {
  API_KEY: PropTypes.string.isRequired,
};

export function LiveSummary({ match, onMatchClick }) {
  return (
    <div className="match-card" onClick={() => onMatchClick(match)}>
      <h3 className="match-teams">{match.event_home_team} vs {match.event_away_team}</h3>
      <p className="match-date">{match.event_date} {match.event_time}</p>
      <p className="match-score">Result: {match.event_final_result || "TBD"}</p>
    </div>
  );
}

LiveSummary.propTypes = {
  match: PropTypes.object.isRequired,
  onMatchClick: PropTypes.func.isRequired,
};

export function LiveDetails({ match, onBack }) {
  return (
    <div className="match-details">
      <button className="back-button" onClick={onBack}>Back to Matches</button>
      <h2 className="details-title">{match.event_home_team} vs {match.event_away_team}</h2>
      <p className="details-info">{match.event_date} {match.event_time}</p>
      <p className="details-info">Stadium: {match.event_stadium || "Unknown"}</p>
      <p className="match-score">Final Result: {match.event_final_result || "TBD"}</p>

      <div className="details-section">
        <h3>Goalscorers</h3>
        <ul>
          {match.goalscorers?.length > 0 ? (
            match.goalscorers.map((goal, index) => (
              <li key={index}>{goal.time} - {goal.home_scorer || ''} {goal.score} {goal.away_scorer || ''}</li>
            ))
          ) : (
            <p>No goals scored.</p>
          )}
        </ul>
      </div>

      <div className="details-section">
        <h3>Cards</h3>
        <ul>
          {match.cards?.length > 0 ? (
            match.cards.map((card, index) => (
              <li key={index}>{card.time} - {card.home_fault || ''} {card.card} {card.away_fault || ''}</li>
            ))
          ) : (
            <p>No cards given.</p>
          )}
        </ul>
      </div>

      <div className="details-section">
        <h3>Statistics</h3>
        <ul>
          {match.statistics?.length > 0 ? (
            match.statistics.map((stat, index) => (
              <li key={index}>{stat.type}: Home - {stat.home}, Away - {stat.away}</li>
            ))
          ) : (
            <p>No stats available.</p>
          )}
        </ul>
      </div>
    </div>
  );
}

LiveDetails.propTypes = {
  match: PropTypes.object.isRequired,
  onBack: PropTypes.func.isRequired,
};
