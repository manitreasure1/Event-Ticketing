import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import axios from "axios";


export default function Highlights({ API_KEY }) {
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const HIGHLIGHT_API_URL = `https://apiv2.allsportsapi.com/football/?&met=Videos&eventId=86392&APIkey=${API_KEY}`;

  useEffect(() => {
    const fetchHighLightData = async () => {
      try {
        const response = await axios.get(HIGHLIGHT_API_URL);
        setVideos(response.data.result || []);
      } catch (err) {
        console.error(err);
        setError("Failed to load highlights.");
      } finally {
        setLoading(false);
      }
    };

    fetchHighLightData();
  }, []);

  return (
    <div className="highlights-container">
      <h1 className="highlights-title">Match Highlights</h1>

      {loading && <p className="loading-text">Loading highlights...</p>}
      {error && <p className="error-text">{error}</p>}

      <div className="highlights">
        {videos.length > 0 ? (
          videos.map((video) => (
            <div key={video.video_id} className="highlight-card">
              <video controls width="100%">
                <source src={video.video_url} type="video/mp4" />
                Your browser does not support the video tag.
              </video>
              <p className="video-title">{video.video_title || "Highlight"}</p>
            </div>
          ))
        ) : (
          !loading && !error && <p className="no-content">No highlights available.</p>
        )}
      </div>
    </div>
  );
}

Highlights.propTypes = {
  API_KEY: PropTypes.string.isRequired,
};
