import React from 'react';
import ReactPlayer from 'react-player';

interface PlayerProps {
  src: string;
  poster: string;
}

const Player: React.FC<PlayerProps> = ({ src, poster }) => {
  return (
    <div className="player-container">
      <ReactPlayer
        url={src}
        controls={true}
        playing={false}
        width="100%"
        height="100%"
        light={poster}
      />
    </div>
  );
};

export default Player;