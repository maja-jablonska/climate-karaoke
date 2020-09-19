import React from 'react';
import { CssTextField, StyledButton } from './styles';
import logo from './karaoke_logo.png';
import { Autocomplete } from '@material-ui/lab';


export const Search = ({value, setValue, fetchLyrics, error, errorMessage}) => {
    return(
        <>
    <img src={logo} className="App-logo" alt="logo" />
        <div className="App-box">
          {error && <div className="App-error">{errorMessage}</div>}
        <Autocomplete
        freeSolo
        id="free-solo-2-demo"
        disableClearable
        options={top100Films.map((option) => option.title)}
        inputValue={value}
        onInputChange={(event, newValue) => {
          setValue(newValue);
        }}
        renderInput={(params) => (
          <CssTextField
            {...params}
            label="Type name of a song"
            margin="normal"
            variant="outlined"
            InputProps={{ ...params.InputProps, type: 'search' }}
          />
        )}
      />
      <StyledButton variant="contained" disabled={value.length === 0} onClick={fetchLyrics}>Sing!</StyledButton>
      </div>
      </>
    )
}

const top100Films = [];