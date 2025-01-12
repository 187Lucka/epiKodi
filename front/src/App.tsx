import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/header';
import Banner from './components/banner';
import Row from './components/row';
import MoviePage from './pages/moviepage';
import PlayerPage from './pages/playerpage';
import { useState, useEffect } from 'react';

interface Data {
  random: {
    id: number;
    title: string;
    description: string;
    banner: string;
  };

  top_rated: Array<{
    id: number;
    title: string;
    poster: string;
  }>;

  action: Array<{
    id: number;
    title: string;
    poster: string;
  }>;

  comedy: Array<{
    id: number;
    title: string;
    poster: string;
  }>;

  horror: Array<{
    id: number;
    title: string;
    poster: string;
  }>;
}

function App() {
  const [data, setData] = useState<Data | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/home')
      .then(response => response.json())
      .then(data => {
        console.log('Data fetched:', data);
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  return (
    <Router>
      <div className="app">
        <Header />
        <div className="container">
          {loading ? (
            <div className="loading">Loading...</div>
          ) : (
            <Routes>
              <Route
                path="/"
                element={
                  <>
                    {data && (
                      <Banner id={data.random.id} title={data.random.title} description={data.random.description} bannerUrl={data.random.banner} />
                    )}
                    <div className="rows">
                      <Row title="Top Rated" movies={data?.top_rated} />
                      <Row title="Action Movies" movies={data?.action} />
                      <Row title="Comedy Movies" movies={data?.comedy} />
                      <Row title="Horror Movies" movies={data?.horror} />
                    </div>
                  </>
                }
              />
              <Route path="/movie/:id" element={<MoviePage />} />
              <Route path="/player/:id" element={<PlayerPage />} />
            </Routes>
          )}
        </div>
      </div>
    </Router>
  );
}

export default App;