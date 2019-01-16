/**
 * router.js 
 *  - Centralized all the endpoints of the ISAAPP APIs  
 */
var express = require('express');
var router = express.Router();
var userService = require('./userService');

// Route processing 
router.use((req, res, next) => {
    console.log("Called: ", req.path);
    next();
})

router.use(userService);

module.exports = router;