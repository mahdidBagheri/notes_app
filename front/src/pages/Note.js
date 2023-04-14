import React, {useState, useEffect } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'

const Note = ({match}) => {
  let params = useParams()
  let navigate = useNavigate()
  let noteId = params.id

  let [note, setNote] = useState(null)

  useEffect(() => {
    if(noteId !== 'add') { getNote()}
  }, [noteId])

  let getNote = async () => {
    let response = await fetch(`http://127.0.0.1:8000/notes/${noteId}`)
    let data = await response.json()
    console.log(data)
    setNote(data)
  }

  let submitData = async () => {
    let url = `http://127.0.0.1:8000/notes/`
    let method = "POST"

    if(noteId !== 'add')
    {
      url = `http://127.0.0.1:8000/notes/${noteId}`
      method = "PUT"
    }

    await fetch(url, {
      method:method,
        headers:{
          'Content-Type':'application/json'
        }, body: JSON.stringify({"title":note.title, "body":note.body})
    })
    navigate('/')
  }

  return (
    <div>
      <Link to={`/`}> Go back </Link>
      {noteId !== `add` && (<button>delete</button>)}

      <textarea onChange={(e) => {setNote({...note,"body":e.target.value})}} value={note?.body} placeholder='enter note ...' ></textarea>
      <button onClick={submitData}> save </button>

    </div>
  )
}

export default Note