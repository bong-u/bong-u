const express = require('express');
const mysql = require('mysql');

const router = express.Router();

router.get('/', function(req, res) {
    req.session.destroy();
    res.redirect('/');
});
module.exports = router;