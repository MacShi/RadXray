# -*- coding: utf-8 -*-
'''
Filename:
Author: mac
Date:
Desc:
'''
import os
import subprocess
def start_xray(port,file_name):
    try:
        xray_cmd= subprocess.Popen("xray/xray_amd64.exe --config xray/config.yaml webscan --listen 0.0.0.0:{}  --html-output ./result/{}".format(port,file_name),shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(xray_cmd.pid)
        # while xray_cmd.poll() is None:
        #     line = xray_cmd.stdout.readline()
        #     line = line.strip()
        #     print(line.decode('utf8'))
        return True
    except Exception as e:
        print("start_xray error",e)
        return False
def start_rad(url,xray_port,interface_file_name):
    try:
        rad_cmd= subprocess.Popen("rad_windows_amd64.exe -t {}  --auto-index --http-proxy 127.0.0.1:{}  --json-output ./result/{}".format(url,xray_port,interface_file_name),shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while rad_cmd.poll() is None:
            line = rad_cmd.stdout.readline()
            line = line.strip()
            print(line.decode('utf8'))
            print("pid", rad_cmd.pid)
    except Exception as e:
        print("start_rad error",e)
class auto_scan:
    def __init__(self,url,xray_port,xray_result_file_name,rad_result_file_nme):
        self.url=url
        self.xray_port=xray_port
        self.xray_result_file_name=xray_result_file_name
        self.rad_result_file_nme=rad_result_file_nme

    def start_xray(self):
        try:
            xray_cmd = subprocess.Popen(
                "xray/xray_amd64.exe --config xray/config.yaml webscan --listen 0.0.0.0:{}  --html-output ./result/{}".format(
                    self.xray_port, self.xray_result_file_name), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.xray_pid=xray_cmd.pid
            # while xray_cmd.poll() is None:
            #     line = xray_cmd.stdout.readline()
            #     line = line.strip()
            #     print(line.decode('utf8'))
            return True
        except Exception as e:
            print("start_xray error", e)
            return False

    def start_rad(self):
        try:
            rad_cmd = subprocess.Popen(
                "rad_windows_amd64.exe -t {}  --auto-index --http-proxy 127.0.0.1:{}  --json-output ./result/{}".format(
                    self.url, self.xray_port, self.rad_result_file_nme), shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.rad_pid=rad_cmd.pid
            while rad_cmd.poll() is None:
                line = rad_cmd.stdout.readline()
                line = line.strip()
                print(line.decode('utf8'))
                print("pid", rad_cmd.pid)
        except Exception as e:
            print("start_rad error", e)



if __name__ == '__main__':
    # if start_xray("9999","aa.html"):
    url ="http://vulmanage.yunshanmeicai.com/vulmanage/"
    #     start_rad(url,9999,"aa.json")
    auto_scan=auto_scan(url=url,xray_port=9999,xray_result_file_name="aa.html",rad_result_file_nme="aa.json")
    auto_scan.start_rad()
    print("============asdffds==============")
    print(auto_scan.rad_pid)
    print(auto_scan.xray_pid)
    print("============asdffds==============")



