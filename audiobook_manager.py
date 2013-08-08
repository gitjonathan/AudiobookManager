import subprocess
import threading
import time
from Tkinter import *

class Application(Frame):
    def rip_cd_process(self):
        cd_status = subprocess.call(["cdparanoia", "-Q"])
        while cd_status == 1: #0 appears to be good
           print "CD NOT READY, PLEASE WAIT"
           time.sleep(2)
           cd_status = subprocess.call(["cdparanoia", "-Q"])

        #subprocess.call(["cdparanoia", "-wv", "1-", filename])

    def run_cdparanoia(self):
        if self.author.get() == "Enter Author":
           print("Please Enter Author") #TODO - print to a dialog
        if self.book.get() == "Enter Title":
           print("Please Enter Title") #TODO - print to a dialog

        self._cdp = threading.Thread(target=self.rip_cd_process)
        self._cdp.start()
 
    def createEntries(self):
        entryHeight = "15"
        entryWidth  = "30"
        entryFont   = "{courier 20 bold}"

        self.author_entry = Entry()
        self.author_entry.pack(side = "left", ipadx = entryWidth, ipady = entryHeight)
        self.author = StringVar()
        self.author.set("Enter Author")
        self.author_entry["textvariable"] = self.author
        self.author_entry["font"] = entryFont 

        self.book_entry = Entry()
        self.book_entry.pack(side = "left", ipadx = entryWidth, ipady = entryHeight)
        self.book = StringVar()
        self.book.set("Enter Title")
        self.book_entry["textvariable"] = self.book
        self.book_entry["font"] = entryFont

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.run_cdp = Button(self)
        self.run_cdp["text"] = "Hello",
        self.run_cdp["command"] = self.run_cdparanoia #self.run_cdparanoia("test.wav")

        self.run_cdp.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createEntries()

root = Tk()
app = Application(master=root)
app.master.maxsize(500, 500)
app.master.minsize(500, 500)
app.master.title("Audiobook Manager")
app.mainloop()
root.destroy()
