from tkinter import * 
from tkinter.ttk import * 
from time import strftime 

import paho.mqtt.client as mqtt
import time

import os

def on_message(client, userdata, message):
      # Menimpa data yang ada pada Calc.py dengan data message.payload
      with open("Calc.py","wb") as text:
            text.write(message.payload)
            text.close
      # Keluar dari tampilan GUI
      gui.destroy()

      # Memberhentikan loop client
      client.loop_stop()

def update():
      # P2 subcribe ke topik "update"
      print("Done Update")
      client.loop_start()
      client.subscribe("update")


      client.on_message=on_message


def reset():
      # P2 subcribe ke topik "reset"
      print("Done Reset")
      client.loop_start()
      client.subscribe("reset")

      client.on_message=on_message

# Mendeklarasikan GUI dengan fungsi TK
gui = Tk() 

#  Pemberian warna belakang pada GUI
gui.configure(background="grey") 

# Pemberian Title pada GUI  
gui.title("COTS") 

# Mendeklarasikan Besar GUI
gui.geometry("300x300") 


# Alamat Broker
broker_address="127.0.0.1"

# buat client P2 
print("Membuat Client P2....")
client = mqtt.Client("P2")


# koneksi P2 ke broker
print("Connecting...")
client.connect(broker_address,1883,60)


# Label Judul Pada GUI
Label(gui, text = 'Welcome In My COTS SISTER',  
      font =('Verdana', 15)).pack(side = TOP, pady = 10) 
      
# pemilihan antara update calculator atau mereset calculator ke awal kembali
Button(gui, text = 'Update', command = update).pack(side = TOP, pady = 10) 
Button(gui, text = 'Reset Calculator', command = reset).pack(side = TOP, pady = 10) 

# Menjalankan GUI
gui.mainloop()

# Menjalankan file Calc.py saya menggunakan ubuntu jika menggunakan windows maka python3 silahkan di hapus
os.system('python3 Calc.py')

