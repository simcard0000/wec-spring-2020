/** @format */

const express = require("express");
const app = express();

app.listen(3000, function () {
	console.log("server running on port 3000");
});

app.use(function (req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Content-Type,Authorization');
    res.header('Access-Control-Allow-Methods', 'GET,POST,PUT,PATCH,DELETE');
  });

app.get("/search", search);

function search(req, res) {
	console.debug(req);

	// Use child_process.spawn method from
	// child_process module and assign it
	// to variable spawn
	var spawn = require("child_process").spawn;

	// Parameters passed in spawn -
	// 1. type_of_script
	// 2. list containing Path of the script
	//    and arguments for the script

	// E.g : http://localhost:3000/search?query=Hello
	var process = spawn("python", ["../src/script.py", req.query.query]);

	// Takes stdout data from script which executed
	// with arguments and send this data to res object
	process.stdout.on("data", function (data) {
		res.send(data.toString());
	});
}

app.listen(8080);
