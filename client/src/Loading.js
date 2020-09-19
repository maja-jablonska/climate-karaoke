import React from "react"
import './Loading.css'
import './App.css'

export const Loading = ({loadingAudio}) => {
    return (
        <div className="App-box">
            <div className="loader"/>
            <p>{loadingAudio ? "A bit more of patience. We're preparing music for you! It can take up to a minute." : "Wait a moment. We're just giving your song an environmental spin!"}</p>
        </div>
    )
}