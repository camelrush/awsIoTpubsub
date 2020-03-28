import paho.mqtt.client
import ssl
import subprocess
import json
import time

endpoint = "a3ufrbqbd4cwta-ats.iot.ap-northeast-1.amazonaws.com"
port = 8883
topic_to = "homeappto"
topic_from = "homeappfrom"
rootCA = "./cert/AmazonRootCA1.pem"
cert = "./cert/bdad9cbd50-certificate.pem.crt"
key = "./cert/bdad9cbd50-private.pem.key"
 
def on_connect(client, userdata, flags, respons_code):
    print("connected<<")
    client.subscribe(topic_to)
 
def on_message(client, userdata, msg):
    print("received<<" + msg.payload.decode("utf-8"))

def on_publish(client,userdata ,mid):
    print("published>>{0}".format(mid))

if __name__ == '__main__':
    client = paho.mqtt.client.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_message = on_message
    client.tls_set(rootCA, certfile=cert, keyfile=key, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
    client.connect(endpoint, port=port, keepalive=60)
    client.loop_start()
    while True:
        time.sleep(3)
        msg = input("send message\n>>")
        client.publish(topic_from ,msg)
