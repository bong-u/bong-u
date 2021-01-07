const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const passport = require('passport');
const flash = require('connect-flash');

const app = express();

const router = require('./router/index');

app.set('view engine', 'ejs');

app.listen(8888, function() {
    console.log("running on port 8888");
});

app.use(session({
    secret : 'bongsessionsecret',
    resave : false,
    saveUninitialized : true
}));

app.use(bodyParser.urlencoded({extended : true}));
app.use(bodyParser.json());
app.use(passport.initialize());
app.use(passport.session());
app.use(flash());

app.use(router);