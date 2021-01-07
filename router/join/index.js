const express = require('express');
const mysql = require('mysql');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const bcrypt = require('bcrypt');

const router = express.Router();

const connection = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : '1379',
    database : 'mydb'
});

router.get('/', function(req, res) {
    let msg = '';

    let errMsg = req.flash('error');
    
    if (errMsg) msg = errMsg;

    res.render('join.ejs', {'msg' : msg});
});

router.post('/', passport.authenticate('local-join', {
    successRedirect : '/',
    failureRedirect : '/join',
    failureFlash : true
}));

const HashPw = function (pw) {
    return new Promise(resolve => {
        bcrypt.genSalt(10, function(err, salt) {
            if (err)
                return done(err);
            bcrypt.hash(pw, salt, function(err, hash) {
                if (err)
                    return done(err);
                resolve(hash);
            });
        });
    });
};

passport.use('local-join', new LocalStrategy({
    usernameField: 'id',
    passwordField: 'pw',
    passReqToCallback: true
}, async function (req, id, pw, done) {
    let name = req.body.name;
    let sql = {id : id, pw : await HashPw(pw), name : name};

    connection.query('select * from user where id=?', [id], function (err, rows) {
        if (err)
            return done(err);
        if (rows.length)
            return done(null, false, {message : 'your id alreay used.'});

        connection.query('insert into user set ?', sql, function (err, rows) {
            if (err)
                return done(err);
    
            return done(null, {'id': id, 'name': name});
        });
    });
}));


passport.serializeUser(function (user, done) {
    console.log('passport session save : ', user.name);
    done (null, user.name);
});
passport.deserializeUser(function (name, done) {
    console.log('passport session get id : ', name);
    done (null, name);
});

module.exports = router;