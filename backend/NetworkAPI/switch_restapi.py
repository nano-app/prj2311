# TODOS ###
# 1. get --> get info from db of last time collect records
# 2. put --> ssh/rest to real switch to change sw config, update db records
# 3. should add some safety controls:
#     NEVER shutdown/change trunk ports (hardcode: excluding g1/0/23-24 ...)
#     DON'T change specific vlans..

# HOWTO ###
# Run >python3 -m flask run --port=8081
# GET >curl http://127.0.0.1:8081/ports/1
# PUT >curl -X PUT -H "Content-Type: application/json" -d '{"portName": "swport", "status": "UP","vlanID":"10"}' http://127.0.0.1:8081/ports/updatePort/1

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data to represent a network port, it is not db record
ports = [
    {"id": 1, "portName": "switch3-port1", "status": "UP", "vlanID": "1"},
    {"id": 2, "portName": "switch4-port2", "status": "DOWN", "vlanID":"2"}
]


# Dummy data to represent a network switch, it is not db record
switches = [
    {"id": 1, "switchName": "switch1", "metric": "CPUPercent", "value": "30"},
    {"id": 2, "switchName": "switch1", "metric": "MemoryPercent", "value": "45"},
    {"id": 3, "switchName": "switch2", "metric": "CPUPercent", "value": "50"},
    {"id": 4, "switchName": "switch3", "metric": "MemoryPercent", "value": "63"},
    {"id": 5, "switchName": "switch4", "metric": "CPUPercent", "value": "50"}
]

# Dummy data to represent a network switch, it is not db record
MACAddresses = [
    {"id": 1, "MACAddress": "AABBCC", "switchName": "switch1", "interface": "gigabit 1/0/3"},
    {"id": 2, "MACAddress": "AABBCC", "switchName": "switch2", "interface": "gigabit 1/0/2"},
    {"id": 3, "MACAddress": "AABBCC", "switchName": "switch3", "interface": "gigabit 1/0/21"},
    {"id": 4, "MACAddress": "AABBCC", "switchName": "switch4", "interface": "gigabit 1/0/10"}
]


## RestAPI functions ####

## PORT ##
# GET request to retrieve a list of all ports.. this is for backend call
@app.route('/ports', methods=['GET'])
def get_ports():
    return jsonify(ports)
    # return jsonify("this is for backend call, please get directly from DB by yourself :)")

# GET request to get Port info directly from switch and update to DB
@app.route('/ports/getPortRealInfo/<int:id>', methods=['GET'])
def get_port(id):
    # --> get from switch
    port = next((port for port in ports if port["id"] == id), None)
    if port is None:
        return "port not found", 404
    return jsonify(port)

# PUT request to update a specific port by ID
@app.route('/ports/updatePort/<int:id>', methods=['PUT'])
def update_port(id):
    data = request.get_json()
    port = next((port for port in ports if port["id"] == id), None)
    if port is None:
        return "port not found", 404
    port["portName"] = data["portName"]
    port["status"] = data["status"]
    port["vlanID"] = data["vlanID"]
    return jsonify(port)

## SWITCH ##
# GET request to retrieve a list of all switches.. this is for backend call
@app.route('/switches', methods=['GET'])
def get_switches():
    # return jsonify(switches)
    return jsonify("..this is for backend call, please get directly from DB by yourself :)")

# GET request to get switch's metrics from real switch and update to DB
@app.route('/switches/getSwitchRealInfo/<int:id>', methods=['GET'])
def get_switch(id):
    # --> get from real switch
    switch = next((switch for switch in switches if switch["id"] == id), None)
    if switch is None:
        return "switch not found", 404
    return jsonify(switch)


# GET request to get mac-address from all real switch and update to DB, call from backend..
@app.route('/switches/getAllMACAddresses', methods=['GET'])
def get_allMACAddress():
    return jsonify(MACAddresses)

if __name__ == '__main__':
    app.run(debug=True)
