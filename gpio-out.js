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
        node.child = spawn(gpioCommand, this.pin);
        console.log("Spawning child process");

        function check_input(msg){
            if (msg.payload === "true" || msg.payload === 1) { msg.payload = true; out = 1;}
            if (msg.payload === "false" || msg.payload === 0) { msg.payload = false; out = 0;}
            return msg;
        }

        function inputlistener(msg, send, done) {
            var out;
            if(msg.payload === "true"){ msg.payload = true;out =1}
            if(msg.payload === "false"){ msg.payload = false;out =0}

            msg.payload = check_input(msg.payload);
            console.log(this.pin);
            console.log(this.iotype);
            console.log(this.freq);
            console.log(this.initstate);
            console.log(this.set);

            /* -- Infinite Loop -- */
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