#The program overwrites the file that you select in option [1].
import re
import os
import sys
import json
import requests
import requests.exceptions
import codecs
import urllib3
import urllib3.exceptions
import colorama

def Command_Line():
    optional_command = "\n" + "[1] Extract Ip(s) From File and Save to Another File" + "\n" + "[2] Extract Ip(s) From File" + "\n" + "[3] HTTP Status(JSON style)"  + "\n" + "[4] HTTP Status(Python style)" + "\n" + "[5] Extract and Ping Ip(s) From File"
    print(Fore.RED + optional_command)
    optional_answer = input("Command: ")
    def ip_extract():
        ip_list = []
        file = input("File Name: ")
        if os.path.isdir(file) == True:
            print(file + " is a directory. You can ONLY extract ip(s) from a file.")
            Command_Line()
        else:
            try:
                if os.path.exists(file):
                    file_name = input("Filename to save ip(s) in: ")
                    if os.path.isdir(file_name) == True:
                        print(file + " is a directory. You can ONLY extract ip(s) from a file.")
                    file = codecs.open(file, 'r' , 'UTF-8')
                    for line in file:
                            ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line + ','  )
                            ip_list.append(ip)
                            print(ip)           
                            with open(file_name, "a") as myfile:
                                myfile.write(str(ip))
                    print("Ip(s) are saved into " + file_name)
                elif os.path.isdir(file) == True:
                    print(file + " is a directory. You can ONLY extract ip from a file.")
                elif os.path.exists(file) == False:
                    print("File " + file + " does not exists")
                    Command_Line()
                else:
                    print("Else returned")
                    Command_Line()
            except IsADirectoryError:
                    print(file_name + " is a directory. You can ONLY extract ip(s) from a file.")
                    Command_Line()
            Command_Line()
    if optional_answer == "":
        print("You didn't type anything.")
        Command_Line()
    elif optional_answer.split()[0] == "1":
        ip_extract()
    elif optional_answer.split()[0] == "2":
            file_ = input("File that conatins ip(s): ")
            try:
                if os.path.exists(file_) == True:
                    file_open = codecs.open(file_, "r", "UTF-8")
                    ip_list = []
                    file_open_read = file_open.read()
                    ip_list.append(file_open_read)
                    print(ip_list)
                elif os.path.exists(file_) == False:
                    print("File " + file_ + " does not exists")
                    Command_Line()
                elif os.path.isdir(file_) == True:
                    print(file + " is a directory. You can ONLY extract ip(s) from a file.")
                else:
                    print("Else returned")
                    Command_Line()
            except IsADirectoryError:
                print(file_ + " is a directory. You can ONLY extract ip(s) from a file.")
                Command_Line()
    elif optional_answer.split()[0] == "3":
        try:
            url = input("Url to get http status: ")
            url = ''.join(('http://', url ,''))
            print("Recieving the status of: " + url)
            payload = {'halo': 'yalo'}
            r = requests.post(url,data=json.dumps(payload))
            status_ =  []
            status_.append(r)
            print(status_)
            Command_Line()
        except requests.exceptions.InvalidURL as e:
            print(e)
            Command_Line()
        except requests.exceptions.ConnectionError as e:
            print(e)
            Command_Line()
    elif optional_answer.split()[0] == "4":
        try:
            question = input("link: ")
            question = ''.join(('http://', question ,''))
            link_status = requests.get(question)
        except requests.exceptions.InvalidURL as e:
            print(e)
            Command_Line()
        if link_status.status_code == 100:
                print("100 Continue")
        elif link_status.status_code == 101:
                print("101 Switching Protocols")
                Command_Line()
        elif link_status.status_code == 102:
                print("102 Processing")
                Command_Line()
        elif link_status.status_code == 200:
                print("200 OK ")
                Command_Line()
        elif link_status.status_code == 201:
                print("201 Created")
                Command_Line()
        elif link_status.status_code == 202:
                print("202 Accepted")
                Command_Line()
        elif link_status.status_code == 203 :
                print("203 Non-authoritative Information")
                Command_Line()        
        elif link_status.status_code == 204:
                print("204 No Content")
                Command_Line()        
        elif link_status.status_code == 205:
                print("205 Reset Content")
                Command_Line()
        elif link_status.status_code == 206:
                print("206 Partial Content")
                Command_Line()
        elif link_status.status_code == 207:
                print("207 Multi-Status")
                Command_Line()
        elif link_status.status_code == 208:
                print("208 Already Reported")
                Command_Line()
        elif link_status.status_code == 226:
                print("226 IM Used")
                Command_Line()
            #3XX Redirection
        elif link_status.status_code == 300:
                print("300 Multiple Choices")
                Command_Line()
        elif link_status.status_code == 301:
                print("301 Moved Permanently")
                Command_Line()
        elif link_status.status_code == 302:
                print("302 Found")
                Command_Line()
        elif link_status.status_code == 303:
                print("303 See Other")
                Command_Line()
        elif link_status.status_code == 304:
                print("304 Not Modified")
                Command_Line()
        elif link_status.status_code == 305:
                print("305 Use Proxy")
                Command_Line()
        elif link_status.status_code == 307:
                print("307 Temporary Redirect")
                Command_Line()
        elif link_status.status_code == 308:
                print("308 Permanent Redirect")
                Command_Line()
            #4XX Client Error
        elif link_status.status_code == 400:
                print("400 Bad Request")
                Command_Line()
        elif link_status.status_code == 401:
                print("401 Unauthorized")
                Command_Line()
        elif link_status.status_code == 402:
                print("402 Payment Required")
                Command_Line()
        elif link_status.status_code == 403:
                print("403 Forbidden")
                Command_Line()
        elif link_status.status_code == 404:
                print("404 Not Found")
                Command_Line()
        elif link_status.status_code == 405:
                print("405 Method Not Allowed")
                Command_Line()
        elif link_status.status_code == 406:
                print("406 Not Acceptable")
                Command_Line()
        elif link_status.status_code == 407:
                print("407 Proxy Authentication Required")
                Command_Line()
        elif link_status.status_code == 408:
                print("408 Request Timeout")
                Command_Line()
        elif link_status.status_code == 409:
                print("409 Conflict")
                Command_Line()
        elif link_status.status_code == 410:
                print("410 Gone")
                Command_Line()
        elif link_status.status_code == 411:
                print("411 Length Required")
                Command_Line()
        elif link_status.status_code == 412:
                print("412 Precondition Failed")
                Command_Line()
        elif link_status.status_code== 413:
                print("413 Payload Too Large")
                Command_Line()
        elif link_status.status_code == 414:
                print("414 Request-URI Too Long")
                Command_Line()
        elif link_status.status_code == 415:
                print("415 Unsupported Media Type")
                Command_Line()
        elif link_status.status_code == 416:
                print("416 Requested Range Not Satisfiable")
                Command_Line()
        elif link_status.status_code == 417:
                print("417 Expectation Failed")
                Command_Line()
        elif link_status.status_code == 418:
                print("418 I'm a teapot")
                Command_Line()
        elif link_status.status_code == 421:
                print("421 Misdirected Request")
                Command_Line()
        elif link_status.status_code == 422:
                print("422 Unprocessable Entity")
                Command_Line()
        elif link_status.status_code == 423:
                print("423 Locked")
                Command_Line()
        elif link_status.status_code == 424:
                print("424 Failed Dependency")
                Command_Line()
        elif link_status.status_code == 426:
                print("426 Upgrade Required")
                Command_Line()
        elif link_status.status_code == 428:
                print("428 Precondition Required")
                Command_Line()
        elif link_status.status_code == 429:
                print("429 Too Many Requests")
                Command_Line()
        elif link_status.status_code == 431:
                print("431 Request Header Fields Too Large")
                Command_Line()
        elif link_status.status_code == 444:
                print("444 Connection Closed Without Response")
                Command_Line()
        elif link_status.status_code == 451:
                print("451 Unavailable For Legal Reasons")
                Command_Line()
        elif link_status.status_code == 499:
                print("499 Client Closed Request")
                Command_Line()
            #5XX Server Error
        elif link_status.status_code == 500:
                print("500 Internal Server Error")
                Command_Line()
        elif link_status.status_code == 501:
                print("501 Not Implemented")
                Command_Line()
        elif link_status.status_code == 502:
                print("502 Bad Gateway")
                Command_Line()
        elif link_status.status_code == 503:
                print("503 Service Unavailable")
                Command_Line()
        elif link_status.status_code == 504:
                print("504 Gateway Timeout")
                Command_Line()
        elif link_status.status_code == 505:
                print("HTTP Version Not Supported")
                Command_Line()
        elif link_status.status_code == 506:
                print("506 Variant Also Negotiates")
                Command_Line()
        elif link_status.status_code == 507:
                print("507 Insufficient Storage")
                Command_Line()
        elif link_status.status_code == 508:
                print("508 Loop Detected")
                Command_Line()
        elif link_status.status_code == 510:
                print("510 Not Extended")
                Command_Line()
        elif link_status.status_code == 511:
                print("511 Network Authentication Required")
                Command_Line()
        elif link_status.status_code == 599:
                print("599 Network Connect Timeout Error")
                Command_Line()
    elif optional_answer.split()[0] == "5":
            file_ = input("File that conatins ip(s): ")
            if os.path.exists(file_) == True:
                file_open = codecs.open(file_, "r", "UTF-8")
                ip_list = []
                file_open_read = file_open.read()
                ip_list.append(file_open_read)
                ip_list.split("[")
                print(ip_list)
                Command_Line()
       # for line in file_open:
       #     ip_list = []
       #     ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
       #     print(str(ip))
       #     for i in range(len(ip_list)):
       #        print(str(ip_list))
            Command_Line()
    elif optional_answer == "pwd":
        print(os.getcwd())
        Command_Line()
    elif optional_answer.split()[0] == "cd":
        try:
            if os.path.isdir(optional_answer.split()[1]) == True:
                os.chdir(optional_answer.split()[1])
                print("You are currently in " + os.getcwd() + " .")
                Command_Line()               
            elif os.path.isdir(optional_answer.split()[1]) == False:
                print("Path: " + optional_answer.split()[1] + " does not exists.")
                Command_Line()
        except IndexError:
            print("Command " + optional_answer +" does not exist.")
            Command_Line()
    elif optional_answer == "ls":
        print("\n".join(os.listdir()))
        Command_Line()
    elif optional_answer == "exit":
        print("Thanks for using our tool. See you soon.")
        sys.exit()
    else:
        print("Command " + optional_answer +" is not present.")
        Command_Line()
Command_Line()
#----------TESTS----------#
#[1] Extracting and saving to another file: CHECK
#[1] Giving File Name blank input: CHECK
#[1] Giving File Name a directory: CHECK
#
#

