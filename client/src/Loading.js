import React from "react"
import './Loading.css'
import './App.css'

export const Loading = ({setLoading, setPlaySong}) => {
    return (
        <div className="App-box">
            <div className="loader"/>
            <p>Wait a moment. We're just giving your song an environmental spin!</p>
        </div>
    )
}