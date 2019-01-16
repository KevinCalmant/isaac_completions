var express = require('express')
var router = express.router

router.get('/register/', (req, res) => {
    res.send(req.path + " called")
})

router.get('/login/', (req, res) => {
    res.send(req.path + " called")
})

