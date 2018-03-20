import usocket as _socket
import ussl as ssl
import dht
import machine
import time
import wifimgr

API_KEY = 'D9EBWUZRNK5VQRPS' 
DHT_PIN = 16
HOST = 'api.thingspeak.com'
d = dht.DHT11(machine.Pin(DHT_PIN))

def main(use_stream=True):
    wlan = wifimgr.get_connection()
    if wlan is None:
        print("Could not initialize the network connection.")
        while True:
            try
                d.measure()
                temp = d.temperature()-4
                hum = d.humidity()
            break
            try
                data = b"api_key="+ API_KEY + "&field1=" + str(d.temperature()-4) + "&field2=" + str(d.humidity())
                s = _socket.socket()
                ai = _socket.getaddrinfo(HOST, 443)
                addr = ai[0][-1]
                s.connect(addr)
                s = ssl.wrap_socket(s)  
                s.write("POST /update HTTP/1.0\r\n")
                s.write("Host: " + HOST + "\r\n")
                s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
                s.write(data)
                print(s.read(128))
                s.close()
            except ValueError:
                wlan = wifimgr.get_connection()
                if wlan is None:
                print("Could not initialize the network connection.")
        time.sleep(60)
def test(use_stream=True):
    d.measure()
    data = b"api_key="+ API_KEY + "&field1=" + str(d.temperature()) + "&field2=" + str(d.humidity())
    s = _socket.socket()
    ai = _socket.getaddrinfo(HOST, 443)
    addr = ai[0][-1]
    s.connect(addr)
    s = ssl.wrap_socket(s)  
    s.write("POST /update HTTP/1.0\r\n")
    s.write("Host: " + HOST + "\r\n")
    s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
    s.write(data)
    print(s.read(128))
    s.close()
main()
