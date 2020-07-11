/** @format */

const express = require("express");
const app = express();

app.get("/hey", (req, res) => res.send("it is what it is!"));

app.listen(8080);
