import './App.css';
import React, { Component } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import cup from './cup.png';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from "@material-ui/core/TextField";
import CloudUploadIcon from '@material-ui/icons/CloudUpload';

function goToStep2() {
    document.getElementById("page1").hidden = true;
    document.getElementById("page2").hidden = false;
    returnFlaskPost();
}

function selectFormat(format) {
    const formatsIds = ["instaCarreFormat", "instaVFormat", "instaHFormat", "instaStoryFormat", "tiktokFormat", "youtubeFormat", "fbHFormat", "fbCarreFormat"];

    formatsIds.forEach(id => {
        document.getElementById(id).style.border = "";
    })

    document.getElementById(format).style.border = "thick solid #3f51b5";
}

function uploadFile() {
    if (document.getElementById("upload").value != "") {
        const upload = document.getElementById("upload").value;
        console.log("ta maman");
        console.log(upload);
        if (upload != null) {
            document.getElementById("tf").value = upload;
        }
    }
}

function returnFlaskPost() {
    console.log(document.getElementById("tf").value);
    let tf = document.getElementById("tf").value;
    //return fetch('http://0.0.0.0:5000/api/v1', { headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, method: 'POST', body: { 'link': tf } });
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
        marginLeft: 10,
        marginRight: 10,
    },
    instagramVertical: {
        width: 120,
        height: 150,
        background: "white",
        marginLeft: 10,
        marginRight: 10,
    },
    instagramHorizontal: {
        width: 120,
        height: 73,
        background: "white",
        marginLeft: 10,
        marginRight: 10,
    },
    instagramStory: {
        width: 216,
        height: 394,
        background: "white",
        marginLeft: 10,
        marginRight: 10,
    },
    youtube: {
        width: 356,
        height: 144,
        background: "white",
        marginLeft: 10,
        marginRight: 10,
    },
    facebookCarre: {
        width: 64,
        height: 64,
        background: "white",
        marginLeft: 10,
        marginRight: 10,
    },
    formatContainer: {
        display: "flex",
    },
    selected: {
        background: "red"
    },
    tfStyle: {
        background: "white",
        width: "60%",
        marginTop: 10,
    },
}));



export default function Home() {
    const classes = useStyles();

    const [platform, setPlatform] = React.useState('instagram');
    let [tf, setTf] = React.useState('');

    const handleChange = (event) => {
        setPlatform(event.target.value);

        switch (event.target.value) {
            case "instagram":
                document.getElementById("insta").hidden = false;
                document.getElementById("tiktok").hidden = true;
                document.getElementById("youtube").hidden = true;
                document.getElementById("facebook").hidden = true;
                break;
            case "tiktok":
                document.getElementById("insta").hidden = true;
                document.getElementById("tiktok").hidden = false;
                document.getElementById("youtube").hidden = true;
                document.getElementById("facebook").hidden = true;
                break;
            case "youtube":
                document.getElementById("insta").hidden = true;
                document.getElementById("tiktok").hidden = true;
                document.getElementById("youtube").hidden = false;
                document.getElementById("facebook").hidden = true;
                break;
            case "facebook":
                document.getElementById("insta").hidden = true;
                document.getElementById("tiktok").hidden = true;
                document.getElementById("youtube").hidden = true;
                document.getElementById("facebook").hidden = false;
                break;
            default:
                document.getElementById("insta").hidden = false;
                document.getElementById("tiktok").hidden = true;
                document.getElementById("youtube").hidden = true;
                document.getElementById("facebook").hidden = true;
        }
    };

    const handleTfChange = (event) => {
        if (event.target.value !== "") {
            document.getElementById("convertBtnContainer").hidden = false;
        } else {
            document.getElementById("convertBtnContainer").hidden = true;
        }
    }

    return (
        <div>
            <div id="page1">
                <form className={classes.formStyle}>
                    <div className={classes.container}>
                        <h1 className={classes.title}>Convertissez votre vidéo</h1>
                        <img className={classes.image} src={cup} alt="Cup" />
                    </div>
                    <TextField
                        variant="filled"
                        id="urlTf"
                        label="Renseignez l'URL de la vidéo"
                        className={classes.tfStyle}
                        InputProps={{
                            className: classes.input
                        }}
                        onChange={handleTfChange}
                    />
                    <Button
                        variant="contained"
                        component="label"
                        color="primary"
                        className={classes.btnStyle}
                        onClick={(event) => { uploadFile() }}
                        startIcon={<CloudUploadIcon />}
                    >
                        Uploadez votre vidéo
                        <input
                            id="upload"
                            type="file"
                            accept=".mp4"
                            hidden
                        />
                    </Button>
                    <div id="convertBtnContainer" hidden>
                        <Button
                            id="convertBtn"
                            variant="contained"
                            className={classes.btnStyle}
                            color="primary"
                            onClick={(event) => { goToStep2() }}
                            hidden={true}
                        >
                            Convertir
                        </Button>
                    </div>
                </form>
            </div>
            <div id="page2" hidden>
                <form className={classes.formStyle}>
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
                        <div id="insta">
                            <div className={classes.formatContainer}>
                                <div id="instaCarreFormat" className={classes.instagramCarre} onClick={(event) => { selectFormat("instaCarreFormat") }}>600x600</div>
                                <div id="instaVFormat" className={classes.instagramVertical} onClick={(event) => { selectFormat("instaVFormat") }}>600x750</div>
                                <div id="instaHFormat" className={classes.instagramHorizontal} onClick={(event) => { selectFormat("instaHFormat") }}>600x315</div>
                                <div id="instaStoryFormat" className={classes.instagramStory} onClick={(event) => { selectFormat("instaStoryFormat") }}>1080x1920</div>
                            </div>
                        </div>
                        <div id="tiktok" hidden>
                            <div className={classes.formatContainer}>
                                <div id="tiktokFormat" className={classes.instagramStory} onClick={(event) => { selectFormat("tiktokFormat") }}>1080x1920</div>
                            </div>
                        </div>
                        <div id="youtube" hidden>
                            <div className={classes.formatContainer}>
                                <div id="youtubeFormat" className={classes.youtube} onClick={(event) => { selectFormat("youtubeFormat") }}>1280x720</div>
                            </div>
                        </div>
                        <div id="facebook" hidden>
                            <div className={classes.formatContainer}>
                                <div id="fbHFormat" className={classes.youtube} onClick={(event) => { selectFormat("fbHFormat") }}>1280x720</div>
                                <div id="fbCarreFormat" className={classes.facebookCarre} onClick={(event) => { selectFormat("fbCarreFormat") }}>640x640</div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    );
}


