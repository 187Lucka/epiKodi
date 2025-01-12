import './Row.css';
import { Link } from 'react-router-dom';

interface Movie {
  id: number;
  title: string;
  poster: string;
}

interface RowProps {
  title: string;
  movies: Movie[];
}

function Row({ title, movies }: RowProps) {
  return (
    <div className="row">
      <h2 className="row-title">{title}</h2>
      <div className="row-posters">
        {movies.map((movie) => (
          <Link to={`/movie/${movie.id}`} key={movie.id}>
            <img
              className="row-poster"
              src={movie.poster}
              alt={`Movie ${movie.title}`}
            />
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Row;
