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
                <p>Here is the text from Home: {this.props.app.text}</p>
            
                <div className="Quiz">
                    <table>
                        <tr>
                            <th>Question</th>
                            <th>Answer</th>
                        </tr>
                    {this.state.array.map(obj => {
                        var split = obj.question.split("___");
                        return <tr>
                            <td><label>{split[0]}</label><textarea style={{resize: 'none', width:"50px", height:"15px"}}/><label>{split[1]}</label></td>
                            <td>{obj.answer}</td>
                        </tr>
                    })}
                    </table>
                </div>
            </div>
        );
    }
}