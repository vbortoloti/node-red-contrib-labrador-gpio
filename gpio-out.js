module.exports = function(RED) {
    function GpioOut(config) {
        RED.nodes.createNode(this,config);
        this.pin = config.pin;
        var node = this;

        var execSync = require('child_process').execSync;
        var exec = require('child_process').exec;
        var spawn = require('child_process').spawn;

        var gpioCommand  = __dirname+'/testgpio.py';
        
        function inputlistener(msg, send, done) {
            if (msg.payload === "true") { msg.payload = true; }
            if (msg.payload === "false") { msg.payload = false; }

            node.child.stdin.write(out+"\n", () => {
                if (done) { done(); }
            });
        }

        node.on('input', function(msg) {
            msg.payload = this.pin;
            node.child = spawn(gpioCommand, ["pwm",52,"up"]);
            node.on("input", inputlistener);
            node.send(msg);
        });
    }
    RED.nodes.registerType("gpio-out",GpioOut);
}