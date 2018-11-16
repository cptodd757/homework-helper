import React, { Component } from 'react';
import axios from 'axios';

export default class Quiz extends Component {
    constructor() {
        super();
        this.state = {
            array: []
        }
    }
    componentDidMount() {
        axios.get(`http://localhost:5000/get`)
            .then(res => {
                this.setState({
                    array: res.data
                });
            });
    }

    render() {
        return (
            <div className="App">
            
                <div className="Quiz">
                    <p>Here is the text from Home: {this.props.app.text}</p>
                    {this.state.array.map(obj => (
                        <div>
                            <h5>{obj.question}</h5>
                            <p>{obj.answer}</p>
                        </div>
                    ))}
                </div>
            </div>
        );
    }
}