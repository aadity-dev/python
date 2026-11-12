
var http = require('http')

http.createServer(function(req, res){
    res.write("Welcome home!!")
    res.end()

}).listen(9000)