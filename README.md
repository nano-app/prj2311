## 1. Environment 
required: dev = test = production (it is for me and end customer ! :)
- windows 10
- docker
- php/nodejs/python/mysql/postgres ...

## 2. how to run network_api from docker:
docker run --name myrest -p 5000:5000 -d andrewxplorer/prj2311_switch_restapi:v.0.1

## 3. how to test function of network_api:
------------
### function: get port info by ID, real-time from switch
curl http://127.0.0.1:8081/ports/1

### function: put (upate) port status/vlan.. json payload 
curl -X PUT -H "Content-Type: application/json" -d '{"portName": "swport", "status": "UP","vlanID":"10"}' http://127.0.0.1:8081/ports/updatePort/1

-------------
### fucntion: get real time metrics from switch
curl http://localhost:5000/switches/getSwitchRealInfo/1

-------------
### fuction: get mac address real-time from all switch (!!) 
curl http://localhost:5000/switches/getAllMACAddresses 



