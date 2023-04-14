import React from 'react'
import {Link} from 'react-router-dom'

function ListItem({note}) {
  return (
    <Link to={`/${note.id}`}>{note.title}</Link>
  )
}

export default ListItem