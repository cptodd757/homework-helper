import React, { Component } from 'react';
import './App.css';
import Home from './scenes/Home';
import Quiz from './scenes/Quiz';


class App extends Component {
    constructor() {
        super();
        this.state = {
            showHome: true
        }
    }

  render() {

      return (
      <div className="App">
          {this.state.showHome ? <Home title={"I <3 Nico"}/> : <Quiz/>}
          <button onClick={() => this.setState({showHome: !this.state.showHome})}>{this.state.showHome ? "Show Quiz" : "Go Home"}</button>
      </div>
    );
  }
}

export default App;
