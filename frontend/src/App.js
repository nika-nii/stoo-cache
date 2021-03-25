import './App.css';
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Review from './Review';
import Stats from './Stats'
import Header from './Header'
const App = () => {
  return (
    <BrowserRouter>
      <Header></Header>
      <Route exact path="/review" component={Review} />
      <Route exact path="/stat" component={Stats} />
    </BrowserRouter>
  );
}

export default App;
