// src/App.js
import React, { useState } from 'react';
import Greeting from './Components/greetings';

function App() {
  const [name, setName] = useState('');
  const [submittedName, setSubmittedName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmittedName(name);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>React Basics Tutorial</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <button type="submit">Greet Me</button>
      </form>

      {submittedName && <Greeting name={submittedName} />}
    </div>
  );
}

export default App;
