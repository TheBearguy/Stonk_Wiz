const express = require('express');
const mongoose = require('mongoose');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const bcrypt = require('bcrypt');
const session = require('express-session');
const app = express();

// Configure passport and session middleware here

// Define your routes for user registration, login, stock management, etc.
// Example:
// app.use('/api/users', require('./routes/userRoutes'));
// app.use('/api/stocks', require('./routes/stockRoutes'));

const PORT = process.env.PORT || 3000;



