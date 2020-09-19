import { CircularProgress } from "@material-ui/core"
import React, {useState} from "react"
import ReactPlayer from 'react-player'
import { AnotherSongButton, StyledIconButton } from "./styles"
import './Player.css'
import { Scrollbars } from 'react-custom-scrollbars';
import logo from './karaoke_logo.png';
import PauseIcon from '@material-ui/icons/Pause';
import PlayArrowIcon from '@material-ui/icons/PlayArrow';

export const Player = ({setPlaySong}) => {
    const [playVideo, setPlayVideo] = useState(false)
    const [loading, setLoading] = useState(true)
    const audio = new Audio("./song.mp3")

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
    <div style={{pointerEvents: "none"}}>
                <ReactPlayer 
                url={"https://www.youtube.com/watch?v=fQDEUU1lyZQ&list=RDWAnYiAdr2tM"} 
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

const lyrics = ["Nos envies ne sont plus personne",
"Mais ne t'en veux pas",
"Aujourd'hui les mots m'emprisonnent",
"Mais quand tu verras",
"Dans mes nuits l'écho du sémaphore",
"Alors tu iras",
"Sans répit chasser les fantômes",
"Qui rodent avec moi",
"C'est déjà la fin de l'automne",
"Quand tu reviendras",
"Au sémaphore ton nom résonne",
"Et ne s'arrête pas, tu vois",
"Au sémaphore ton nom résonne",
"Et ne s'arrête pas, tu vois",
"Aujourd'hui les mots nous abandonnent",
"Mais il restera",
"Dans mes nuits l'écho du sémaphore",
"Et au fond les orages",
"Sans répit s'enlacent et se tordent",
"Depuis longtemps…"]