import './App.css';
import { useState, useRef } from 'react';
import axios from 'axios';

function App() {
  return (
    <>
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous"/>
        <link href="https://fonts.googleapis.com/css2?family=Jersey+20&display=swap" rel="stylesheet"/>
        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap" rel="stylesheet"/>
      </head>
      <body>
        <Header />
        <div className="row">
          <InputSection />
          <OutputSection />
        </div>
      </body>
    </>
  );
}

function Header() {
  return (
    <header className="header">
      <h1 id="title" className="header-text">
        course organization for u n me
      </h1>
    </header>
  );
}

function InputSection() {
  // State for storing selected files and response messages
  const [files, setFiles] = useState([]);
  const [responseMessage, setResponseMessage] = useState('');
  
  // Handle file input change
  const handleFileChange = (event) => {
    setFiles(event.target.files);
  };

  // Handle form submission (file upload)
  const handleSubmit = async () => {
    if (files.length === 0) {
      setResponseMessage("No files selected");
      return;
    }

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append('files', files[i]);
    }

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResponseMessage(response.data.message); // Message from the backend
    } catch (error) {
      setResponseMessage("Error uploading files.");
    }
  };

  return(
    <div id="column-left" className="column">
      <h1 className="header-text">
        1. upload syllabuses + schedules for all your classes!
      </h1>
      <div className="row">
        <div id="column-internal-left" className="column">
          {/* Pass necessary props to FileDropbox */}
          <FileDropbox 
            files={files} 
            handleFileChange={handleFileChange} 
          />
          {/* Pass handleSubmit as a prop to Submit */}
          <Submit handleSubmit={handleSubmit} />
        </div>
        <p>placeholder for file uploading ...</p>
      </div>
    </div>
  );
}

function FileDropbox({ files, handleFileChange }) {
  const uploadRef = useRef(null); // Used to change file upload value on click
  const clickHandler = () => {
    uploadRef.current.click();
  };

  return(
    <div className="dropbox" onClick={clickHandler}>
      <div className="dropbox-content">
        <svg id="upload-icon" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 99.09 122.88">
          <path d="M64.64,13,86.77,36.21H64.64V13ZM42.58,71.67a3.25,3.25,0,0,1-4.92-4.25l9.42-10.91a3.26,3.26,0,0,1,4.59-.33,5.14,5.14,0,0,1,.4.41l9.3,10.28a3.24,3.24,0,0,1-4.81,4.35L52.8,67.07V82.52a3.26,3.26,0,1,1-6.52,0V67.38l-3.7,4.29ZM24.22,85.42a3.26,3.26,0,1,1,6.52,0v7.46H68.36V85.42a3.26,3.26,0,1,1,6.51,0V96.14a3.26,3.26,0,0,1-3.26,3.26H27.48a3.26,3.26,0,0,1-3.26-3.26V85.42ZM99.08,39.19c.15-.57-1.18-2.07-2.68-3.56L63.8,1.36A3.63,3.63,0,0,0,61,0H6.62A6.62,6.62,0,0,0,0,6.62V116.26a6.62,6.62,0,0,0,6.62,6.62H92.46a6.62,6.62,0,0,0,6.62-6.62V39.19Zm-7.4,4.42v71.87H7.4V7.37H57.25V39.9A3.71,3.71,0,0,0,61,43.61Z"/>
        </svg>
        <p className="dropbox-text">Drag and drop or click to browse files</p>
        <p className="subtext">Supported file types: .pdf, .docx, .html</p>
        <input type="file" ref={uploadRef} onChange={handleFileChange} />
      </div>
    </div>
  );
}

function Submit({ handleSubmit }) {
  return (
    <button className="submit" onClick={handleSubmit}>Submit</button>
  );
}

function OutputSection() {
  return (
    <div className="column">
      <h1 className="header-text">
        2. get your organized schedule!
      </h1>
      <p>
        Your custom schedule features assignments and assessments across all courses organized by deadline so you won’t miss any :)
      </p>
      <p>
        Also featuring simplified grade calculation :)
      </p>
    </div>
  );
}

export default App;
