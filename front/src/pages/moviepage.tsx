import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import './moviepage.css';

interface Data {
  id: number;
  title: string;
  synopsis: string;
  banner: string;
  year: number;
  duration: number;
  rating: string;
  genres: string;
  actors: string;
}

interface RandData {
  id: number;
  title: string;
  year: number;
  rating: number;
  genres: string;
  duration: number;
  synopsis: string;
  poster: string;
  banner: string;
  trailer: string;
  actors: string;
  created_at: string;
  updated_at: string;
}

const MoviePage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const handlePlay = () => {
    navigate(`/player/${id}`);
  };

  const [data, setData] = useState<Data | null>(null);
  const [recommendations, setRecommendations] = useState<RandData[]>([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/id/${id}`)
      .then(response => response.json())
      .then(data => {
        console.log('Data fetched:', data);
        setData(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });

    fetch('http://localhost:8000/api/rand/8')
      .then(response => response.json())
      .then(data => {
        console.log('Random movies fetched:', data);
        setRecommendations(data);
      })
      .catch(error => {
        console.error('Error fetching random movies:', error);
      });
  }, [id]);

  const formatDuration = (minutes: number) => {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}h ${mins}m`;
  };

  return (
    <div className="movie-page">
      <div className="movie-banner">
        <img
          className="banner-image"
          src={data?.banner || 'https://via.placeholder.com/1920x1080?text=Movie+Banner'}
          alt={`Movie Banner ${data?.title || id}`}
        />
        <div className="movie-info">
          <h1 className="movie-title">{data?.title || `Movie Title ${id}`}</h1>
          <div className="movie-details">
            <span>📅 {data?.year}</span> | <span>⏳ {data ? formatDuration(data.duration) : ''}</span> | <span>⭐ {data?.rating}</span> | <span>🎬 {data?.genres}</span>
          </div>
          <p className="movie-description">
            {data?.synopsis || 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.'}
          </p>
          <div className="movie-buttons">
            <button className="play-button" onClick={handlePlay}>Play</button>
            {/* <button className="my-list-button">My List</button> */}
          </div>
        </div>
      </div>

      <div className="movie-cast">
        <h2>Cast</h2>
        <div className="cast-list">
          {data?.actors.split(',').map((actor, index) => (
            <div className="cast-member" key={index}>
              <img src={`https://via.placeholder.com/100?text=${actor.trim()}`} alt={actor.trim()} />
              <p>{actor.trim()}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="movie-recommendations">
        <h2>Recommendations</h2>
        <div className="recommendation-list">
          {recommendations.map((movie) => (
            <Link to={`/movie/${movie.id}`} key={movie.id}>
              <div className="recommendation">
                <img src={movie.poster} alt={movie.title} />
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MoviePage;