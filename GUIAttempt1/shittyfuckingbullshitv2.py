import wx
import wx.lib.newevent
import serial
import time
ser = serial.Serial(port ='COM4',baudrate=115200)
print(ser.isOpen())

class Window(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,300))
        self.CreateStatusBar()
        self.SetStatusText('Welcome to a sample GUI!')
        self.basicGUI()
        self.Show(True)

    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exit = fileButton.Append(wx.NewId(), "Exit", "Close the window")
        menuBar.Append(fileButton, '&File')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exit)
        self.SetTitle('Sample program')

        panel = wx.Panel(self, pos=(10,10),size = (500,300))
        wx.TextCtrl(panel, pos=(10,10),size=(200,200))
        ledon = wx.Button(panel, label = "LED On", pos = (310,20), size = (100,20))
        ledoff = wx.Button(panel, label = "LED Off", pos=(310,40), size = (100,20))
        flash = wx.Button(panel, label = "Flash", pos=(310,60),size=(100,20))
        panel.Bind(wx.EVT_BUTTON, self.LEDON, ledon)
        panel.Bind(wx.EVT_BUTTON, self.LEDOFF, ledoff)
        panel.Bind(wx.EVT_BUTTON, self.FLASHfn, flash)

    def Quit(self, e):
        self.Close()

    def LEDON(self, e):
        ser.write("ON")
    def LEDOFF(self, e):
        ser.write("OFF")
    def FLASHfn(self, e):
        for x in range (1,6):
            ser.write("ON")
            time.sleep(1)
            ser.write("OFF")
            time.sleep(1)







app = wx.App()
Window(None, title="I fucking hate this library")
app.MainLoop()

