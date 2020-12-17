import './App.css';
import React, { Component } from 'react';
import TextField from './Textfield';
import { makeStyles } from '@material-ui/core/styles';
//import TextField from "@material-ui/core/TextField";
import Button from '@material-ui/core/Button';
import cup from './cup.png';


//const API = 'https://us-central1-callert-b38f5.cloudfunctions.net/webApi/api/v1/users/';
const COLOR = '#ff8fd9';

const useStyles = makeStyles((theme) => ({
    profileContainerStyle: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: 5,
    },
    btnStyle: {
        marginTop: 40,
        color: "white",
    },
    title: {
        fontSize: "60px",
        color: "white",
        margin: "20px",
        paddingRight: "100px",
    },
    container: {
        width: "60%",
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        marginTop: 40,
        marginBottom: 40,
    },
    image: {
        width: "50%",
    }
}));

export default function Home() {
    const classes = useStyles();


    return (
        <form className={classes.profileContainerStyle}>
            <div className={classes.container}>
                <h1 className={classes.title}>Convertissez votre vidéo</h1>
                <img className={classes.image} src={cup} alt="Cup" />
            </div>
            <TextField />
            <Button
                variant="contained"
                component="label"
                color="primary"
                className={classes.btnStyle}
            >
                Uploadez votre vidéo
                <input
                    type="file"
                    hidden
                />
            </Button>
            <Button
                type="submit"
                variant="contained"
                className={classes.btnStyle}
                color="primary"
            >
                Convertir
        </Button>
        </form>
    );
}


