from paho.mqtt import client as mqtt
from PyScriptTools  import CPUTools as cpu
import time 

client = mqtt.Client()
client.connect("140.127.220.208", 1883, 60)

while True:
    cpuload = cpu.ShowCPUTotalUsage(show=True)
    cpuload=cpuload.replace("%","")
    cpu_usage =int(float(cpuload)/1)
    print("The CPU usage is : ", cpu_usage ,"%")
    client.publish("XIANGYU", cpu_usage)
    time.sleep(1)