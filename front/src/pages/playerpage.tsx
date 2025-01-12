import React, { useState, useRef, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './playerpage.css';

interface PlayerParams {
  id: string;
}

const PlayerPage: React.FC = () => {
  const { id } = useParams<PlayerParams>();
  const navigate = useNavigate();

  const videoRef = useRef<HTMLVideoElement>(null);
  const [quality, setQuality] = useState('720p');
  const [videoUrl, setVideoUrl] = useState('');
  const [qualitys, setQualitys] = useState(['']);

  const handleBack = () => {
    navigate(`/movie/${id}`);
  };

  const fetchVideoUrl = (videoId: string, videoQuality: string) => {
    const apiUrl = `http://localhost:8000/api/movies/${videoId}?quality=${videoQuality}`;
    setVideoUrl(apiUrl);
  };

  const handleQualityChange = (newQuality: string) => {
    setQuality(newQuality);
    fetchVideoUrl(id, newQuality);
  };

  const handleForward = () => {
    if (videoRef.current) {
      videoRef.current.currentTime += 10;
    }
  };

  const handleRewind = () => {
    if (videoRef.current) {
      videoRef.current.currentTime -= 10;
    }
  };

  useEffect(() => {
    const fetchVideoUrl = (videoId: string, videoQuality: string) => {
      const apiUrl = `http://localhost:8000/api/movies/${videoId}?quality=${videoQuality}`;
      console.log("Fetching video URL:", apiUrl);
      setVideoUrl(apiUrl);
    };

    const fetchQualitys = async (videoId: string) => {
      const apiUrl = `http://localhost:8000/api/resolution/${videoId}`;
      console.log("Fetching qualitys:", apiUrl);
      const response = await fetch(apiUrl);
      const data = await response.json();
      console.log("Qualitys:", data);
      setQualitys(data);
    }
  
    fetchQualitys(id);
    fetchVideoUrl(id, quality);
  }, [id, quality]);

  return (
    <div className="player-page">
      <button className="back-button" onClick={handleBack}>←</button>

      <div className="video-container">
        <video key={videoUrl} ref={videoRef} controls>
          <source src={videoUrl} type="video/mp4" />
          Votre navigateur ne prend pas en charge les vidéos HTML5.
        </video>
      </div>

      <div className="player-controls">
        <button className="control-button" onClick={handleRewind}>Rewind 10s</button>
        <button className="control-button" onClick={handleForward}>Forward 10s</button>
        <div className="quality-select">
          <span>Quality: </span>
          <select
            value={quality}
            onChange={(e) => handleQualityChange(e.target.value)}
          >
            {qualitys.map((q) => (
              <option key={q} value={q}>{q}</option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
};

export default PlayerPage;
