import './partial.css';

function Footer() {
    const currentYear = new Date().getFullYear();

    return (
        <footer>
            <div className="footer-container">
                <div>
                    <h4>Company</h4>
                    <ul>
                        <li><a href="/about">About Us</a></li>
                        <li><a href="/careers">Careers</a></li>
                        <li><a href="/blog">Blog</a></li>
                        <li><a href="/partners">Partners</a></li>
                        <li><a href="/investors">Investors</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Support</h4>
                    <ul>
                        <li><a href="/faq">FAQ</a></li>
                        <li><a href="/help-center">Help Center</a></li>
                        <li><a href="/contact">Contact Us</a></li>
                        <li><a href="/report-issue">Report an Issue</a></li>
                        <li><a href="/refunds">Refund Policy</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="/terms">Terms of Service</a></li>
                        <li><a href="/privacy">Privacy Policy</a></li>
                        <li><a href="/cookies">Cookie Policy</a></li>
                        <li><a href="/security">Security</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Follow Us</h4>
                    <ul>
                        <li><a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a></li>
                        <li><a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a></li>
                        <li><a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a></li>
                        <li><a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
                        <li><a href="https://youtube.com" target="_blank" rel="noopener noreferrer">YouTube</a></li>
                    </ul>
                </div>
            </div>
            <div className="footer-bottom">
                <span> &copy; {currentYear} Event Ticketing, All rights reserved. </span>
            </div>
        </footer>
    );
}

export default Footer;
