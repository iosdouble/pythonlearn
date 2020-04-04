
import nmap
nm=nmap.PortScanner()
nm.scan('192.168.125.134','445')
a=nm['192.168.125.134'].all_protocols()    #返回主机扫描的端口包含的协议
print(a)
##################################




