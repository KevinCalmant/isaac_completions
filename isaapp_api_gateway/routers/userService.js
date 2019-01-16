/**
 * userService.js 
 *   - Route that represent isaapp_api_user endpoints
 */
var express = require('express');
var router = express.Router();

const apiAdapter = require('./apiAdapter');

const BASE_URL = "http://localhost:5000";
const api = apiAdapter(BASE_URL);

router.post('/api/register', (req, res) => {
    api.post(req.path, req.body).then(resp => {
        res.send(resp.data);
    })
})

router.post('/api/login', (req, res) => {
    api.post(req.path, req.body).then(resp => {
        res.send(resp.data);
    })
})

router.get('/api/users', (req, res) => {
    api.get(req.path, {'headers' : req.headers}).then(resp => {
        res.send(resp.data);
    })
})

module.exports = router;

