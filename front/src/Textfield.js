import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";

const styles = {
  root: {
    background: "white",
  },
  input: {
    color: "black",
  }
};

const tfStyle = {
  width: "60%",
  marginTop: "10px",
};

function CustomizedInputs(props) {
  const { classes } = props;

  return (
    <TextField
      variant="standard"
      id="name"
      label="Renseigner l'URL de la vidéo"
      className={classes.root}
      InputProps={{
        className: classes.input
      }}
      style={tfStyle}
    />
  );
}

CustomizedInputs.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(CustomizedInputs);