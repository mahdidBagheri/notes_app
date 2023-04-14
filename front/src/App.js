import './App.css';
import { 
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom'

import Note from './pages/Note'
import Notes from './pages/Notes'
import Layout from './components/Layout';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path={'/'} element={<Notes/>} exact />
          <Route path={'/:id'} element={<Note/>} exact />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
