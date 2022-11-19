//npm install python-shell
module.exports = function(RED) {
    function GpioOut(config) {
        RED.nodes.createNode(this,config);

        this.pin = config.pin;
        this.iotype = config.iotype || "out";
        this.freq = config.freq || 0;
        this.duty = config.duty || 0;
        this.initstate = config.initstate.toString() || 0;
        this.set = config.set || false;
        

        var node = this;
        var gpioCommand = __dirname+'/gpio-out.sh';
        var spawn = require("child_process").spawn;
        //FIX ME
        //node.child = spawn(gpioCommand, [this.pin, out, 100, 0, false]);
        node.child = spawn(gpioCommand,[this.pin,this.iotype,this.freq,this.duty]);

        console.log("Spawning child process");
        var out = 0;
        var lastInputSent;

        this.status({fill:"green",shape:"dot",text:"connected"});


        function inputlistener(msg, send, done) {
            if(this.status.text=="sending")
                return;
            this.status({fill:"red",shape:"ring",text:"sending"});
            if(msg.payload == "true" || msg.payload == "1"){
                out = 1;
            }else if(msg.payload == "false" || msg.payload == "0"){
                out = 0;
            }
            //console.log(this.pin+" "+this.iotype+" "+this.freq +" "+this.duty + " " + this.initstate+" "+this.set);
            if(lastInputSent == null || lastInputSent != out){
                lastInputSent = out;
                if (node.child !== null) {
                    node.child.stdin.write(out+"\n", () => {
                        setTimeout(function() { if (done) { done(); } },150);
                    });
                }else {
                    console.log("erro")
                }
            }
            node.send(msg);
            this.status({fill:"green",shape:"dot",text:"connected"});
        }

        node.on('input',inputlistener);

        node.child.on('close', function (code) {
            node.child.removeAllListeners();
            delete node.child;
            node.finished();
        });
        
        node.on("close", function(done) {
            if (node.child != null) {
                node.finished = done;
                node.child.stdin.write("close "+node.pin, () => {
                    node.child.kill('SIGKILL');
                    setTimeout(function() { if (done) { done(); } }, 50);
                });
            }
            else { if (done) { done(); } }
        });
 
    }
    RED.nodes.registerType("gpio-out",GpioOut);
}