import React, { useState } from 'react'
import "./InputArea.css"

const InputArea = (props) => {

    const [topic, setTopic] = useState({
        topicName: ""
    })

    function handleChange(e) {
        const {name, value} = e.target
        setTopic({[name]: value})
    }

    function handleClick(e){
        e.preventDefault()
        props.onAdd(topic)
        setTopic({
            topicName: ""
        })
    }

  return (
    <div className='inputArea'>
        <input name="topicName" value={topic.topicName} onChange={handleChange} placeholder='Search here'/>
        <button onClick={handleClick}> Execute </button>
    </div>
  )
}

export default InputArea