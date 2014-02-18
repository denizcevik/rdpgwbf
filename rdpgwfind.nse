description = [[
Detects Microsoft RDP Gateways with HTTP over RPC requests.
]]
 
author = "Deniz Cevik"
license = "Same as Nmap--See http://nmap.org/book/man-legal.html"
categories = {"discovery", "safe"}

local http = require "http"
local shortport = require "shortport"

portrule = shortport.http

action = function(host, port)
                response = http.generic_request(host, port, "RPC_IN_DATA", "/rpc/rpcproxy.dll?localhost:3388")
                if http.response_contains(response,"401 Unauthorized",true) then
                                if http.response_contains(response,"Access Denied",true) then
                                                return string.format("Microsoft RDP Gateway Migth Be Detected !")
                                end
        end
end