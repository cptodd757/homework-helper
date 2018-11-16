import React, { Component } from 'react';

export default class Quiz extends Component {
    render() {
        return (
            <div className="App">
                <p>This is the quiz</p>
                <p>Here is the text from Home: {this.props.app.text}</p>
            </div>
        );
    }
}