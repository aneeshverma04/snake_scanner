import json

d = {
    "167.99.203.53": {
        "osmatch": {},
        "ports": [
            {
                "protocol": "tcp",
                "portid": "30119",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Apache httpd",
                    "version": "2.4.41",
                    "extrainfo": "(Ubuntu)",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:apache:http_server:2.4.41"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "30125",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Node.js",
                    "extrainfo": "Express middleware",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:nodejs:node.js"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "30415",
                "state": "filtered",
                "reason": "no-response",
                "reason_ttl": "0",
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "30432",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Werkzeug httpd",
                    "version": "1.0.1",
                    "extrainfo": "Python 2.7.17",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:python:python:2.7.17"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "30477",
                "state": "filtered",
                "reason": "no-response",
                "reason_ttl": "0",
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "30532",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "nginx",
                    "version": "1.19.2",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:igor_sysoev:nginx:1.19.2"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "30654",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Apache httpd",
                    "version": "2.4.41",
                    "extrainfo": "(Ubuntu)",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:apache:http_server:2.4.41"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "30927",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Apache httpd",
                    "version": "2.4.41",
                    "extrainfo": "(Ubuntu)",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:apache:http_server:2.4.41"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "31074",
                "state": "filtered",
                "reason": "no-response",
                "reason_ttl": "0",
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "31215",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "unknown",
                    "servicefp": "SF-Port31215-TCP:V=7.92%I=7%D=3/2%Time=63FFE15B%P=x86_64-pc-linux-gnu%r(NULL,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(GenericLines,1F,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\\r\\n\")%r(GetRequest,2D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\nGET\\x20/\\x20HTTP/1\\.0\\r\\n\")%r(HTTPOptions,31,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\nOPTIONS\\x20/\\x20HTTP/1\\.0\\r\\n\")%r(RTSPRequest,31,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\nOPTIONS\\x20/\\x20RTSP/1\\.0\\r\\n\")%r(RPCCheck,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(DNSVersionBindReqTCP,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(DNSStatusRequestTCP,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(Help,23,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\nHELP\\r\\n\")%r(SSLSessionReq,20,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\\x16\\x03\\n\")%r(TerminalServerCookie,1F,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\\x03\\n\")%r(TLSSessionReq,20,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\\x16\\x03\\n\")%r(Kerberos,1E,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\\n\")%r(SMBProgNeg,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(X11Probe,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(FourOhFourRequest,50,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\nGET\\x20/nice%20ports%2C/Tri%6Eity\\.txt%2ebak\\x20HTTP/1\\.0\\r\\n\")%r(LPDString,26,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\\x01default\\n\")%r(LDAPSearchReq,20,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n0\\x84\\n\")%r(LDAPBindReq,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(SIPOptions,35,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\nOPTIONS\\x20sip:nm\\x20SIP/2\\.0\\r\\n\")%r(LANDesk-RC,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(TerminalServer,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(NCP,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(NotesRPC,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(JavaRMI,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(WMSRequest,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(oracle-tns,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\")%r(ms-sql-s,1D,\"You\\x20know\\x20who\\x20are\\x200xDiablos:\\x20\\n\");",
                    "method": "table",
                    "conf": "3"
                },
                "cpe": [],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "31522",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Node.js Express framework",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:nodejs:node.js"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "31795",
                "state": "filtered",
                "reason": "no-response",
                "reason_ttl": "0",
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "31948",
                "state": "filtered",
                "reason": "no-response",
                "reason_ttl": "0",
                "service": {
                    "name": "iceedcp_tx",
                    "method": "table",
                    "conf": "3"
                },
                "cpe": [],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "32157",
                "state": "filtered",
                "reason": "no-response",
                "reason_ttl": "0",
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "32171",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Apache httpd",
                    "version": "2.4.41",
                    "extrainfo": "(Ubuntu)",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:apache:http_server:2.4.41"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "32186",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Node.js Express framework",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:nodejs:node.js"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "32272",
                "state": "filtered",
                "reason": "no-response",
                "reason_ttl": "0",
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "32309",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Apache httpd",
                    "version": "2.4.41",
                    "extrainfo": "(Ubuntu)",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:apache:http_server:2.4.41"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "32350",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "mysql",
                    "product": "MySQL",
                    "version": "5.5.5-10.7.3-MariaDB-1:10.7.3+maria~focal",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:mariadb:mariadb:5.5.5-10.7.3-mariadb-1%3A10.7.3%2Bmaria~focal"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "32558",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "http",
                    "product": "Apache httpd",
                    "version": "2.4.41",
                    "extrainfo": "(Ubuntu)",
                    "method": "probed",
                    "conf": "10"
                },
                "cpe": [
                    {
                        "cpe": "cpe:/a:apache:http_server:2.4.41"
                    }
                ],
                "scripts": []
            },
            {
                "protocol": "tcp",
                "portid": "46311",
                "state": "open",
                "reason": "syn-ack",
                "reason_ttl": "128",
                "service": {
                    "name": "tcpwrapped",
                    "method": "probed",
                    "conf": "8"
                },
                "cpe": [],
                "scripts": []
            }
        ],
        "hostname": [
            {
                "name": "www.rick.htb",
                "type": "user"
            },
            {
                "name": "www.rick.htb",
                "type": "PTR"
            }
        ],
        "macaddress": 'null',
        "state": {
            "state": "up",
            "reason": "user-set",
            "reason_ttl": "0"
        }
    },
    "runtime": {
        "time": "1677713851",
        "timestr": "Thu Mar  2 05:07:31 2023",
        "summary": "Nmap done at Thu Mar  2 05:07:31 2023; 1 IP address (1 host up) scanned in 104.54 seconds",
        "elapsed": "104.54",
        "exit": "success"
    },
    "stats": {
        "scanner": "nmap",
        "args": "/usr/bin/nmap -v -oX - -sV -Pn -p 30477,32272,32157,31522,30119,32171,30125,32558,31795,32309,32186,30654,30532,31948,30415,30927,32350,30432,31074,46311,31215 www.rick.htb",
        "start": "1677713747",
        "startstr": "Thu Mar  2 05:05:47 2023",
        "version": "7.92",
        "xmloutputversion": "1.05"
    },
    "task_results": [
        {
            "task": "SYN Stealth Scan",
            "time": "1677713748",
            "extrainfo": "21 total ports"
        },
        {
            "task": "Service scan",
            "time": "1677713841",
            "extrainfo": "14 services on 1 host"
        },
        {
            "task": "NSE",
            "time": "1677713850"
        },
        {
            "task": "NSE",
            "time": "1677713851"
        }
    ]
}

# print (d["167.99.203.53"]['ports'])
# print(json.dumps(d, indent=4))

d3 = d["167.99.203.53"]['ports']
# # print(json.dumps(d2, indent=4))

# print(json.dumps(d3, indent=4))

size = len(d3)

list_ports = []

for i in range(size):
    port_num = d3[i]['portid']
    if 'service' in d3[i].keys():
        service = d3[i]['service']
        flag = False
        if 'product' in service.keys():
            if "Python" in service['product']:
                flag = True
        if 'extrainfo' in service.keys():
            if "Python" in service['extrainfo']:
                flag = True
        if flag is True:
            list_ports.append(port_num)
            flag = False

print(list_ports)
