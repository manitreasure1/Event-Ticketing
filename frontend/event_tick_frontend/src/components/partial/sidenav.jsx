import { Link} from "react-router-dom";
import "./partial.css";
import PropTypes from "prop-types";


export default function Sidenav({ onClose }) {
  return (
    <>
      <nav className="sidenav">
        <div className="sidenav-header">
          <picture className="sidenav-profile">
            <img src="/image.png" alt="profile-img" />
            <span className="sidenav-username">User Name</span>
          </picture>
        </div>

        <ul className="sidenav-menu">
          <div className="sidenav-section">
            <li className="sidenav-item">
              <Link to="/dashboard/events" onClick={onClose}>
                Events
                <span className="material-symbols-outlined">event_available</span>
              </Link>
            </li>
            <li className="sidenav-item">
              <Link to="/dashboard/organizations" onClick={onClose}>
                Organizations
                <span className="material-symbols-outlined">corporate_fare</span>
              </Link>
            </li>
            <li className="sidenav-item">
              <Link to="/dashboard/tickets" onClick={onClose}>
                Tickets
                <span className="material-symbols-outlined">local_activity</span>
              </Link>
            </li>
            <li className="sidenav-item">
              <Link to="/dashboard/achieve" onClick={onClose}>
                Achieve
                <span className="material-symbols-outlined">archive</span>
              </Link>
            </li>
            <li className="sidenav-item">
              <Link to="/dashboard" onClick={onClose}> {/* Update link to point to /dashboard */}
                Dashboard
                <span className="material-symbols-outlined">dashboard</span>
              </Link>
            </li>
          </div>

          {/* Separated Settings link */}
          <div className="sidenav-section sidenav-settings">
            <li className="sidenav-item">
              <Link to="/me/settings" onClick={onClose}>
                Settings
                <span className="material-symbols-outlined">manage_accounts</span>
              </Link>
            </li>
          </div>
        </ul>
      </nav>
      <div className="overlay" onClick={onClose}></div>
    </>
  );
}

Sidenav.propTypes = {
  onClose: PropTypes.func.isRequired,
};
