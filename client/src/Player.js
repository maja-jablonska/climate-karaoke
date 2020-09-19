import React, {useState, useEffect} from "react"
import ReactPlayer from 'react-player'
import { AnotherSongButton } from "./styles"
import './Player.css'
import { Scrollbars } from 'react-custom-scrollbars';
import logo from './karaoke_logo.png';

export const Player = ({setPlaySong, lyricsObj, youtubeData, audioFile}) => {
    const [playVideo, setPlayVideo] = useState(false)
    const [audio] = useState(new Audio(audioFile))
    const [playing, setPlaying] = useState(false);

    useEffect(() => {
        playing ? audio.play() : audio.pause();
        return () => {
            audio.pause();
        }
      },
      [playing]
    );
    

    const {lyrics, song} = lyricsObj;
    const {id, title} = youtubeData;

    return(
        <div >
            <div className="Player-top-box">
                <img src={logo} className="App-logo-mini" alt="logo" />
                <AnotherSongButton variant="contained" onClick={() => setPlaySong(false)}>Choose another song</AnotherSongButton>
            </div>
            <div className="Player-lyrics">
                <Scrollbars style={{height: "70vh", marginTop: "20vh"}} className="Player-text-background">
                    {lyrics.map(l => <p>{l}</p>)}
                </Scrollbars>
            </div>
            <div className="Player-box">
                <div>
                    <h3 className="Player-h3">{song}</h3>
                    <p className="Player-p">Video: <a href={`https://www.youtube.com/watch?v=${id}`}>{title}</a></p>
                </div>
                <div style={{pointerEvents: "none"}}>
                            <ReactPlayer 
                            url={`https://www.youtube.com/watch?v=${id}`} 
                            controls={false}
                            playing={playVideo}
                            muted={true}
                            volume={0}
                            onReady={() => { setPlayVideo(true); setPlaying(true); }}
                        />
                </div>
            </div>
        </div>
    )
}