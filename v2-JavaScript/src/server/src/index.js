const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();

app.use(bodyParser.json());

app.get('/', (request,response)=>{
    response.send('test');
});

app.post('/saveGame', (request, response) =>{
    //fs.appendFileSync('games.json', JSON.stringify(response.body));

    response.json({"success":"true"});
});


app.listen(3002, ()=>{
    console.log('Listening on port 3002');
})
