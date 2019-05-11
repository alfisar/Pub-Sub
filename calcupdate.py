from tkinter import *

label = "" 

def press(num): 

    global label
  
    label = label + str(num) 
  
    eksekusi.set(label) 
  
  
def equalpress(): 

    try: 
  
        global label
   
        total = str(eval(label)) 
  
        eksekusi.set(total) 
        label = str(total)
  
    except: 
  
        equation.set(" error ") 
        label = "" 
  
def hapus(): 
    global label
    label = "" 
    eksekusi.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    gui = Tk() 

    gui.configure(background="black") 
  
    gui.title("Calculator Update") 
  
    gui.geometry("330x150") 
  
    eksekusi = StringVar() 
  

    label_field = Entry(gui, textvariable=eksekusi)
  
    label_field.grid(columnspan=4, ipadx=85) 
  
   
    button1 = Button(gui, text=' 1 ', fg='black', bg='grey', 
                     command=lambda: press(1), height=1, width=7) 
    button1.grid(row=3, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='grey', 
                     command=lambda: press(2), height=1, width=7) 
    button2.grid(row=3, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='grey', 
                     command=lambda: press(3), height=1, width=7) 
    button3.grid(row=3, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='grey', 
                     command=lambda: press(4), height=1, width=7) 
    button4.grid(row=2, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='grey', 
                     command=lambda: press(5), height=1, width=7) 
    button5.grid(row=2, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='grey', 
                     command=lambda: press(6), height=1, width=7) 
    button6.grid(row=2, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='grey', 
                     command=lambda: press(7), height=1, width=7) 
    button7.grid(row=1, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='grey', 
                     command=lambda: press(8), height=1, width=7) 
    button8.grid(row=1, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='grey', 
                     command=lambda: press(9), height=1, width=7) 
    button9.grid(row=1, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='grey', 
                     command=lambda: press(0), height=1, width=7) 
    button0.grid(row=4, column=0) 
  
    tambah = Button(gui, text=' + ', fg='black', bg='grey', 
                  command=lambda: press("+"), height=1, width=7) 
    tambah.grid(row=1, column=3) 
    
    kurang = Button(gui, text=' - ', fg='black', bg='grey', 
                  command=lambda: press("-"), height=1, width=7) 
    kurang.grid(row=2, column=3) 
    kali = Button(gui, text=' * ', fg='black', bg='grey', 
                      command=lambda: press("*"), height=1, width=7) 
    kali.grid(row=3, column=3) 
  
    bagi = Button(gui, text=' / ', fg='black', bg='grey', 
                    command=lambda: press("/"), height=1, width=7) 
    bagi.grid(row=4, column=3) 
  
    hasil = Button(gui, text=' = ', fg='black', bg='grey', 
                   command=equalpress, height=1, width=7) 
    hasil.grid(row=4, column=2) 
  
    hapus = Button(gui, text='Clear', fg='black', bg='grey', 
                   command=hapus, height=1, width=7) 
    hapus.grid(row=4, column='1') 
    
    gui.mainloop()
    

