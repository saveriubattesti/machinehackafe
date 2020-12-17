import './App.css';
import React, { Component } from 'react';
import TextField from './Textfield';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import cup from './cup.png';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import InputLabel from '@material-ui/core/InputLabel';

function goToStep2() {
    document.getElementById("page1").hidden = true;
    document.getElementById("page2").hidden = false;
}

const useStyles = makeStyles((theme) => ({
    formControl: {
        margin: theme.spacing(1),
        width: 120,
        background: "#3f51b5",
        marginLeft: "40%",
      },
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
        maxWidth: 337.5,
    },
    preview: {
        marginTop: 40,
        marginBottom: 40,
        background: "red",
        width: "50%",
        height: 300,
    },
    formatsContainer: {
        marginTop: 40,
    },
    platformSelect: {
        color: "white",
        paddingLeft: 16,
    },
    instagramCarre: {
        width: 120,
        height: 120,
        background: "white",
    }
}));

export default function Home() {
    const classes = useStyles();

    const [platform, setPlatform] = React.useState('instagram');

    const handleChange = (event) => {
        setPlatform(event.target.value);
    };

    return (
        <div>
            <div id="page1">
                <form  className={classes.formStyle}>
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
                        variant="contained"
                        className={classes.btnStyle}
                        color="primary"
                        onClick={(event) => {goToStep2()}}
                    >
                        Convertir
                    </Button>
                </form>
            </div>
            <div id="page2" hidden>
                <form  className={classes.formStyle}>
                    <div className={classes.preview}>
                        <h1>Preview</h1>
                    </div>
                    <FormControl className={classes.formControl}>
                        <Select
                            id="platform-select"
                            value={platform}
                            onChange={handleChange}
                            color="primary"
                            className={classes.platformSelect}
                            defaultValue={platform}
                        >
                            <MenuItem value="instagram">Instagram</MenuItem>
                            <MenuItem value="tiktok">TikTok</MenuItem>
                            <MenuItem value="youtube">YouTube</MenuItem>
                            <MenuItem value="facebook">Facebook</MenuItem>
                        </Select>
                    </FormControl>
                    <div className={classes.formatsContainer}>
                        <div className={classes.instagramFormats}>
                            <div className={classes.instagramCarre}>600x600</div>
                            <div className={classes.instagramVertical}>600x750</div>
                            <div className={classes.instagramHorizontal}>600x600</div>
                            <div className={classes.instagramStory}>600x600</div>
                        </div>
                    </div>
                    
                </form>
            </div>
        </div>
    );
}


