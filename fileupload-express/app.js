const express = require('express')
const app = express()
const port = 3000

const spawn = require("child_process").spawn;

const multer = require('multer')
const fs = require('fs')
const url = require('url')
const storage =   multer.diskStorage({
  destination: function (req, file, callback) {
    callback(null, './uploads');
  },
  filename: function (req, file, callback) {
    callback(null, file.fieldname + '-' + Date.now());
  }
});

const upload = multer({ storage : storage}).single('userPhoto');

app.get('/', (req, res) => res.sendFile(__dirname+"/index.html"))

app.post('/api/photo',function(req,res){
    upload(req,res,function(err) {
        if(err) {
            return res.end("Error uploading file.");
        }
        
        try {
          var filename = req.file.filename
        }
        catch (e) {
          console.log(e);
          res.end('No file was attached. Go back because I dont have that error handling figured out yet...')
        }
        finally {
          console.log("entering and leaving the finally block");
        }       


        console.log('attempting to get file name of empty file')
        //store the request upload file name

        console.log('attempting to get file name of empty file')

        //spawn a python process to manipulate the user submitted image and listen for a response
        const pythonProcess = spawn('python',["manipulate-userPhoto.py", filename])
		pythonProcess.stdout.on('data', (data) => {
            
            //do something with the python response data, in the is case, we are returning a modified version of the user submited image
    	    fs.readFile(data.toString().replace(/(\r\n|\n|\r)/gm, ""), function (err, content) {
    	        if (err) {
    	            res.writeHead(400, {'Content-type':'text/html'})
    	            console.log(err);
    	            res.end("There was an error processing your image :(");    
    	        } else {
    	            //specify the content type in the response will be an image
    	            res.writeHead(200,{'Content-type':'image/jpg'});
    	            res.end(content);
    	        }
    	    })

        }); //close pythonProcess


    }); //close upload

}); //close post


app.listen(port, () => console.log(`Example app listening on port ${port}!`))