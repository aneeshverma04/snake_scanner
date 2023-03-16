import subprocess
import masscan
import nmap3
import json
import ast
import requests
import base64
import pickle 
import pickletools
from io import StringIO

def nmap_python_ports_fetch(nmap_result,ip):
    if ip in nmap_result:
        formatted_result = nmap_result[ip]['ports']
    else:
        print("Nmap Result incomplete")
        return []

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
    # print(mscan_dict)
    if ip in mscan_dict["scan"]:
        mscan_result_formatted = mscan_dict["scan"][ip]
    else:
        return []

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
    mscan_list_1000 = masscan_ports_fetch(1000,ip)
    mscan_list_500 = masscan_ports_fetch(500,ip)
    mscan_list_250 = masscan_ports_fetch(250,ip)
    # mscan_list_100 = masscan_ports_fetch(100,ip)

    mscan_list = mscan_list_1000 + mscan_list_500 + mscan_list_250
    # mscan_list = mscan_list_1000 + mscan_list_500 + mscan_list_250 + mscan_list_100

    # mscan_list = []
    # for i in range(5):
    #     mscan_list = mscan_list + masscan_ports_fetch(1000,ip)
   

    mscan_list_unique = list(set(mscan_list))
    # mscan_list_unique = [80,443]
    
    # print(mscan_list_unique)
    
    # mscan_list_unique = [30341,32045]    
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
    # print(nmap_result)

    python_ports = nmap_python_ports_fetch(nmap_result,ip)
    ports_str = ''.join(str(val)+"," for val in python_ports)
    ports_str = ports_str[:-1]  
    if ports_str == '':
        print ("There are no ports containing python server")
        return []
    print("The ports which contain a python server are:"+ports_str)
    return python_ports
    #return mscan_list_unique
    
def fetch_editable_data(url,ports):
    editable_data = []
    
    for port in ports:
        new_session = requests.session()
        if port == 443:
            url_complete = "https://"+url+":"+str(port)
            #resp = new_session.get("https://"+url+str(port))
            new_session.get(url_complete)
        else:
            url_complete = "http://"+url+":"+str(port)
            #resp = new_session.get("http://"+url+":"+str(port))
            new_session.get(url_complete)
        cookie = list(new_session.cookies.get_dict().values())
        if cookie == []:
            cookie = ['None']
        editable_data = editable_data + cookie

    return (editable_data)

        # start fuzzing and get cookies of each
        # wordlist_file = open("common.txt","r")

        # for l in wordlist_file:
        #     w = l.strip()
        #     url_new = url_complete + "/" + w
        #     resp = new_session.get(url_new)
        #     if resp:
        #         print("Discovered directory at this link: " + url_new)
        #         print (new_session.cookies.get_dict()) 

def decrypting_cookies(data):
    decrypted_data = []
    for val in data:
        # if val is base 64
        decrypted_data.append(base64.b64decode(val))
    return decrypted_data

def check_object_picklable(data):
    picklable_data = []
    for val in data:
        try:
            pickletools.dis(val,out=StringIO())
            picklable_data.append(True)
        except:
            picklable_data.append(False)
    StringIO().close
    return picklable_data

if __name__=="__main__":
    url = input("Enter the website you want to scan: ")
    python_ports = check_website_python(url)
    encrypted_data = fetch_editable_data(url,python_ports)
    decrypted_data = decrypting_cookies(encrypted_data)
    # decrypted_data = [b"(dp0\nS'serum'\np1\nccopy_reg\n_reconstructor\np2\n(c__main__\nanti_pickle_serum\np3\nc__builtin__\nobject\np4\nNtp5\nRp6\ns.","dadas",b"(dp0\nS'serum'\np1\nccopy_reg\n_reconstructor\np2\n(c__main__\nanti_pickle_serum\np3\nc__builtin__\nobject\np4\nNtp5\nRp6\ns."]
    picklable_data = check_object_picklable(decrypted_data)
    flag = False
    for i in range(len(picklable_data)):
        if picklable_data[i] != False:
            print(url+ ":" + str(python_ports[i]) +" might be susceptible to Insecure Deserialization")
            flag = True
    
    if flag == False:
        print("This website is not susceptible to Insecure Deserialization")