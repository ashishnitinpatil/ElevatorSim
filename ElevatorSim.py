# Elevator Simulator
# Written by Andrew Bouchard
# This program simulates the behavior of a simple elevator and was written for the Vanderbilt University fall 2008 class
#   CS376 Hybrid and Embedded Systems taught by Xenofon Koutsoukos
# Date Started: 8/31/2008
# Last Updated: 9/8/2008

# Import needed libraries
import wx

# This is the main GUI class
class Elevator(wx.Frame):
    def __init__(self, parent, id, title):
        
        # Initialize the frame
        wx.Frame.__init__(self, parent, id, title, size=(500, 400))
        
        # Declare fonts
        title = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        subtitle = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        
        # Define the panel and the sizer
        panel = wx.Panel(self, -1)
        sizer = wx.GridBagSizer(0, 0)
        
        # Create elevator images
        OpenImage = 'elevator_open.jpg'
        open = wx.Image(OpenImage, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        ClosedImage = 'elevator_closed.jpg'
        closed = wx.Image(ClosedImage, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        
        # Declare the row for the gui widgets
        guirow = 0
        
        # Main Title
        lblmaintitle = wx.StaticText(panel, -1, 'Elevator Simulator', style=wx.ALIGN_CENTER)
        sizer.Add(lblmaintitle, (guirow, 0), (1,5), wx.ALL | wx.EXPAND, 5)
        lblmaintitle.SetFont(title)
        guirow = guirow+1
        lblmainsubtitle = wx.StaticText(panel, -1, 'Written by Andrew Bouchard', style=wx.ALIGN_CENTER)
        sizer.Add(lblmainsubtitle, (guirow, 0), (1,5), wx.ALL | wx.EXPAND, 5)
        lblmainsubtitle.SetFont(subtitle)

        guirow = guirow+1
        
        # Separation line
        line1 = wx.StaticLine(panel, -1 )
        sizer.Add(line1, (guirow, 0), (1, 5), wx.ALL | wx.EXPAND, 5)

        guirow = guirow+1
        
        # Column Labels
        lblIncallsTitle = wx.StaticText(panel, -1, 'Internal calls')
        sizer.Add(lblIncallsTitle, (guirow, 0), flag=wx.ALL | wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL, border=5)
        lblExcallsTitle = wx.StaticText(panel, -1, 'External calls')
        sizer.Add(lblExcallsTitle, (guirow, 2), (1, 2), wx.ALL | wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL, 5)
        
        guirow = guirow+1
        
        # Fifth floor
        # Incall button
        self.cmdIncall5 = wx.ToggleButton(panel, 5, '5')
        sizer.Add(self.cmdIncall5, (guirow, 0), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.Incall, id=self.cmdIncall5.GetId())
        # Elevator graphic
        self.floor5 = wx.StaticBitmap(self, -1, closed)
        sizer.Add(self.floor5, (guirow, 1), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        # Excall up button
        self.cmdExcall5Up = wx.ToggleButton(panel, 15, 'Up')
        sizer.Add(self.cmdExcall5Up, (guirow, 2), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallUp, id=self.cmdExcall5Up.GetId())
        self.cmdExcall5Up.Enable(False)
        # Excall down button
        self.cmdExcall5Down = wx.ToggleButton(panel, 25, 'Down')
        sizer.Add(self.cmdExcall5Down, (guirow, 3), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallDown, id=self.cmdExcall5Down.GetId())
        
        # Variable display
        self.lblElevatorDir = wx.StaticText(panel, -1, 'elevator_dir = HOLD')
        sizer.Add(self.lblElevatorDir, (guirow, 4), (1, 1), wx.ALL | wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        
        guirow = guirow+1
        
        # Fourth floor
        # Incall button
        self.cmdIncall4 = wx.ToggleButton(panel, 4, '4')
        sizer.Add(self.cmdIncall4, (guirow, 0), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.Incall, id=self.cmdIncall4.GetId())
        # Elevator graphic
        self.floor4 = wx.StaticBitmap(self, -1, closed)
        sizer.Add(self.floor4, (guirow, 1), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        # Excall up button
        self.cmdExcall4Up = wx.ToggleButton(panel, 14, 'Up')
        sizer.Add(self.cmdExcall4Up, (guirow, 2), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallUp, id=self.cmdExcall4Up.GetId())
        # Excall down button
        self.cmdExcall4Down = wx.ToggleButton(panel, 24, 'Down')
        sizer.Add(self.cmdExcall4Down, (guirow, 3), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallDown, id=self.cmdExcall4Down.GetId())
        
        # Variable display
        self.lblElevatorLoc = wx.StaticText(panel, -1, 'elevator_loc = 1')
        sizer.Add(self.lblElevatorLoc, (guirow, 4), (1, 1), wx.ALL | wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        
        guirow = guirow+1
        
        # Third floor
        # Incall button
        self.cmdIncall3 = wx.ToggleButton(panel, 3, '3')
        sizer.Add(self.cmdIncall3, (guirow, 0), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.Incall, id=self.cmdIncall3.GetId())
        # Elevator graphic
        self.floor3 = wx.StaticBitmap(self, -1, closed)
        sizer.Add(self.floor3, (guirow, 1), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        # Excall up button
        self.cmdExcall3Up = wx.ToggleButton(panel, 13, 'Up')
        sizer.Add(self.cmdExcall3Up, (guirow, 2), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallUp, id=self.cmdExcall3Up.GetId())
        # Excall down button
        self.cmdExcall3Down = wx.ToggleButton(panel, 23, 'Down')
        sizer.Add(self.cmdExcall3Down, (guirow, 3), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallDown, id=self.cmdExcall3Down.GetId())
        
        # Variable display
        self.lblIncalls = wx.StaticText(panel, -1, 'incalls = []')
        sizer.Add(self.lblIncalls, (guirow, 4), (1, 1), wx.ALL | wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        
        guirow = guirow+1
        
        # Second floor
        # Incall button
        self.cmdIncall2 = wx.ToggleButton(panel, 2, '2')
        sizer.Add(self.cmdIncall2, (guirow, 0), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.Incall, id=self.cmdIncall2.GetId())
        # Elevator graphic
        self.floor2 = wx.StaticBitmap(self, -1, closed)
        sizer.Add(self.floor2, (guirow, 1), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        # Excall up button
        self.cmdExcall2Up = wx.ToggleButton(panel, 12, 'Up')
        sizer.Add(self.cmdExcall2Up, (guirow, 2), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallUp, id=self.cmdExcall2Up.GetId())
        # Excall down button
        self.cmdExcall2Down = wx.ToggleButton(panel, 22, 'Down')
        sizer.Add(self.cmdExcall2Down, (guirow, 3), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallDown, id=self.cmdExcall2Down.GetId())
        
        # Variable display
        self.lblExcallsUp = wx.StaticText(panel, -1, 'excalls_up = []')
        sizer.Add(self.lblExcallsUp, (guirow, 4), (1, 1), wx.ALL | wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        
        guirow = guirow+1
        
        # First floor
        # Incall button
        self.cmdIncall1 = wx.ToggleButton(panel, 1, '1')
        sizer.Add(self.cmdIncall1, (guirow, 0), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.Incall, id=self.cmdIncall1.GetId())
        # Elevator graphic
        self.floor1 = wx.StaticBitmap(self, -1, closed)
        sizer.Add(self.floor1, (guirow, 1), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        # Excall up button
        self.cmdExcall1Up = wx.ToggleButton(panel, 11, 'Up')
        sizer.Add(self.cmdExcall1Up, (guirow, 2), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallUp, id=self.cmdExcall1Up.GetId())
        # Excall down button
        self.cmdExcall1Down = wx.ToggleButton(panel, 21, 'Down')
        sizer.Add(self.cmdExcall1Down, (guirow, 3), (1,1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        self.Bind(wx.EVT_TOGGLEBUTTON,  self.ExcallDown, id=self.cmdExcall1Down.GetId())
        self.cmdExcall1Down.Enable(False)
        
        # Variable display
        self.lblExcallsDn = wx.StaticText(panel, -1, 'excalls_dn = []')
        sizer.Add(self.lblExcallsDn, (guirow, 4), (1, 1), wx.ALL | wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        
        guirow = guirow+1
        
        # Step button
        cmdStep = wx.Button(panel, -1, 'Step')
        sizer.Add(cmdStep, (guirow, 0), (1,2), flag=wx.ALL | wx.ALIGN_CENTER | wx.EXPAND, border=5)
        self.Bind(wx.EVT_BUTTON,  self.Step, id=cmdStep.GetId())
        # Reset button
        cmdReset = wx.Button(panel, -1, 'Reset')
        sizer.Add(cmdReset, (guirow, 2), (1,2), flag=wx.ALL | wx.ALIGN_CENTER | wx.EXPAND, border=5)
        self.Bind(wx.EVT_BUTTON,  self.Reset, id=cmdReset.GetId())
        
        sizer.AddGrowableCol(4)
        sizer.AddGrowableRow(guirow)
        panel.SetSizer(sizer)
        frm_sizer = wx.BoxSizer()
        frm_sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(frm_sizer)
        self.Fit()
        self.Centre()
        self.Show(True)
    
    # Creates an internal call to the appropriate floor
    def Incall(self, event):
        
        # Get global variable of incalls
        global incalls
        
        floor = event.GetId()
        
        # Toggle if floor number is in the incalls
        if floor in incalls:
            incalls.remove(floor)
        else:
            incalls.append(floor)
        
        self.Update()
    
    # Creates an external call going up on the appropriate floor
    def ExcallUp(self, event):
        
        # Get global variable of incalls
        global excalls_up
        
        floor = event.GetId()-10
        
        # Toggle if floor number is in the incalls
        if floor in excalls_up:
            excalls_up.remove(floor)
        else:
            excalls_up.append(floor)
        
        self.Update()
    
    # Creates an external call going down on the appropriate floor
    def ExcallDown(self, event):
        
        # Get global variable of incalls
        global excalls_dn
        
        floor = event.GetId()-20
        
        # Toggle if floor number is in the incalls
        if floor in excalls_dn:
            excalls_dn.remove(floor)
        else:
            excalls_dn.append(floor)
        
        self.Update()
    
    # Updates the GUI display
    def Update(self):
        
        # Get global variables
        global elevator_loc
        global elevator_dir
        global incalls
        global excalls_up
        global excalls_dn
        global doors
        
        # Create elevator images
        OpenImage = 'elevator_open.jpg'
        open = wx.Image(OpenImage, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        ClosedImage = 'elevator_closed.jpg'
        closed = wx.Image(ClosedImage, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        
        # Display the values
        self.lblElevatorLoc.SetLabel(label = "elevator_loc = " + str(elevator_loc))
        self.lblElevatorDir.SetLabel(label = "elevator_dir = " + str(elevator_dir))
        self.lblIncalls.SetLabel(label = "incalls = " + str(incalls))
        self.lblExcallsUp.SetLabel(label = "excalls_up = " + str(excalls_up))
        self.lblExcallsDn.SetLabel(label = "excalls_dn = " + str(excalls_dn))
        
        # Update the elevator display
        if doors == "OPEN" and elevator_loc == 5:
            self.floor5.SetBitmap(open)
        else:
            self.floor5.SetBitmap(closed)
        if doors == "OPEN" and elevator_loc == 4:
            self.floor4.SetBitmap(open)
        else:
            self.floor4.SetBitmap(closed)
        if doors == "OPEN" and elevator_loc == 3:
            self.floor3.SetBitmap(open)
        else:
            self.floor3.SetBitmap(closed)
        if doors == "OPEN" and elevator_loc == 2:
            self.floor2.SetBitmap(open)
        else:
            self.floor2.SetBitmap(closed)
        if doors == "OPEN" and elevator_loc == 1:
            self.floor1.SetBitmap(open)
        else:
            self.floor1.SetBitmap(closed)
        
        # Reset the toggle buttons
        self.SetToggles()
    
    # Resets the state to its initial configuration
    def Reset(self, event):
        
        # Get global variables
        global elevator_loc
        global elevator_dir
        global incalls
        global excalls_up
        global excalls_dn
        global doors
        
        # Reset values to initial values
        elevator_loc = 1
        elevator_dir = "HOLD"
        incalls = []
        excalls_up = []
        excalls_dn = []
        doors = "CLOSED"
        
        self.Update()
    
    # Sets the toggle buttons to their appropriate states
    def SetToggles(self):
        
        # Get global variables
        global elevator_loc
        global incalls
        global excalls_up
        global excalls_dn
        
        # Reset toggle buttons
        if 5 in incalls:
            self.cmdIncall5.SetValue(True)
        else:
            self.cmdIncall5.SetValue(False)
        if 4 in incalls:
            self.cmdIncall4.SetValue(True)
        else:
            self.cmdIncall4.SetValue(False)
        if 3 in incalls:
            self.cmdIncall3.SetValue(True)
        else:
            self.cmdIncall3.SetValue(False)
        if 2 in incalls:
            self.cmdIncall2.SetValue(True)
        else:
            self.cmdIncall2.SetValue(False)
        if 1 in incalls:
            self.cmdIncall1.SetValue(True)
        else:
            self.cmdIncall1.SetValue(False)
        if 5 in excalls_up:
            self.cmdExcall5Up.SetValue(True)
        else:
            self.cmdExcall5Up.SetValue(False)
        if 4 in excalls_up:
            self.cmdExcall4Up.SetValue(True)
        else:
            self.cmdExcall4Up.SetValue(False)
        if 3 in excalls_up:
            self.cmdExcall3Up.SetValue(True)
        else:
            self.cmdExcall3Up.SetValue(False)
        if 2 in excalls_up:
            self.cmdExcall2Up.SetValue(True)
        else:
            self.cmdExcall2Up.SetValue(False)
        if 1 in excalls_up:
            self.cmdExcall1Up.SetValue(True)
        else:
            self.cmdExcall1Up.SetValue(False)
        if 5 in excalls_dn:
            self.cmdExcall5Down.SetValue(True)
        else:
            self.cmdExcall5Down.SetValue(False)
        if 4 in excalls_dn:
            self.cmdExcall4Down.SetValue(True)
        else:
            self.cmdExcall4Down.SetValue(False)
        if 3 in excalls_dn:
            self.cmdExcall3Down.SetValue(True)
        else:
            self.cmdExcall3Down.SetValue(False)
        if 2 in excalls_dn:
            self.cmdExcall2Down.SetValue(True)
        else:
            self.cmdExcall2Down.SetValue(False)
        if 1 in excalls_dn:
            self.cmdExcall1Down.SetValue(True)
        else:
            self.cmdExcall1Down.SetValue(False)
    
    # Takes one step of the simulation
    def Step(self, event):
        
        # Get global variables
        global elevator_loc
        global elevator_dir
        global incalls
        global excalls_up
        global excalls_dn
        global doors
        global last_state
        
        # Advance the elevator one floor in the current direction
        # Also, create a reference to the appropriate list of external calls
        if elevator_dir == "UP":
            elevator_loc = elevator_loc+1
        elif elevator_dir == "DOWN":
            elevator_loc = elevator_loc-1
        
        # Control logic
        if self.NoCalls():
            elevator_dir == "HOLD"
        # Transitions from state "UP"
        elif elevator_dir == "UP" or (elevator_dir == "HOLD" and last_state == "UP"):
            if self.SIC() or self.SECU():
                elevator_dir = "HOLD"
                doors = "OPEN"
                if elevator_loc in incalls:
                    incalls.remove(elevator_loc)
                if elevator_loc in excalls_up:
                    excalls_up.remove(elevator_loc)
            elif self.SECD() and not (self.HIC() or self.HECU() or self.HECD()):
                elevator_dir = "HOLD"
                doors = "OPEN"
                last_state = "DOWN"
                if elevator_loc in excalls_dn:
                    excalls_dn.remove(elevator_loc)
            elif self.HIC() or self.HECU() or self.HECD():
                elevator_dir = "UP"
            elif self.LIC() or self.LECU() or self.LECD():
                elevator_dir = "DOWN"
        # Transitions from state "DOWN"
        elif elevator_dir == "DOWN" or (elevator_dir == "HOLD" and last_state == "DOWN"):
            if self.SIC() or self.SECD():
                elevator_dir = "HOLD"
                doors = "OPEN"
                if elevator_loc in incalls:
                    incalls.remove(elevator_loc)
                if elevator_loc in excalls_dn:
                    excalls_dn.remove(elevator_loc)
            elif self.SECU() and not (self.LIC() or self.LECU() or self.LECD()):
                elevator_dir = "HOLD"
                doors = "OPEN"
                last_state = "UP"
                if elevator_loc in excalls_up:
                    excalls_up.remove(elevator_loc)
            elif self.LIC() or self.LECU() or self.LECD():
                elevator_dir = "DOWN"
            elif self.HIC() or self.HECU() or self.HECD():
                elevator_dir = "UP"
        
        self.Update()
        
        # Reset doors to closed for the next step
        doors = "CLOSED"
    
    # Returns true if there are no calls to the elevator
    def NoCalls(self):
        
        # Get global variables
        global incalls
        global excalls_up
        global excalls_dn
        global doors
        
        # If there are no calls, return true
        if incalls == [] and excalls_up == [] and excalls_dn ==[]:
            return True
        else:
            return False
    
    # Returns true if there is a higher internal call
    def HIC(self):
        
        # Get global variables
        global elevator_loc
        global incalls
        
        for call in incalls:
            if call > elevator_loc:
                return True
        return False
    
    # Returns true if there is a lower internal call
    def LIC(self):
        
        # Get global variables
        global elevator_loc
        global incalls
        
        for call in incalls:
            if call < elevator_loc:
                return True
        return False
    
    #Returns true if there is an internal call for this floor
    def SIC(self):
        
        # Get global variables
        global elevator_loc
        global incalls
        
        for call in incalls:
            if call == elevator_loc:
                return True
        return False
    
    # Returns true if there is a higher external call going up
    def HECU(self):
        
        # Get global variables
        global elevator_loc
        global excalls_up
        
        for call in excalls_up:
            if call > elevator_loc:
                return True
        return False
    
    # Returns true if there is a lower external call going up
    def LECU(self):
        
        # Get global variables
        global elevator_loc
        global excalls_up
        
        for call in excalls_up:
            if call < elevator_loc:
                return True
        return False
    
    #Returns true if there is an external call on this floor going up
    def SECU(self):
        
        # Get global variables
        global elevator_loc
        global excalls_up
        
        for call in excalls_up:
            if call == elevator_loc:
                return True
        return False
    
    # Returns true if there is a higher external call going down
    def HECD(self):
        
        # Get global variables
        global elevator_loc
        global excalls_dn
        
        for call in excalls_dn:
            if call > elevator_loc:
                return True
        return False
    
    # Returns true if there is a lower external call going down
    def LECD(self):
        
        # Get global variables
        global elevator_loc
        global excalls_dn
        
        for call in excalls_dn:
            if call < elevator_loc:
                return True
        return False
    
    #Returns true if there is an external call on this floor going down
    def SECD(self):
        
        # Get global variables
        global elevator_loc
        global excalls_dn
        
        for call in excalls_dn:
            if call == elevator_loc:
                return True
        return False
    
# Declare the global values
global elevator_loc
global elevator_dir
global incalls
global excalls_up
global excalls_dn
global doors
global last_state

# Initialize globals
elevator_loc = 1
elevator_dir = "HOLD"
incalls = []
excalls_up = []
excalls_dn = []
doors = "CLOSED"
last_state = "UP"

# Start the GUI
app = wx.App()
main = Elevator(None, -1, 'Elevator Simulation')
app.MainLoop()