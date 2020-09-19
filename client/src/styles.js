import { Button, IconButton, TextField } from "@material-ui/core"
import { withStyles } from '@material-ui/core/styles';

export const StyledButton = withStyles({
    root: {
      '&:disabled': {
        backgroundColor: "#333",
        color: '#aaa'
      },
    },
  })(Button);

  export const StyledIconButton = withStyles({
    root: {
      marginTop: "50px",
      backgroundColor: "#aaa",
      '&:disabled': {
        backgroundColor: "#333",
        color: '#aaa'
      },
      '&:hover': {
        backgroundColor: "#999"
      }
    },
  })(IconButton);

  export const AnotherSongButton = withStyles({
    root: {
      marginTop: "-8vh",
      marginLeft: "50px",
      backgroundColor: "#aaa",
      '&:disabled': {
        backgroundColor: "#333",
        color: '#aaa'
      },
    },
  })(Button);
  
export const CssTextField = withStyles({
    root: {
      fontColor: 'white',
      '& label.Mui-focused': {
        color: 'white',
      },
      '& .MuiInputLabel-root': {
        color: '#aaa',
      },
      '& .MuiInput-underline:after': {
        borderBottomColor: '#666',
      },
      '& .MuiOutlinedInput-input' : {
        color: 'white'
      },
      '& .MuiOutlinedInput-root': {
        '& fieldset': {
          borderColor: '#666',
        },
        '&:hover fieldset': {
          borderColor: '#aaa',
        },
        '&.Mui-focused fieldset': {
          borderColor: 'white',
        },
      },
    },
  })(TextField);