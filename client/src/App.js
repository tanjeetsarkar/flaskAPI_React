import { useState } from 'react';
import './App.css';
import InputArea from './components/InputArea/InputArea';


function App() {

  const [output, setOutput] = useState("")

  function addTopic (topic_name) {
    fetch("/info", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "topic_name": topic_name.topicName,
      }),
    })
    .then((res) => res.json())
    .then((result) => setOutput(result))
    .catch((err) => console.log('error'))

    console.log(output)
  }



  return (
    <div >
      <InputArea onAdd={addTopic}/>
      {output && 
      <div className='displayArea'> 
        <h1>{output.topic.toUpperCase()}</h1>
        <p>{output.details}</p>
      </div> }
    </div>
  );
}

export default App;
