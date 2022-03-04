import React, { useState } from 'react'

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
    <div>
        <input name="topicName" value={topic.topicName} onChange={handleChange} placeholder='Search wiki here'/>
        <button onClick={handleClick}> Execute </button>
    </div>
  )
}

export default InputArea