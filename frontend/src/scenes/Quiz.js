import React, { Component } from 'react';
import axios from 'axios';

export default class Quiz extends Component {
    constructor() {
        super();
        this.state = {
            array: [],
            showAnswers: false,
            finished: false
        }
    }
    componentDidMount() {
        axios.get(`http://localhost:5000/get`)
            .then(res => {
                this.setState({
                    array: res.data,
                    answers: res.data.map(obj => null),
                    results: res.data.map(obj => false),
                });
            });
    }

    addToArray(val, index) {
        var copy = this.state.answers;
        copy[index] = val;
        this.setState({
            answers: copy
        });
        this.submitAnswers();
    }

    submitAnswers() {
        this.setState({
            results: this.state.array.map((obj, i) => obj.answer === this.state.answers[i])
        })
    }

    render() {
        return (
            <div className="App">
                <div className="Quiz">
                    <table>
                        <tr>
                            <th>Question</th>
                            <th>Result</th>
                            {this.state.showAnswers && <th>Answer</th>}
                        </tr>
                    {this.state.array.map((obj, i) => {
                        console.log(obj);
                        var split = obj.question.split("_____");
                        console.log(split);
                        return <tr>
                            <td>
                                <label>{split[0]}</label>
                                <textarea onChange={e => this.addToArray(e.target.value, i)} style={{resize: 'none', width:"50px", height:"15px"}}/>
                                <label>{split[1]}</label>
                            </td>
                                <td>{this.state.results[i] ? "Correct" : ""}</td>
                                {this.state.showAnswers && <td>{obj.answer}</td>}
                        </tr>
                    })}
                    </table>
                    <br/>
                    <button style={{width: '100%'}} onClick={() => this.setState({showAnswers: !this.state.showAnswers})}>{this.state.showAnswers ? "Hide answers" : "Show answers"}</button>


                </div>
            </div>
        );
    }
}