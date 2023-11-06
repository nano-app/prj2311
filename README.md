## 1. Environment 
required: dev = test = production (=> make it easy for dev/ test and implement at customer site)
- windows 10
- docker
- php/nodejs/python/mysql/postgres ...

## 2. how to run network_api from docker:
> docker run --name myrest -p 5000:5000 -d andrewxplorer/prj2311_switch_restapi:v.0.2

## 3. Function calls:
get port info by ID (real-time from actual switch)
(!) change the last '1','2' .. by actual portID (from db table/collection)
> curl http://127.0.0.1:5000/ports/getPortRealInfo/1

change vlanID of a port
> curl -X PUT -H "Content-Type: application/json" -d '{"vlanID":"10"}' http://127.0.0.1:5000/port/updatePortVlanID/1

turn on a port (status = UP)
> curl -X PUT -H "Content-Type: application/json" -d '{"status":"UP"}' http://127.0.0.1:5000/port/updatePortStatus/2

turn off a port (status = DOWN)
> curl -X PUT -H "Content-Type: application/json" -d '{"status":"DOWN"}' http://127.0.0.1:5000/port/updatePortStatus/2

-------------
get real time metrics from switch
> curl http://localhost:5000/switches/getSwitchRealInfo/1

-------------
get mac address real-time from all switch (!!) 
> curl http://localhost:5000/switches/getAllMACAddresses 



