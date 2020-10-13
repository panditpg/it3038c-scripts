var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");
var total_memory = os.totalmem();
var total_mem_in_mb = total_mem_in_mb%1024;

var server = http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        })
    }
    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname();
        html=`
        <!DOCTYPE html>
            <html>
            <head>
                <title>System Information</title>
            </head>
            <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: </p>
                <p>Total Memory: ${os.totalmem() + "/MB"}</p>
                <p>Free Memory: ${os.freemem() + "/MB"}</p>
                <p>Number of CPUS: ${os.cpus()}</p>
            </body>
            </html>
        `
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/html"});
        res.end(`404 File Note Found at ${req.url}`);
    }
    //res.writeHead(200, {"Content-Type":"text/html"});
    //res.end();
});

server.listen(3000);

console.log("Server listening on port 3000");
//console.log("Total memory: " + total_mem_in_mb + "MB");