var http = require('http');
var express = require('express')
var fs = require("fs");
var util = require('util');
var app = express();
var multer = require('multer');
var upload = multer({ dest: 'uploads/' })
//var bodyParser = ('body-parser');
//var dispatcher = require('httpdispatcher');


app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.get('/', function(req, res){
    var html = fs.readFileSync('index2.html');
    res.writeHead(200, {'Content-Type' : 'text/html'});
    res.end(html);
})

app.post('/submit' , upload.single( 'File' ), function(req, res) {

});

app.post('/submit', upload.single('file'), function(req,res,next) {
    fs.readFile(req.file.path, 'UTF-8', function(err,data){
        if(err){
            res.end(err);
        }
        res.end(data);
    });
});


<!DOCTYPE html>
<html>
  <body>
    <form action = "/submit" method = "post"></form>
        <form action="/submit" method="post" enctype="multipart/form-data"
        Select a file: <input type="file" name="file"></input>
        <input type="submit"></input>
    </form>
</body>
</html>


///Listening to Computer's IP address
app.listen(3000, "0.0.0.0");
console.log("Listening at 0.0.0.0:3000");

