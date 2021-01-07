const express = require('express');

const router = express.Router();

router.get('/', function (req, res) {
    let flag = req.isAuthenticated();
    let name = req.user;

    res.render('main.ejs', {isLoggedin : flag, username : name});
});

module.exports = router;