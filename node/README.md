var fs = require("fs");
 var http = require("http");
 var fs = require("fs");
 var ip = require("ip");
 


var project2_readfile = http.createServer(function(req, res){
  if (req.url === "/") {
    fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(body);
    })
}


else if(req.url.match("/sysinfo")){

  html=`
  <!DOCTYPE html>
      <htdml>
      <head>
          <title>System Information</title>
      </head>
      <body>
          
          <p>IP: ${ip.address()}</p>
          
          <h1>Project Two Craps: "Create Schedule and Display on the Browser using LOCALHOST:8080/sysinfo"</</h1>
          <p>Project Two Description: 
          This Project is a general introduction of Node.js.
          It basically helps us to display any information with the file system on our computer/s. 
          It is utilized mainly, for this project, to arrange the columns and rows of a table.
          Generally, HTML is used here to show how to create simple time table on the web-browser
          or server with the help of node.js. I have decided to use some code from the in-class
          lab as well as open source. Other aspects covered in this project are
          A) Read files, and
          B) Create files.
          Finally, it also functions as a file server.</p>
          <p>In this first part of the code, written above, the fs.readFile() method is utilized to read files 
          on my computer. The above code for Node.js file reads the HTML file that returns the given content.
          Thus, it completes the first purpose of the project as "Read Files".
          Finally, this time table has not been applied for any font usage in particular
          and no background colors are used to it. It's kept SIMPLE!</p>
          <h1>TIME TABLE</h1> 
    <table border="5" cellspacing="0" align="center"> 
        <!--<caption>Timetable</caption>-->
        <tr> 
            <td align="center" height="60" 
                width="100"><br> 
                <b>Day/Period</b></br> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>I<br>9:30-10:20</b> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>II<br>10:20-11:10</b> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>III<br>11:10-12:00</b> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>12:00-12:40</b> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>IV<br>12:40-1:30</b> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>V<br>1:30-2:20</b> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>VI<br>2:20-3:10</b> 
            </td> 
            <td align="center" height="60" 
                width="100"> 
                <b>VII<br>3:10-4:00</b> 
            </td> 
        </tr> 
        <tr> 
            <td align="center" height="60"> 
                <b>Monday</b></td> 
            <td align="center" height="60">NETWORKING</td> 
            <td align="center" height="60">EEP</td> 
            <td align="center" height="60">SCRIPTING</td> 
            <td rowspan="6" align="center" height="60"> 
                <h2>L<br>U<br>N<br>C<br>H</h2> 
            </td> 
            <td colspan="3" align="center" 
                height="60">LAB</td> 
            <td align="center" height="60">JAVA</td> 
        </tr> 
        <tr> 
            <td align="center" height="60"> 
                <b>Tuesday</b> 
            </td> 
            <td colspan="3" align="center" 
                height="60">LAB 
            </td> 
            <td align="center" height="60">NETWORKING</td> 
            <td align="center" height="60">SCRIPTING</td> 
            <td align="center" height="60">EEP</td> 
            <td align="center" height="60">MUSIC</td> 
        </tr> 
        <tr> 
            <td align="center" height="60"> 
                <b>Wednesday</b> 
            </td> 
            <td align="center" height="60">EEP</td> 
            <td align="center" height="60">JAVA</td> 
            <td align="center" height="60">NETWORKING</td> 
            <td align="center" height="60">SCRIPTING</td> 
            <td colspan="3" align="center" 
                height="60">LIBRARY 
            </td> 
        </tr> 
        <tr> 
            <td align="center" height="60"> 
                <b>Thursday</b> 
            </td> 
            <td align="center" height="50">JAVA</td> 
            <td align="center" height="50">NETWORKING</td> 
            <td align="center" height="50">SCRIPTING</td> 
            <td colspan="3" align="center" 
                height="60">LAB 
            </td> 
            <td align="center" height="60">EEP</td> 
        </tr> 
        <tr> 
            <td align="center" height="60"> 
                <b>Friday</b> 
            </td> 
            <td colspan="3" align="center" 
                height="60">LAB 
            </td> 
            <td align="center" height="60">EEP</td> 
            <td align="center" height="60">SCRIPTING</td> 
            <td align="center" height="60">NETWORKING</td> 
            <td align="center" height="60">JAVA</td> 
        </tr> 
        <tr> 
            <td align="center" height="60"> 
                <b>Saturday</b> 
            </td> 
            <td align="center" height="60">NETWORKING</td> 
            <td align="center" height="60">SCRIPTING</td> 
            <td align="center" height="60">EEP</td> 
            <td colspan="3" align="center" 
                height="60">PRESENTATION 
            </td> 
            <td align="center" height="60">MUSIC</td> 
        </tr> 
    </table> 
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
      
         
  
  
}).listen(8080);

console.log("Server listening on port 8080");

  
//*********************************************************** */
  //*********************************************************** */
