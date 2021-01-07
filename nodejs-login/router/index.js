const express = require('express');
const main = require('./main');
const join = require('./join/index');
const login = require('./login/index');
const logout = require('./logout/index')

const router = express.Router();

router.use('/', main);
router.use('/join', join);
router.use('/login', login);
router.use('/logout', logout);

module.exports = router;