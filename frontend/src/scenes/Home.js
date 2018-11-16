import React, { Component } from 'react';

export default class Home extends Component {
    constructor() {
        super();
        this.state = {
            text: ""
        }
    }

    render() {
        return (
            <div className="App">
                <h1>{this.props.title}</h1>
                <textarea value={this.state.text} onChange={e => this.setState({text: e.target.value})}/>
                <button onClick={() => this.props.app.text = this.state.text}>Submit</button>
            </div>
        );
    }
}


