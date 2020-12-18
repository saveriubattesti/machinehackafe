import React, { Component } from 'react';
import die from './die.jpg';

class Preview extends Component {
    constructor() {
        super();
        this.state = {
            img: null,
        };
    }

    /*componentDidMount() {
        console.log('app mounted');
   
        fetch('http://0.0.0.0:5000/test')
            .then(data => data.json())
            .then(data => this.setState({ img: data }, () => console.log(data)));
    }*/

    componentDidMount() {     // Simple POST request with a JSON body using fetch 
        console.log(this.state.url)
        const requestOptions = { 
            method: 'POST', 
            headers: { 'Content-Type': 'application/json' }, 
            body: JSON.stringify({ title: this.state.url }) };
            fetch('http://0.0.0.0:5000/api/setURL', requestOptions).then(response => response.json()).then(data => this.setState({ img: data }));
    }

    render() {
        const imgStyle = {
            width: "100%",
            maxHeight: 300,
            maxWidth: 573.5,
        };

        if (this.state.img === null) {
            return (
                <div>
                    <img style={imgStyle} src={die} alt="image"></img>
                </div>
            );
        }

        return (
            <div>
                <img style={imgStyle} src={this.state.img} alt="image"></img>
            </div>
        );
    }
}

export default Preview;
