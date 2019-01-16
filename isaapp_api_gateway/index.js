/**
 * index.js
 *   - Entry point for the gateway 
 */
var bodyParser = require('body-parser');
var express = require('express');
var app = express();
var router = require('./routers/router');

// We need bodyParser to enable us to parse POST datas
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.send("Simple API Gateway");
});

app.use(router);

console.log("ISAAPP API Gateway running on : localhost:3000");

app.listen(3000);

