import React, {useState} from 'react';
import './App.css';
import { Loading } from './Loading';
import { Search } from './Search';
import { Player } from './Player';
import { BACKEND_URL } from './config';

function App() {
  const [value, setValue] = useState('')
  const [loading, setLoading] = useState(false)
  const [loadingAudio, setLoadingAudio] = useState(false)
  const [playSong, setPlaySong] = useState(false)
  const [lyrics, setLyrics] = useState(undefined)
  const [youtubeData, setYoutubeData] = useState(undefined)
  const [error, setError] = useState(false)
  const [errorMessage, setErrorMessage] = useState("")
  const [audio, setAudio] = useState(undefined)

  const fetchLyrics = async () => {
    try {
      const response = await fetch(`${BACKEND_URL}/lyrics?song_name="${value}"`)
      const youtubeResponse = await fetch(`${BACKEND_URL}/song?song_name="${value}`)
      const data = await response.json()
      const ytData = await youtubeResponse.json()
      setLyrics(data)
      console.log(ytData)
      setYoutubeData(ytData.data)
    } catch (err) {
      setErrorMessage("We couldn't find lyrics for the chosen song. Try again with different title.")
      setError(true)
      setLoading(false)
      return
    }
    setError(false)
  }

  const fetchAudio = async () => {
    setLoadingAudio(true)
    try {
      const youtubeResponse = await fetch(`${BACKEND_URL}/download?song_name="${value}`)
      const ytData = await youtubeResponse.json()
      setAudio(new Audio(ytData))
    } catch (err) {
      setErrorMessage("We couldn't process audio for you. Try once again.")
      setError(true)
      setLoadingAudio(false)
      return
    }
    setError(false)
    setLoadingAudio(false)
    setPlaySong(true)
  }

  const fetchData = async () => {
    setLoading(true)
    await fetchLyrics()
    await fetchAudio()
    setLoading(false)
  }

  return (
    <div className="App">
      <header className="App-header">
        {loading ? <Loading loadingAudio={loadingAudio}/> :
        <>
        {playSong ? <Player setPlaySong={setPlaySong} lyricsObj={lyrics} youtubeData={youtubeData} audio={audio}/> :
        <Search value={value} setValue={setValue} setLoading={setLoading} fetchLyrics={fetchData}
        error={error} errorMessage={errorMessage}/>}
</>}
      </header>
    </div>
  );
}

export default App;


