import React, {useState, useEffect} from 'react';
import './App.css';
import { Loading } from './Loading';
import { Search } from './Search';
import { Player } from './Player';

function App() {
  const [value, setValue] = useState('')
  const [loading, setLoading] = useState(false)
  const [playSong, setPlaySong] = useState(false)

  useEffect(() => {
    if (loading) {
    const timer = setTimeout(() => {
      setLoading(false)
      setPlaySong(true)
    }, 2000);
    return () => clearTimeout(timer);
  }
  }, [loading]);
  return (
    <div className="App">
      <header className="App-header">
        {loading ? <Loading setLoading={setLoading} setPlaySong={setPlaySong}/> :
        <>
        {playSong ? <Player setPlaySong={setPlaySong} /> :
        <Search value={value} setValue={setValue} setLoading={setLoading}/>}
</>}
      </header>
    </div>
  );
}

export default App;


