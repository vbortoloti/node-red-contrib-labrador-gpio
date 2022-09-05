//npm install python-shell
module.exports = function(RED) {
    function GpioOut(config) {
        RED.nodes.createNode(this,config);
        this.pin = config.pin;
        var node = this;
        var testCommand = __dirname+'/testgpio.py 3'
        var spawn = require("child_process").spawn;

        
        console.log('python '+ testCommand)

        
        node.on('input', function(msg) {
            msg.payload = this.pin;
            console.log("teste");

            node.child = spawn('python',["./testprint.py",2,2]);
            console.log("tryen");

            let output;
            node.child.stdout.on("data", (data) => {
                output += data;
            });

            console.log(output);
            

            // exec('python '+ testCommand, (err, stdout, stderr) => {

            //     if (err) {
            //         // node couldn't execute the command
            //         return;
            //     }
                
            //     // the *entire* stdout and stderr (buffered)
            //     console.log(`stdout: ${stdout}`);
            //     console.log(`stderr: ${stderr}`);
            // });
            
            node.send(msg);
        });
    }
    RED.nodes.registerType("gpio-out",GpioOut);
}