
const express = require('express');

const app = express();

app.use(express.static('lost_and_found_pets_project'));

app.get('/action', function (req, res) {
    res.send(req.query.nume + ' vrea sa ' + req.query.actiune + ' are numarul de telefon ' + req.query.numar);
})

app.listen(5555, function() {
    console.log("Server is listening on port 5555...");
});
