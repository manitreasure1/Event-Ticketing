import { useState, useEffect } from "react";
import axios from "axios";
import PropTypes from "prop-types";


export default function LeaguesCard({ API_KEY, num1, num2 }) {
  const [leagues, setLeagues] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const LEAGUE_API_URL = `https://apiv2.allsportsapi.com/football/?met=Leagues&APIkey=${API_KEY}`;

  const fetchLeagueData = async () => {
    try {
      const response = await axios.get(LEAGUE_API_URL);
      setLeagues(response.data.result || []);
    } catch (err) {
      console.error(err);
      setError("Failed to load leagues.");
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => {
    fetchLeagueData();
  }, []);

  return (
    <div className="leagues-container">
      <h1 className="leagues-title">Top Leagues</h1>

      {loading && <p className="loading-text">Loading leagues...</p>}
      {error && <p className="error-text">{error}</p>}

      <div className="leagues">
        {leagues.length > 0 ? (
          leagues.slice(num1, num2).map((league) => (
            <div key={league.league_key} className="leagues__card">
              <h2 className="league-name">{league.league_name}</h2>
              <div className="league-details">
                <div className="league-info">
                  <h3>{league.league_name}</h3>
                  <img
                    src={league.league_logo}
                    width="60"
                    height="100"
                    alt={`${league.league_name} logo`}
                    loading="lazy"
                  />
                </div>
                <div className="country-info">
                  <h3>
                    {league.country_name.substring(0, 5)} <br />
                    {league.country_name.substring(5)}
                  </h3>
                  <img
                    src={league.country_logo}
                    width="100"
                    height="100"
                    alt={`${league.country_name} logo`}
                    loading="lazy"
                  />
                </div>
              </div>
            </div>
          ))
        ) : (
          !loading && !error && <p className="no-content">No leagues available.</p>
        )}
      </div>
    </div>
  );
}

LeaguesCard.propTypes = {
  API_KEY: PropTypes.string.isRequired,
  num1 : PropTypes.number,
  num2: PropTypes.number
};
