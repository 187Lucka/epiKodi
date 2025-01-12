import './Banner.css';
import { Link } from 'react-router-dom';

interface BannerProps {
  id: number;
  title: string;
  description: string;
  bannerUrl: string;
}

function Banner({id, title, description, bannerUrl }: BannerProps) {
  return (
    <div
      className="banner"
      style={{ backgroundImage: "url(" + bannerUrl + ")" }}
    >
      <div className="banner-content">
        <h1 className="banner-title">{title}</h1>
        <div className="banner-buttons">
          <Link to={`/player/${id}`}>
            <button className="banner-button">Play</button>
          </Link>
          <Link to={`/movie/${id}`}>
            <button className="banner-button">Information</button>
          </Link>
        </div>
        <p className="banner-description">
          {description}
        </p>
      </div>
      <div className="banner-fadeBottom"></div>
    </div>
  );
}

export default Banner;