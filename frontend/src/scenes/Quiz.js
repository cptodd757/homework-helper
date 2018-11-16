import React, { Component } from 'react';

export default class Quiz extends Component {
    render() {
        return (
            <div className="App">
            
                <div className="Quiz">
                    <p>Here is the text from Home: {this.props.app.text}</p>
                    {this.props.app.array.map(obj => (
                        <div>
                            <h5>{obj.question} {obj.answer}</h5>
                        </div>
                    ))}
                </div>
            </div>
        );
    }
}