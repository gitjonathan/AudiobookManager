import subprocess
import threading
import time
import wx

class AudioManager(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(350,200))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

	panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        txtAudioMan = wx.StaticText(panel, -1, "Audio Manager")
        txtAudioMan.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        txtAudioMan.SetSize(txtAudioMan.GetBestSize())
        box.Add(txtAudioMan, 0, wx.ALL, 10)

        close = wx.Button(panel, wx.ID_CLOSE, "Close")
        close.Bind(wx.EVT_BUTTON, self.OnClose)
        box.Add(close, 0, wx.ALL, 10)

        start = wx.Button(panel, wx.ID_FORWARD, "Begin")
        start.Bind(wx.EVT_BUTTON, self.RipCdProcess)
        box.Add(start, 0, wx.ALL, 10)

        panel.SetSizer(box)
        panel.Layout()

    def OnClose(self, event):
        dlg = wx.MessageDialog(self,
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

    def RipCdProcess(self, event):
        cd_status = subprocess.call(["cdparanoia", "-Q"])
        while cd_status == 1: #o appears to be good
           print "CD NOT READY, PLEASE WAIT"
           time.sleep(2)
	   cd_status = subprocess.call(["cdparanoia", "-Q"])

    def RunCdparanoia(self):
	if self.author.get() == "Enter Author":
           print("Please Enter Author") #TODO - print to a dialog
        if self.book.get() == "Enter Title":
           print("Please Enter Title") #TODO - print to a dialog

        self._cdp = threading.Thread(target=self.rip_cd_process)
        self._cdp.start() 

app = wx.App(redirect=True)
top = AudioManager("Audio Manager")
top.Show()
app.MainLoop()
