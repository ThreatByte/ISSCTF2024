import React, { useState, useEffect } from 'react';
import './App.css';
import { API } from './Api.js'

function App() {
  const currentUrl = window.location.href;
  const urlObject = new URL(currentUrl);
  const modifiedUrl = urlObject.href;
  const baseUrl = modifiedUrl;
  const api = API(baseUrl);
  api.ping()
  const [audio] = useState(new Audio('/dark.mp3'));
  let hasPlayed = false

  const playAudio = () => {
    if(hasPlayed === false) {
        audio.play()
          .catch(() => {});
        hasPlayed = true
    }
  };

  const handleMouseMove = () => {
    playAudio();
  };

  useEffect(() => {
    document.addEventListener('mousemove', handleMouseMove);
  }, []);

  return (
    <div className="App">
      <div className="glow terminal">
        <p className="mute">= = = = WELCOME TO = = = =</p>
        <h1>The <span className="name">Gibson</span> <span className="cursor"></span></h1>

        <p className="mute">= = = = =  LOG  = = = = =</p>
        <div className="left">
          <span style={{color: 'black', backgroundColor: 'orange', padding: '2px' }}>[INFO]</span> >> Initiating Connection to gibson@localhost<br></br>
          This may take a moment...<br></br><br></br>
          <span style={{color: 'black', backgroundColor: 'green', padding: '2px' }}>[SUCCESS]</span> >> Connected to Gibson Mainframe Access Point...<br></br>
          Fetching latest entry<br></br><br></br>

          <div className="email">
            <h4>Urgent: System Security Update - Protecting the Gibson</h4>
            <h4>To: All Employees</h4><br></br>
            Hello valued Employee #???,

            <p style={{marginLeft: '10px'}}>
              I hope this message finds you well. As we continue to navigate the digital landscape,
              it is imperative that we prioritize the security of our systems and data.
              Over the past few weeks, our cybersecurity team has detected a series of
              unprecedented cyber threats targeting the Gibson.<br></br><br></br>
            </p>

            <p style={{marginLeft: '10px'}}>
              In response to these emerging challenges, we are implementing a comprehensive security
              update to fortify our defenses and ensure the integrity of our network. This requires
              rebuildng of our infrastructure. Please expect downtime while we work on rebuilding
              systems from the ground up.<br></br><br></br>
            </p>

            Hack the planet.<br></br>
            - Ellingson Mineral Company
          </div>
        </div>
        <br></br>
        
        <p className="mute">= = = = =  END  = = = = =</p>
        <div className="left">
          <span style={{color: 'black', backgroundColor: 'red', padding: '2px' }}>[BYE]</span> >> Closing connection...<br></br>
          Connection terminated. Session has ended.
        </div>
      </div>
    </div>
  );
}

export default App;
