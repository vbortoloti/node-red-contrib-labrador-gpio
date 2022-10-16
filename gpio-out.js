//npm install python-shell
module.exports = function(RED) {

    function GpioOut(config) {
        RED.nodes.createNode(this,config);

        this.pin = config.pin;
        this.iotype = config.iotype;
        this.freq = config.freq;
        this.initstate = config.initstate;
        this.set = config.set;
        

        var node = this;
        var gpioCommand = __dirname+'/gpio-out.sh';
        var spawn = require("child_process").spawn;
        node.child = spawn(gpioCommand, [this.pin]);
        console.log("Spawning child process");
        var out = 0;
        function inputlistener(msg, send, done) {
            out = msg.payload;
            console.log(out);
            if (node.child !== null) {
                node.child.stdin.write(out+"\n", () => {
                    if (done) { done(); }
                });
            }else {
                console.log("erro")
            }
            node.send(msg);
        }
        node.on('input',inputlistener);
 
    }
    RED.nodes.registerType("gpio-out",GpioOut);
}