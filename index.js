'use strict';

const MongoClient = require('mongodb').MongoClient;
const express = require('express');

// Constants
const PORT = 5000;

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello world\n');
});

app.listen(PORT);
console.log(`Running on Port:${PORT}`);