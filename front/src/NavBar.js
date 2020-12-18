import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import LocalCafeIcon from '@material-ui/icons/LocalCafe';
import jelly from './jelly.png';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    menuButton: {
        color: "white",
    },
    title: {
        color: "white",
    },
    imgContainer: {
        marginTop: 4,
        marginLeft: "auto", 
    },
    img: {
        height: 60,

    }
}));

export default function ButtonAppBar() {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            <AppBar position="static">
                <Toolbar>
                    <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
                        <LocalCafeIcon />
                    </IconButton>
                    <Button
                        className={classes.title}
                    >
                        Convertir la vidéo
                    </Button>
                    <div className={classes.imgContainer}>
                        <img className={classes.img} src={jelly} alt="Jellysmack" />
                    </div>
                </Toolbar>
            </AppBar>
        </div>
    );
}