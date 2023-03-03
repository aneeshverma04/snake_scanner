import subprocess
import masscan
import nmap3
import json
import ast

def nmap_python_ports_fetch(nmap_result,ip):
    formatted_result = nmap_result[ip]['ports']
    size = len(formatted_result)
    list_ports = []

    for i in range(size):
        port_num = formatted_result[i]['portid']
        if 'service' in formatted_result[i].keys():
            service = formatted_result[i]['service']
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

    return list_ports

def masscan_ports_fetch(speed,ip):
    # Speed packets per second
    # sudo masscan 167.99.203.53 -p1-65535 --rate=250

    print("Scanning of ports started with speed of " + str(speed) + " packet per second. Please be patient.")
    
    mscan = masscan.PortScanner()
    
    mscan.scan(ip, ports='1-65535', arguments='--max-rate '+ str(speed))
    
    mscan_dict = ast.literal_eval(mscan.scan_result)
    mscan_result_formatted = mscan_dict["scan"][ip]

    size_mscan = len(mscan_result_formatted)
    list_mscan_ports = []

    for i in range(size_mscan):
        list_mscan_ports.append(mscan_result_formatted[i]['port'])

    print(list_mscan_ports)

    return list_mscan_ports

def check_website_python(url):
    # nmap
    # nmap scanme.nmap.org -sV -p 80,443
    print(url)
    # www.rick.htb
    # Fetch ip from domain name as masscan requires ip 
    command = "resolveip -s " + url
    ip = subprocess.check_output(command, shell=True).rstrip().decode('utf-8')
    print(ip)
    # Use masscan and search for all possible open ports (tcp)
    # mscan_list_1000 = masscan_ports_fetch(1000,ip)
    # mscan_list_500 = masscan_ports_fetch(500,ip)
    # mscan_list_250 = masscan_ports_fetch(250,ip)
    # # mscan_list_100 = masscan_ports_fetch(100,ip)
    
    # # mscan_list = mscan_list_1000 + mscan_list_500 + mscan_list_250 + mscan_list_100
    # mscan_list = mscan_list_1000 + mscan_list_500 + mscan_list_250
    # mscan_list_unique = list(set(mscan_list))
    
    # print(mscan_list_unique)
    
    #mscan_list_unique = [30477, 32272, 32157, 31522, 30119, 32171, 30125, 32558, 31795, 32309, 32186, 30654, 30532, 31948, 30415, 30927, 32350, 30432, 31074, 46311, 31841]
    mscan_list_unique = [31415]    
    mscan_list_str = ''.join(str(val)+"," for val in mscan_list_unique)
    mscan_list_str = mscan_list_str[:-1]    
    print(mscan_list_str)

    nmap = nmap3.Nmap()
    # args="-sV -Pn -p 30432"
    
    # nmap_result = nmap.scan_top_ports(url, args="-sV -Pn -p 30432,80")
    nmap_result = nmap.nmap_version_detection(url, args="-Pn -p "+mscan_list_str)

    # nmap = nmap3.NmapScanTechniques()
    # nmap_result = nmap.nmap_tcp_scan(url)
    # print(json.dumps(nmap_result, indent=4))

    python_ports = nmap_python_ports_fetch(nmap_result,ip)
    ports_str = ''.join(str(val)+"," for val in python_ports)
    ports_str = ports_str[:-1]  
    print("The ports which contain a python server are:"+ports_str)
    return python_ports
    
def fetch_editable_data(ports):
    pass

if __name__=="__main__":
    url = input("Enter the website you want to scan: ")
    python_ports = check_website_python(url)
    fetch_editable_data(python_ports)