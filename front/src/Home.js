import './App.css';
import React, { Component } from 'react';
import TextField from './Textfield';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import cup from './cup.png';

const useStyles = makeStyles((theme) => ({
    formStyle: {
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
        fontSize: 60,
        color: "white",
        paddingRight: 100,
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
        maxHeight: 400,
    }
}));

export default function Home() {
    const classes = useStyles();


    return (
        <form className={classes.formStyle}>
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


