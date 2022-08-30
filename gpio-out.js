//npm install python-shell
module.exports = function(RED) {
    function GpioOut(config) {
        RED.nodes.createNode(this,config);
        this.pin = config.pin;
        var node = this;
        const { exec } = require('child_process');
        var testCommand = __dirname+'/testprint.py'
        node.on('input', function(msg) {
            msg.payload = this.pin;
            console.log("teste");
            exec('python3 '+ testCommand /*+ ' pwm 32 up'*/, (err, stdout, stderr) => {
            if (err) {
                // node couldn't execute the command
                return;
            }
            
            // the *entire* stdout and stderr (buffered)
            console.log(`stdout: ${stdout}`);
            //console.log(`stderr: ${stderr}`);
            });
            node.send(msg);
        });
    }
    RED.nodes.registerType("gpio-out",GpioOut);
}