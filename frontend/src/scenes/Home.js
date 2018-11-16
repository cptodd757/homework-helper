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
                <textarea style={{width:"50vw", height:"40vh"}} value={this.state.text} onChange={e => this.setState({text: e.target.value})}/>
                <br/>
                <button onClick={() => this.props.app.text = this.state.text}>Submit</button>
            </div>
        );
    }
}


