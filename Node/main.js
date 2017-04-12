'use strict';

var express = require('express'); 
var app = express();
var http = require('http').Server(app);

/* Run our server */

http.listen(3000, function() {
	console.log("Running Jungle on port 3000...");
});