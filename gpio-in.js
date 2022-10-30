//npm install python-shell
module.exports = function(RED) {
    function GpioIn(config) {
        RED.nodes.createNode(this,config);

        this.pin = config.pin;
        this.read = config.read || false;
        

        var node = this;
        var gpioCommand = __dirname+'/gpio-in.sh';
        var spawn = require("child_process").spawn;
        //FIX ME
        //node.child = spawn(gpioCommand, [this.pin, out, 100, 0, false]);
        var out = 0;

        var startPin = function() {
            node.child = spawn(gpioCommand,[this.pin]);
            console.log("Spawning child process");

            node.child.stdout.on('data', function (data) {
                var d = data.toString().trim().split("\n");
                for (var i = 0; i < d.length; i++) {
                    if (d[i] === '') { return; }
                    else{node.send({ topic:"gpio/"+node.pin, payload:Number(d[i]) });}
                }
            });

            node.child.on('close', function (code) {
                node.child.removeAllListeners();
                delete node.child;
                if (!node.finished && code === 1) {
                    setTimeout(function() {startPin()}, 250);
                }
                else if (node.finished) {
                    node.finished();
                }
            });
        }
        startPin();
        
        node.on("close", function(done) {
            if (node.child != null) {
                node.finished = done;
                node.child.stdin.write("close "+node.pin, () => {
                    if (node.child) {
                        node.child.kill('SIGKILL');
                    }
                });
            }
            else { if (done) { done(); } }
        });
 
    }
    RED.nodes.registerType("gpio-in",GpioIn);
}
