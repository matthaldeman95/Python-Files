from Tkinter import *
import tkFont

class InventoryWindow:
    def __init__(self, master, RW):
        n = 0
        self.keys=[]
        self.keys = [[k] for k, v in sorted(inventory.iteritems())]
        for key in range(len(self.keys)/2):
            Label(master,text=self.keys[key][0]).grid(row=n,column=0,sticky=W)
            self.keys[key].append(Entry(master))
            self.keys[key][1].grid(row=n,column=1)
            self.keys[key][1].insert(0, inventory[self.keys[key][0]])
            n += 1
        n = 0
        for key in range(len(self.keys)/2,len(self.keys)):
            Label(master, text=self.keys[key][0]).grid(row=n, column=2, sticky=W)
            self.keys[key].append(Entry(master))
            self.keys[key][1].grid(row=n, column=3)
            self.keys[key][1].insert(0, inventory[self.keys[key][0]])
            n += 1
        Label(master, text='Add/Remove Entry: ').grid(row=n,column=0, sticky=W)
        self.textfield = Entry(master)
        self.textfield.grid(row=n,column=1,sticky=W)
        self.button = Button(
            master, text="Ok", fg='red',command=self.updateInventory
        )
        self.button.grid(row=n+1,column=1)
        master.bind('<Return>',self.returnKey)
        #master.bind('<Escape>',self.escapeKey)

    def returnKey(self,event):
        if self.textfield.get():
            instruction, quantity, item = self.textfield.get().strip().split(' ')
            self.textfield.delete(0, END)
            for el in sorted(inventory.iteritems()):
                if item.lower() in el[0].lower():
                    item = el[0]
            if 'A'.lower() in instruction.lower():
                inventory[item] += int(quantity)
            elif 'R'.lower() in instruction.lower():
                print "removing"
                inventory[item] -= int(quantity)
            for key in range(len(self.keys)):
                if item == self.keys[key][0]:
                    self.keys[key][1].delete(0,END)
                    self.keys[key][1].insert(0,inventory[item])
        self.updateInventory()
        RecipeWindow.refresh(RW)

    def updateInventory(self):
        for key in range(len(self.keys)):
            inventory[self.keys[key][0]] = int(self.keys[key][1].get())

    def escapeKey(self,event):
        self.updateInventory()
        RecipeWindow.refresh(RW)



class RecipeWindow:
    def __init__(self, master):
        self.master = master
        self.customFont = tkFont.Font(family="Helvetica", size=12)
        self.frame=Frame(master,width=700,height=600)
        self.frame.grid()



        self.technologycomponents = [r for r in TechnologyComponents]
        self.techcomp = IntVar()
        tc = Checkbutton(self.frame, text='Technology Components', variable = self.techcomp, command=self.refresh)
        tc.grid(row=0,column=10)
        tc.select()

        self.energysources = [r for r in EnergySources]
        self.energys = IntVar()
        es = Checkbutton(self.frame, text='Energy Sources', variable=self.energys, command=self.refresh)
        es.grid(row=1,column=10)
        es.select()

        self.exosuit = [r for r in Exosuit]
        self.exos = IntVar()
        ex = Checkbutton(self.frame, text='Exosuit Upgrades', variable=self.exos, command=self.refresh)
        ex.grid(row=2,column=10)
        ex.select()

        self.shipups = [r for r in Ship]
        self.ship = IntVar()
        sh = Checkbutton(self.frame, text='Ship Upgrades', variable=self.ship, command=self.refresh)
        sh.grid(row=3, column=10)
        sh.select()

        self.multitool = [r for r in Multitool]
        self.mult = IntVar()
        mt = Checkbutton(self.frame, text='Multi-tool Upgrades', variable=self.mult, command=self.refresh)
        mt.grid(row=4,column=10)
        mt.select()

        self.update()

    def refresh(self):
        self.frame.destroy()
        self.update()




    def updater(self, master, group, n):
        for rec in range(len(group)):
            c = 2
            makerec = group[rec].canMake(inventory)
            color = 'red'
            if makerec == True:
                color = 'green'
            #buttons = {}
            Label(self.frame, text=group[rec].name, fg=color).grid(row=n, column=0, sticky=W)
            Label(self.frame, text='            ').grid(row=n, column=1, sticky=W)
            #buttons['%s'%group[rec].name] = (Button(self.frame, text='Make', command=lambda: self.make(group[rec].name)).grid(row=n, column=10))
            for el in range(len(group[rec].elements)):
                color = 'red'
                make = group[rec].canMakeInd(inventory, group[rec].elements[el][0], el)
                if make == True:
                    color = 'green'
                string1 = group[rec].elements[el][0] + ' : '
                string2 = str(inventory[group[rec].elements[el][0]]) + '/' + str(group[rec].elements[el][1]) + '      '
                Label(self.frame, text=string1, fg=color).grid(row=n, column=c, sticky=W)
                Label(self.frame, text=string2, fg=color).grid(row=n, column=c + 1, sticky=W)
                c += 2
            n += 1
        return n

    def update(self):
        n = 0
        self.frame = Frame(self.master)
        s = Scrollbar(self.frame).grid(row=0,column=15)
        self.frame.grid()
        if self.techcomp.get():
            Label(self.frame, text='Technology Components', fg='blue', font=self.customFont).grid(row=n, column=0, sticky=W)
            n = self.updater(self.frame,self.technologycomponents, n+1)

        if self.energys.get():
            Label(self.frame, text='Energy Sources', fg='blue', font=self.customFont).grid(row=n, column=0, sticky=W)
            n = self.updater(self.frame,self.energysources, n+1)

        if self.exos.get():
            Label(self.frame, text='Exosuit Upgrades', fg='blue', font=self.customFont).grid(row=n, column=0, sticky=W)
            n = self.updater(self.frame, self.exosuit, n + 1)

        if self.ship.get():
            Label(self.frame, text='Ship Upgrades', fg='blue', font=self.customFont).grid(row=n, column=0, sticky=W)
            n = self.updater(self.frame, self.shipups, n + 1)

        if self.mult.get():
            Label(self.frame, text='Multi-tool Upgrades', fg='blue', font=self.customFont).grid(row=n, column=0, sticky=W)
            n = self.updater(self.frame, self.multitool, n + 1)

    def make(self, element):
        print "Creating", element

