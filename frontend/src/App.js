import React, { useEffect, useState } from 'react';

function App() {
  const [notes, setNotes] = useState([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    fetch('/api/notes')
      .then(res => res.json())
      .then(setNotes);
  }, []);

  const addNote = () => {
    fetch('/api/notes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: input })
    }).then(res => res.json())
      .then(note => setNotes([...notes, note]));
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Notes</h1>
      <ul>
        {notes.map(note => <li key={note.id}>{note.content}</li>)}
      </ul>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={addNote}>Add</button>
    </div>
  );
}

export default App;
