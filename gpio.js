module.exports = function(RED) {
    function LowerCaseNode(config) {
        RED.nodes.createNode(this,config);
        this.pin = config.pin;
        var node = this;

        node.on('input', function(msg) {
            msg.payload = this.pin;
            node.send(msg);
        });
    }
    RED.nodes.registerType("GPIO",LowerCaseNode);
}