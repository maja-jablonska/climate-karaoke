import { CircularProgress } from "@material-ui/core"
import React, {useState} from "react"
import ReactPlayer from 'react-player'
import { AnotherSongButton, StyledIconButton } from "./styles"
import './Player.css'
import { Scrollbars } from 'react-custom-scrollbars';
import logo from './karaoke_logo.png';
import PauseIcon from '@material-ui/icons/Pause';
import PlayArrowIcon from '@material-ui/icons/PlayArrow';

export const Player = ({setPlaySong, lyricsObj, youtubeData, audio}) => {
    const [playVideo, setPlayVideo] = useState(false)
    const [loading, setLoading] = useState(true)

    const {lyrics, song} = lyricsObj;
    const {id, title} = youtubeData;

    const start = () => {
        if (playVideo) { console.log("pausi9ng"); audio.pause();
        if (audio.paused) {console.log("paused");} else console.log("not paused")
        setPlayVideo(false); } 
        else { audio.play(); setPlayVideo(true); }
    }
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
                onReady={() => setLoading(false)}
            />
            </div>
            <div className="App-loading-button">
    <StyledIconButton variant="contained" onClick={start} disabled={loading}>{playVideo ? <PauseIcon/> : <PlayArrowIcon/>}</StyledIconButton>
            {loading && <CircularProgress className="App-spinner"/>}
            </div>
            </div>
        </div>
    )
}