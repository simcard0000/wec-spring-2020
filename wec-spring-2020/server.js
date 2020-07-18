/** @format */

const express = require("express");
const app = express();

app.listen(3000, function () {
	console.log("server running on port 3000");
});

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

app.get("/search", search);

function search(req, res) {
	console.debug(req);
	var spawn = require("child_process").spawn;

	// e.g : http://localhost:3000/search?query=Hello
	var process = spawn("python", ["../src/script.py", req.query.query]);

	// Takes stdout data from script which executed
	// with arguments and send this data to res object
	process.stdout.on("data", function (data) {
        process.stdout.write(data);
        res.send(data.toString());
    }).on('error', (e) => { // catches ECONNRESET errors
        console.error(e);
    });
}

app.listen(8080);
