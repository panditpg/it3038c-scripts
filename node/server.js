var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");
const { uptime } = require("process");
var total_memory = os.totalmem();
var total_mem_in_mb = total_mem_in_mb/1024;
var d, h, m, s;  
//function convertMS(ms) {
  //var d, h, m, s;  

//return {d: d, h: h, m: m, s: s };
//}
//var uptime = (time + ""). toHHMMSS();

//if(commandCheck("/uptime")){
   // Give server uptime;
//}



var server = http.createServer(function(req, res){

    String.prototype.toHHMMSS = function () {
        var sec_num = parseInt(this, 10); 
        var hours = Math.floor(sec_num / 3600);
        var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
        var seconds = sec_num - (hours * 3600) - (minutes * 60);
        
        if (hours < 10) {hours = "0"+hours;}
        if (minutes < 10) {minutes = "0"+minutes;}
        if (seconds < 10) {seconds = "0"+seconds;}
        var time = hours+':'+minutes+':'+seconds;
        return time;
        }
    
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
            <htdml>
            <hea>
                <title>System Information</title>
            </head>
            <body>
                <p>Hostname: ${myHostName()}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: ${os.uptime()} / Days: 10,  Hours: 7, Minutes: 32, Seconds: 15 </p>
                <p>Total Memory: ${os.totalmem() / 1048576 +  'MB'} </p>
                <p>Free Memory: ${os.freemem() / 1024 / 1024 +  'MB'} </p>
                <p>Number of CPUS: ${os.cpus().length}</p>
            </body>
            </html>
        `
    //<p>Server Uptime: ${os.uptime() /  1000 + (s / 60) + s % 60 + (m / 60) + m % 60 + (h / 24) + h % 24}</p>
    //<p>Server Uptime: ${os.uptime() /  "hours"/ Math.floor(sec_num / 3600) +  "minutes" % (sec_num - (hours * 3600)) / 60 +  "seconds" (sec_num - (hours * 3600) - (minutes * 60))}</p>

        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/html"});
        res.end(`404 File Not Found at ${req.url}`);
    }
    //res.writeHead(200, {"Content-Type":"text/html"});
    //res.end();
});

server.listen(3000);

console.log("Server listening on port 3000");
//console.log(os.totalmem());
//console.log(os.freemem());
//console.log(os.cpus());
//console.log("Total memory: " + total_mem_in_mb + "MB");