class Recipe:
    def __init__(self, name, element1, *args):
        self.name = name
        self.elements = [element1]
        for arg in args:
            self.elements.append(arg)

    def canMake(self,inventory):
        for el in range(len(self.elements)):
            element = self.elements[el][0]
            if inventory['%s'%element] < self.elements[el][1]:
                return False
        return True

    def canMakeInd(self,inventory,element,el):
        if inventory[element] < self.elements[el][1]:
            return False
        else:
            return True
        return

inventory = {'Iron': 0,
             'Zinc': 0,
             'Titanium': 0,
             'Heridium': 0,
             'Platinum': 0,
             'Chrysonite': 0,
             'Carbon': 0,
             'Thamium9': 0,
             'Plutonium': 0,
             'Nickel': 0,
             'Iridium': 0,
             'Copper': 0,
             'Gold': 0,
             'Aluminium': 0,
             'Emeril': 0,
             'Omegon': 0,
             'Radnox': 0,
             'Murrine': 0,
             'Calium': 0,
             'Carite Sheet': 0,
             'Microdensity Fabric': 0,
             'Electron Vapor': 0,
             'Suspension Fluid': 0,
             'Antimatter': 0,
             'Dynamic Resonator': 0,
             'Night Crystals': 0,
             'Shielding Shard': 0,
             'Shielding Plate': 0,
             'Power Gel': 0,
             'Power Canister': 0,
             'Unstable Plasma': 0,
             'Warp Cell': 0,
             "Vy'keen Effigy": 0,
             'Korvax Convergence Cube': 0,
             'Korvax Casing': 0,
             'Gravitino Ball': 0,
             'Albumen Pearl': 0,
             }


CariteSheet = Recipe('Carite Sheet',('Iron',50))
MicrodensityFabric = Recipe('Microdensity Fabric', ('Iron', 50), ('Platinum', 10))
ElectronVapor = Recipe('Electron Vapor', ('Suspension Fluid', 1), ('Plutonium', 100))
SuspensionFluid = Recipe('Suspension Fluid', ('Carbon', 50))
Antimatter = Recipe('Antimatter', ('Electron Vapor', 1), ('Heridium', 50), ('Zinc', 20))
DynamicResonator = Recipe('Dynamic Resonator', ('Antimatter', 2), ('Chrysonite', 100), ('Microdensity Fabric',4))

TechnologyComponents = [CariteSheet, MicrodensityFabric, ElectronVapor,SuspensionFluid,
           Antimatter, DynamicResonator]

ShieldingShard = Recipe('Shielding Shard', ('Iron', 25))
ShieldingPlate = Recipe('Shielding Plate', ('Iron', 50))
PowerGel = Recipe('Power Gel', ('Carbon', 25))
PowerCanister = Recipe('Power Canister', ('Carbon', 50))
UnstablePlasma = Recipe('Unstable Plasma', ('Thamium9', 400), ('Plutonium', 200))
WarpCell = Recipe('Warp Cell', ('Thamium9', 100), ('Antimatter', 1))

EnergySources = [ShieldingShard, ShieldingPlate, PowerGel, PowerCanister,
                 UnstablePlasma, WarpCell]

HealthSigma = Recipe('Health Sigma', ('Iron', 50), ('Plutonium', 50), ('Zinc', 10))
HealthTau = Recipe('Health Tau', ('Aluminium', 150), ('Carbon', 250), ('Thamium9', 50))
HealthTheta = Recipe('Health Theta', ('Aluminium', 200), ('Plutonium', 250), ('Thamium9', 300))

Exosuit = [HealthSigma, HealthTau, HealthTheta]

Ship = []

Multitool = []



root = Tk()
RW = RecipeWindow(root)

IW = InventoryWindow(Tk(), RW)
root.mainloop()

root.destroy()






