import paho.mqtt.client as mqtt
# Membuat alamat broker
broker_address="127.0.0.1"

#  Membuat cliaent baru
print("creating new instance")
client = mqtt.Client("P1")

# Koneksi dengan broker menggunakan port bawaan
print("connecting to broker")
client.connect(broker_address,1883,60)

print ("read file")

# Melakukan pubish dengan judul publish update data yang di publish akan terus kesimpan di server jika server tidak di restart
f=open("calcupdate.py", "rb")
l = f.read()
byteArr = bytes(l)
client.loop()
client.publish("update",byteArr,0,True)

# Melakukan pubish dengan judul publish yaitu reset data yang di publish akan terus kesimpan di server jika server tidak di restart
f=open("calcreset.py", "rb")
l = f.read()
byteArr = bytes(l)
client.loop()
client.publish("reset",byteArr,0,True)

print("end read")

# Memberhentikan loop dan mendisconnectkan client
client.loop_stop()
client.disconnect()
