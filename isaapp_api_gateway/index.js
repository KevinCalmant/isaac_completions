var bodyParser = require('body-parser')
var express = require('express')
var router = require('./routers/router')

var app = express()

// We need bodyParser to enable us to parse POST datas
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

console.log("ISAAPP API Gateway running on : localhost:3000")

app.listen(3000)

