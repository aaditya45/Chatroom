import socket
import tkinter
import threading
import tkinter.scrolledtext
from tkinter import simpledialog
import time

class Client:
    def __init__(self,host,port):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))
        msg=tkinter.Tk()
        msg.withdraw()
        
        self.nickname=simpledialog.askstring("nickname","please enter nickname",parent=msg)
        self.gui_done=False
        self.running=True
        
        gui_thread=threading.Thread(target=self.gui_loop)
        receive_thread=threading.Thread(target=self.receive)
        
        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win=tkinter.Tk()
        self.win.configure(bg='lightgrey')
        
        self.chat_label=tkinter.Label(self.win,text='chat',bg='lightgrey')
        self.chat_label.config(font=("Ariel",12))
        self.chat_label.pack(padx=20,pady=5)

        self.text_area=tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20,pady=5)
        self.text_area.config(state='disabled')

        self.msg_label=tkinter.Label(self.win,text='message',bg='lightgrey')
        self.msg_label.config(font=("Ariel",12))
        self.msg_label.pack(padx=20,pady=5)

        self.input_area=tkinter.Text(self.win,height=3)
        self.input_area.pack(padx=20,pady=5)

        self.send_button=tkinter.Button(self.win,text='send',command=self.write)
        self.send_button.config(font=("Ariel",12))
        self.send_button.pack(padx=20,pady=5)

        self.gui_done=True

        self.win.protocol("WM_DELETE_WINDOW",self.stop)
        self.win.mainloop()

    def write(self):
        message=f"{self.nickname}: {self.input_area.get('1.0','end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0','end')

    def stop(self):
        self.running=False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            #print('receive loop')
            #time.sleep(2)
            try:
                message=self.sock.recv(1024).decode('utf-8')
                print(f"message: {message}")
                if message=='NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end',message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except Exception as e:
                print(f"Exception@receive:{str(e)}")
                self.sock.close()
                break

client=Client("localhost",9090)