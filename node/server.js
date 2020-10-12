var http = require("http");
var fs = require("fs");

var server = http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body)
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        })
    }
    //res.writeHead(200, {"Content-Type": "text/html"});
    //res.end(); 
});

server.listen(3000);

console.log("Server listening on port 3000");