const express = require("express");
const app = express();
const PORT = 8080;

app.get('/', (req, res) => {
  res.json('Hello, user!');
})

app.get('/greeting/:name', (req, res) => {
  res.json(`Hello, ${req.params.name}!`);
});


app.listen(PORT, () => {
  console.log('Server listening on port '+PORT)
});