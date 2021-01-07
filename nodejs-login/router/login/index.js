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

    res.render('login.ejs', {'msg' : msg});
});

router.post('/', passport.authenticate('local-login', {
    successRedirect : '/',
    failureRedirect : '/login',
    failureFlash : true
}));

passport.use('local-login', new LocalStrategy({
    usernameField: 'id',
    passwordField: 'pw',
    passReqToCallback: true
}, function (req, id, pw, done) {

    if (!(id && pw)) 
        return done(null, false, {message : 'please enter id and password!'});
    else {
        connection.query('select * from user where id=?', [id], function (err, rows) {
            if (!bcrypt.compareSync(pw, rows[0].pw))
                return done(null, false, {message : 'incorrect id or password!'});
            else
                return done(null, {'id' : id, 'name' : rows[0].name});
        });
    }
    
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