import React, {useState} from 'react';
import './App.css';
import { Search } from './Search';


function App() {
  const [value, setValue] = useState('')
  return (
    <div className="App">
      <header className="App-header">
        <Search value={value} setValue={setValue}/>
      </header>
    </div>
  );
}

export default App;


