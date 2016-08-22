from Tkinter import *
import tkFont


class InventoryWindow:
    def __init__(self, master, RW):
        n = 0
        self.master = master
        self.keys=[]
        self.keys = [[k] for k, v in sorted(inventory.iteritems())]
        for key in range(len(self.keys)/2):
            Label(master,text=self.keys[key][0]).grid(row=n,column=0,sticky=W)
            self.keys[key].append(Entry(master, width = 10))
            self.keys[key][1].grid(row=n,column=1)
            self.keys[key][1].insert(0, inventory[self.keys[key][0]])
            n += 1
        n = 0
        for key in range(len(self.keys)/2,len(self.keys)):
            Label(master, text=self.keys[key][0]).grid(row=n, column=2, sticky=W)
            self.keys[key].append(Entry(master,width=10))
            self.keys[key][1].grid(row=n, column=3)
            self.keys[key][1].insert(0, inventory[self.keys[key][0]])
            n += 1
        Label(master, text='Command Line: ').grid(row=n,column=0, sticky=W)
        self.textfield = Entry(master)
        self.textfield.grid(row=n,column=1,sticky=W)
        self.button = Button(
            master, text="Ok", fg='red',command=self.updateInventory
        )
        self.button.grid(row=n+1,column=1)
        master.bind('<Return>',self.returnKey)
        self.destbutton = Button(
            master, text='Close', fg='red', command=self.quitAll
        )
        self.destbutton.grid(row=n+1, column=2)

    def returnKey(self,event):
        if self.textfield.get():
            data = []
            data = self.textfield.get().strip().split(' ')

            if 'A'.lower() in data[0].lower() or 'R'.lower() in data[0].lower():
                for el in sorted(inventory.iteritems()):
                    if data[2].lower() in el[0].lower():
                        item = el[0]
                if 'A'.lower() in data[0].lower():
                    inventory[item] += int(data[1])
                elif 'R'.lower() in data[0].lower():
                    inventory[item] -= int(data[1])
                for key in range(len(self.keys)):
                    if item == self.keys[key][0]:
                        self.keys[key][1].delete(0, END)
                        self.keys[key][1].insert(0, inventory[item])
            elif 'B'.lower() in data[0]:
                for rec in Recipes:
                    if data[1].lower() in rec.name.lower():
                        if rec.canMake(inventory):
                            inventory[rec.name] += 1
                            for el in rec.elements:
                                inventory[el[0]] -= el[1]
                                for key in range(len(self.keys)):
                                    if el[0] == self.keys[key][0]:
                                        self.keys[key][1].delete(0, END)
                                        self.keys[key][1].insert(0, inventory[el[0]])
            elif 'P'.lower() in data[0]:
                stri = ""
                for words in range(1,len(data)):
                    stri += data[words]
                    stri += " "
                for rec in Recipes:
                    if stri.lower().strip() in rec.name.lower():
                        rec.pinned = not rec.pinned

        for key in range(len(self.keys)):
            self.keys[key][1].delete(0, END)
            self.keys[key][1].insert(0, inventory[self.keys[key][0]])
        self.textfield.delete(0, END)
        self.updateInventory()
        RecipeWindow.refresh(RW)

    def updateInventory(self):
        for key in range(len(self.keys)):
            inventory[self.keys[key][0]] = int(self.keys[key][1].get())

    def escapeKey(self,event):
        self.updateInventory()
        RecipeWindow.refresh(RW)

    def quitAll(self):
        self.master.quit()




class RecipeWindow(Frame):
    def __init__(self, master):
        self.master = master
        self.customFont = tkFont.Font(family="Helvetica", size=12)
        """
        self.tc = Checkbutton(self.frame, text='Technology Components', variable=self.techcomp, command=self.refresh)
        self.tc.select()

        self.es = Checkbutton(self.frame, text='Energy Sources', variable=self.energys, command=self.refresh)
        self.es.select()

        self.ex = Checkbutton(self.frame, text='Exosuit Upgrades', variable=self.exos, command=self.refresh)
        self.ex.select()

        self.sh = Checkbutton(self.frame, text='Ship Upgrades', variable=self.ship, command=self.refresh)
        self.sh.select()

        self.mt = Checkbutton(self.frame, text='Multi-tool Upgrades', variable=self.mult, command=self.refresh)
        self.mt.select()
        """
        self.spec = IntVar()
        self.technocompon = [r for r in TechnologyComponents]
        self.energysources = [r for r in EnergySources]
        self.techcomp = IntVar()
        self.energys = IntVar()

        self.exos = IntVar()
        self.exohealth = [r for r in Health]
        self.exoprot = [r for r in Protection]
        self.exostamina = [r for r in Stamina]
        self.exoutil = [r for r in Utilities]
        self.health = IntVar()
        self.protection = IntVar()
        self.stamina = IntVar()
        self.utilities = IntVar()

        self.ship = IntVar()
        self.weapons = [r for r in Weapons]
        self.weaponsvar = IntVar()
        self.shiphealth = [r for r in ShipHealth]
        self.shiphealthvar = IntVar()
        self.scan = [r for r in ShipScan]
        self.scanvar = IntVar()
        self.hyper = [r for r in Hyperdrive]
        self.hypervar = IntVar()

        self.multitool = IntVar()
        self.laser = [r for r in Laser]
        self.laservar = IntVar()
        self.proj = [r for r in Projectile]
        self.projvar = IntVar()
        self.grenade = [r for r in Grenade]
        self.grenadevar = IntVar()
        self.toolscan = [r for r in ToolScan]
        self.toolscanvar = IntVar()

        self.generate()



    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def refresh(self):
        self.frame.destroy()
        self.canvas.destroy()
        self.vsb.destroy()

        self.generate()

    def subgroupupdater(self, master, subgroup, n, name, var):
        if var:
            for item in range(len(subgroup)):
                c = 2
                i = subgroup[item]
                makerec = i.canMake(inventory)
                color = 'red'
                n += 1
                if makerec == True:
                    color = 'green'
                Label(self.frame, text=i.name, fg=color).grid(row=n, column=0, sticky=W)
                Label(self.frame, text='            ').grid(row=n, column=1, sticky=W)

                for el in range(len(i.elements)):
                    color = 'red'
                    make = i.canMakeInd(inventory, i.elements[el][0], el)
                    if make == True:
                        color = 'green'
                    string1 = i.elements[el][0] + ' : '
                    string2 = str(inventory[i.elements[el][0]]) + '/' + str(i.elements[el][1]) + '      '
                    Label(self.frame, text=string1, fg=color).grid(row=n, column=c, sticky=W)
                    Label(self.frame, text=string2, fg=color).grid(row=n, column=c + 1, sticky=W)
                    c += 2
        return n



    def update(self):
        Label(self.frame, text='Pinned Recipes', fg='blue', font=self.customFont).grid(row=0, column=0, sticky=W)
        n = 1
        for rec in Recipes:
            c = 2
            if rec.pinned == True:
                makerec = rec.canMake(inventory)
                color = 'red'
                if makerec == True:
                    color = 'green'
                Label(self.frame, text=rec.name, fg=color).grid(row=n, column=0, sticky=W)
                Label(self.frame, text='            ').grid(row=n, column=1, sticky=W)

                for el in range(len(rec.elements)):
                    color = 'red'
                    make = rec.canMakeInd(inventory, rec.elements[el][0], el)
                    if make == True:
                        color = 'green'
                    string1 = rec.elements[el][0] + ' : '
                    string2 = str(inventory[rec.elements[el][0]]) + '/' + str(rec.elements[el][1]) + '      '
                    Label(self.frame, text=string1, fg=color).grid(row=n, column=c, sticky=W)
                    Label(self.frame, text=string2, fg=color).grid(row=n, column=c + 1, sticky=W)
                    c += 2
                n += 1

        if self.spec.get():
            Label(self.frame, text='Special Parts', fg='blue', font=self.customFont).grid(row=n+2, column=0, sticky=W)
            Checkbutton(self.frame, text='Technology Components', variable=self.techcomp, command=self.refresh).grid(row=n+3, column=0,sticky=W)
            n = self.subgroupupdater(self.frame,self.technocompon, n+3, 'Technology Components', self.techcomp.get())
            Checkbutton(self.frame, text='Energy Sources', variable=self.energys, command=self.refresh).grid(row=n+1, column=0, sticky=W)
            n = self.subgroupupdater(self.frame,self.energysources, n+1, 'Energy Sources', self.energys.get())

        if self.exos.get():
            Label(self.frame, text='Exosuit Upgrades', fg='blue', font=self.customFont).grid(row=n+2, column=0, sticky=W)
            Checkbutton(self.frame, text='Health', variable = self.health, command = self.refresh).grid(row=n+3,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.exohealth, n+3, 'Health', self.health.get())
            Checkbutton(self.frame, text='Protection', variable = self.protection, command = self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.exoprot, n+1, 'Protection', self.protection.get())
            Checkbutton(self.frame, text='Stamina', variable = self.stamina, command = self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.exostamina, n+1, 'Stamina', self.stamina.get())
            Checkbutton(self.frame, text='Utilities', variable = self.utilities, command = self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.exoutil, n+1, 'Utilities', self.utilities.get())

        if self.ship.get():
            Label(self.frame, text='Ship Upgrades', fg='blue', font=self.customFont).grid(row=n+2, column=0, sticky=W)
            Checkbutton(self.frame, text='Weapons', variable=self.weaponsvar, command=self.refresh).grid(row=n+3,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.weapons, n+3, 'Weapons', self.weaponsvar.get())
            Checkbutton(self.frame, text='Health', variable=self.shiphealthvar, command=self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.shiphealth, n+1, 'Health', self.shiphealthvar.get())
            Checkbutton(self.frame, text='Scan', variable=self.scanvar, command=self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.scan, n+1, 'Scan', self.scanvar.get())
            Checkbutton(self.frame, text='Hyperdrive', variable=self.hypervar, command=self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.hyper, n+1, 'Hyperdrive', self.hypervar.get())

        if self.multitool.get():
            Label(self.frame, text='Multi-tool Upgrades', fg='blue', font=self.customFont).grid(row=n+2, column=0, sticky=W)
            Checkbutton(self.frame, text='Laser', variable=self.laservar, command=self.refresh).grid(row=n+3,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.laser, n+3, 'Laser', self.laservar.get())
            Checkbutton(self.frame, text='Projectile', variable=self.projvar, command=self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.proj, n+1, 'Projectile', self.projvar.get())
            Checkbutton(self.frame, text='Grenade', variable=self.grenadevar, command=self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.grenade, n+1, 'Grenade', self.grenadevar.get())
            Checkbutton(self.frame, text='Scan', variable=self.toolscanvar, command=self.refresh).grid(row=n+1,column=0, sticky=W)
            n = self.subgroupupdater(self.frame, self.toolscan, n+1, 'Scan', self.toolscanvar.get())

    def generate(self):
        Frame.__init__(self, self.master)

        self.canvas = Canvas(self.master, width=1000, height=600)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(self.master, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor='nw', tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.tc = Checkbutton(self.frame, text='Special Parts', variable=self.spec, command=self.refresh)
        #self.tc.select()

        self.es = Checkbutton(self.frame, text='Energy Sources', variable=self.energys, command=self.refresh)
        #self.es.select()

        self.ex = Checkbutton(self.frame, text='Exosuit Upgrades', variable=self.exos, command=self.refresh)
        #self.ex.select()

        self.sh = Checkbutton(self.frame, text='Ship Upgrades', variable=self.ship, command=self.refresh)
        #self.sh.select()

        self.mt = Checkbutton(self.frame, text='Multi-tool Upgrades', variable=self.multitool, command=self.refresh)
        #self.mt.select()

        self.tc.grid(row=0, column=10, sticky=W)
        #self.es.grid(row=1, column=10)
        self.ex.grid(row=2, column=10, sticky=W)
        self.sh.grid(row=3, column=10, sticky=W)
        self.mt.grid(row=4, column=10, sticky=W)

        self.update()


class Recipe:
    def __init__(self, name, element1, *args):
        self.name = name
        self.elements = [element1]
        self.pinned = False
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

    def build(self):
        if self.canMake(inventory):
            for el in range(len(self.elements)):
                element = self.elements[el][0]
                inventory['%s'%element] -= self.elements[el][1]


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
             'Shielding Shard': 0,
             'Shielding Plate': 0,
             'Power Gel': 0,
             'Power Canister': 0,
             'Unstable Plasma': 0,
             'Warp Cell': 0,
             'Gravitino Ball': 0,
             'Dimensional Matrix': 0,
             'Vortex Cube': 0,
             'Neutrino Module': 0,
             'AquaSphere': 0
             }

def getInventory():
    try:
        infile = open('inventory.csv')
        for line in infile:
            k, v = line.split(',')
            inventory[k] = int(v)
    finally:
        pass



ShieldboostSigma = Recipe('Shieldboost Sigma', ('Zinc', 15), ('Platinum', 15), ('Thamium9', 15))
ShieldboostTau = Recipe('Shieldboost Tau', ('Zinc', 100), ('Platinum', 100), ('Gold', 50))
ShieldboostTheta = Recipe('Shieldboost Theta', ('Chrysonite', 300), ('Microdensity Fabric', 2))
HealthSigma = Recipe('Health Sigma', ('Iron', 50), ('Plutonium', 50), ('Zinc', 10))
HealthTau = Recipe('Health Tau', ('Aluminium', 150), ('Carbon', 250), ('Thamium9', 50))
HealthTheta = Recipe('Health Theta', ('Aluminium', 200), ('Plutonium', 250), ('Thamium9', 300))

CoolantNetworkSigma = Recipe('Coolant Network Sigma', ('Iron', 50), ('Carbon', 100))
CoolantNetworkTau = Recipe('Coolant Network Tau', ('Zinc', 50), ('Carbon', 100), ('Microdensity Fabric', 1))
CoolantNetworkTheta = Recipe('Coolant Network Theta', ('Microdensity Fabric', 2), ('Electron Vapor', 1), ('Gravitino Ball', 1))
RadiationSigma = Recipe('Radiation Deflector Sigma', ('Iron', 50), ('Carbon', 100))
RadiationTau = Recipe('Radiation Deflector Tau', ('Zinc', 50), ('Carbon', 100), ('Microdensity Fabric', 1))
RadiationTheta = Recipe('Radiation Deflector Theta', ('Microdensity Fabric', 2), ('Electron Vapor', 1), ('Gravitino Ball', 1))
ThermicSigma = Recipe('Thermic Layer Sigma', ('Iron', 50), ('Carbon', 100))
ThermicTau = Recipe('Thermic Layer Tau', ('Zinc', 50), ('Carbon', 100), ('Microdensity Fabric', 1))
ThermicTheta = Recipe('Thermic Layer Theta', ('Microdensity Fabric', 2), ('Electron Vapor', 1), ('Gravitino Ball', 1))
ToxinSigma = Recipe('Toxin Suppressor Sigma', ('Iron', 50), ('Carbon', 100))
ToxinTau = Recipe('Toxin Suppressor Tau', ('Zinc', 50), ('Carbon', 100), ('Microdensity Fabric', 1))

AerationSigma = Recipe('Aeration Membrane Sigma', ('Iron', 50), ('Carbon', 100))
AerationTau = Recipe('Aeration Membrane Tau', ('Zinc', 50), ('Carbon', 100), ('Microdensity Fabric', 1))
AerationTheta = Recipe('Aeration Membrane Theta', ('Microdensity Fabric', 2), ('Electron Vapor', 1), ('Gravitino Ball', 1))
StaminaSigma = Recipe('Stamina Sigma', ('Iron', 20), ('Carbon', 20))
StaminaTau = Recipe('Stamina Tau', ('Iron', 100), ('Heridium', 150), ('Plutonium', 50))
StaminaTheta = Recipe('Stamina Theta', ('Zinc', 150), ('Heridium', 150), ('Plutonium', 50))

JetpackSigma = Recipe('Jetpack Booster Sigma', ('Carite Sheet', 1), ('Platinum', 15),('Zinc', 10))
JetpackTau = Recipe('Jetpack Booster Tau', ('Chrysonite', 150), ('Titanium', 150), ('Plutonium', 150))
JetpackTheta = Recipe('Jetpack Booster Theta', ('Omegon', 50), ('Chrysonite', 300), ('Plutonium', 300))
LifeSupportSigma = Recipe('Life Support Sigma', ('Plutonium', 50), ('Platinum', 20))
LifeSupportTau = Recipe('Life Support Tau', ('Plutonium', 50), ('Platinum', 150))



Health = [HealthSigma, HealthTau, HealthTheta, ShieldboostSigma, ShieldboostTau, ShieldboostTheta]
Protection = [CoolantNetworkSigma, CoolantNetworkTau, CoolantNetworkTheta,RadiationSigma, RadiationTau, RadiationTheta,
              ThermicSigma, ThermicTau, ThermicTheta, ToxinSigma, ToxinTau]
Stamina = [AerationSigma, AerationTau, AerationTheta, StaminaSigma, StaminaTau, StaminaTheta]
Utilities = [JetpackSigma, JetpackTau, JetpackTheta, LifeSupportSigma, LifeSupportTau]
Exosuit = [Health, Protection, Stamina, Utilities]



AcceleratedFireSigma = Recipe('Accelerated Fire Sigma', ('Iron', 50), ('Aluminium', 100))
AcceleratedFireTau = Recipe('Accelerated Fire Tau', ('Nickel', 100), ('Platinum', 100))
AcceleratedFireTheta = Recipe('Accelerated Fire Theta', ('Thamium9', 300), ('Iron', 300), ('Dimensional Matrix', 3))
AdvancedCoolingSigma = Recipe('Advanced Cooling Sigma', ('Thamium9', 30), ('Chrysonite', 30), ('Iron', 50))
AdvancedCoolingTau = Recipe('Advanced Cooling Tau', ('Thamium9', 80), ('Chrysonite', 70), ('Iridium', 120))
AdvancedCoolingTheta = Recipe('Advanced Cooling Theta', ('Thamium9', 200), ('Chrysonite', 250), ('Gravitino Ball', 10))
BeamImpactSigma = Recipe('Beam Impact Sigma', ('Thamium9', 50), ('Chrysonite', 50))
BeamImpactTau = Recipe('Beam Impact Tau', ('Thamium9', 200), ('Copper', 50), ('Carbon', 50))
BeamImpactTheta = Recipe('Beam Impact Theta', ('Omegon', 100), ('Vortex Cube', 3), ('Carbon', 50))
CannonDamageSigma = Recipe('Cannon Damage Sigma', ('Iron', 50), ('Thamium9', 50))
CannonDamageTau = Recipe('Cannon Damage Tau', ('Iridium', 100), ('Copper', 50), ('Zinc', 50))
CannonDamageTheta = Recipe('Cannon Damage Theta', ('Omegon', 100), ('Gold', 50), ('Zinc', 50))
PhaseBeam = Recipe('Phase Beam', ('Iron', 30), ('Heridium', 30), ('Thamium9', 30))
PhaseCoolantSigma = Recipe('Phase Coolant Sigma', ('Microdensity Fabric', 2), ('Thamium9', 200), ('Platinum', 25))
PhaseCoolantTau = Recipe('Phase Coolant Tau', ('Heridium', 150), ('Thamium9', 200), ('Platinum', 50))
PhaseCoolantTheta = Recipe('Phase Coolant Theta', ('Dimensional Matrix', 1), ('Thamium9', 200), ('Copper', 200))

DeflectionEnhancementSigma = Recipe('Deflection Enhancement Sigma', ('Carite Sheet', 6), ('Heridium', 500))
DeflectionEnhancementTau = Recipe('Deflection Enhancement Tau', ('Titanium', 200), ('Heridium', 250), ('Iron', 300))
DeflectionEnhancementTheta = Recipe('Deflection Enhancement Theta', ('Zinc', 300), ('Platinum', 80), ('Emeril', 200))

PhotonixCore = Recipe('Photonix Core', ('Chrysonite', 100), ('Iron', 200), ('Zinc', 50))
PulseJetTau = Recipe('Pulse Jet Tau', ('Nickel', 100), ('Thamium9', 50), ('Neutrino Module', 2))
PulseJetSigma = Recipe('Pulse Jet Sigma', ('Chrysonite', 100), ('Iron', 200), ('Zinc', 50))
WarpReactorSigma = Recipe('Warp Reactor Sigma', ('Dynamic Resonator', 1), ('Iridium', 200), ('Copper', 400))
WarpReactorTau = Recipe('Warp Reactor Tau', ('Dynamic Resonator', 2), ('Nickel', 600), ('Aluminium', 800))
WarpReactorTheta = Recipe('Warp Reactor Theta', ('Dynamic Resonator', 3), ('Gold', 1000), ('Emeril', 1000))


Weapons = [AcceleratedFireTau, AcceleratedFireSigma, AcceleratedFireTheta, AdvancedCoolingSigma, AdvancedCoolingTau,
           AdvancedCoolingTheta, BeamImpactSigma, BeamImpactTau, BeamImpactTheta,CannonDamageSigma, CannonDamageTau,
           CannonDamageTheta, PhaseBeam, PhaseCoolantSigma, PhaseCoolantTau, PhaseCoolantTheta]

ShipHealth = [DeflectionEnhancementSigma, DeflectionEnhancementTau, DeflectionEnhancementTheta]
ShipScan = []
Hyperdrive = [PulseJetTau, PulseJetSigma, WarpReactorSigma, WarpReactorTau, WarpReactorSigma, PhotonixCore]

Ship = [Weapons, ShipHealth, ShipScan, Hyperdrive]

BeamCoolantSigma = Recipe('Beam Coolant Sigma', ('Iridium', 50), ('Heridium', 20))
BeamCoolantTau = Recipe('Beam Coolant Tau', ('Iridium', 200), ('Heridium', 100))
BeamCoolantTheta = Recipe('Beam Coolant Theta', ('Aluminium', 200), ('Heridium', 100))
BeamFocusSigma = Recipe('Beam Focus Sigma', ('Iron', 20), ('Heridium', 20), ('Plutonium', 25))
BeamFocusTau = Recipe('Beam Focus Tau', ('Plutonium', 50), ('Chrysonite', 100))
BeamFocusTheta = Recipe('Beam Focus Theta', ('Plutonium', 50), ('Chrysonite', 200), ('Platinum', 200))
BeamIntensifierSigma = Recipe('Beam Intensifier Sigma', ('Titanium', 30), ('Plutonium', 25))
BeamIntensifierTau = Recipe('Beam Intensifier Tau', ('Copper', 60), ('Iron', 200))
BeamIntensifierTheta = Recipe('Beam Intensifier Theta', ('Copper', 120), ('Iron', 100), ('Iridium', 100))
#BeamIntensifierTheta = Recipe('Beam Intensifier Theta', ('Copper', 120), ('Iron', 100), 'Iridium', 100)
CombatAmpSigma = Recipe('Combat Amplifier Sigma', ('Titanium', 30), ('Carbon', 30))
CombatAmpTau = Recipe('Combat Amplifier Tau', ('Platinum', 200), ('Titanium', 50), ('Chrysonite', 50))
CombatAmpTheta = Recipe('Combat Amplifier Theta', ('Heridium', 400), ('Iron', 200), ('Radnox', 20))
CombatAmpOmega = Recipe('Combat Amplifier Omega', ('Heridium', 400), ('Iron', 200), ('Gold', 100))
Railshot = Recipe('Railshot Adapter', ('Aluminium', 100), ('Copper', 50), ('Iron', 200))

Boltcaster = Recipe('Boltcaster', ('Iron', 25), ('Plutonium', 25))
BoltcasterClipSigma = Recipe('Boltcaster ClipSigma', ('Plutonium', 50), ('Titanium', 20), ('Microdensity Fabric', 2))
BoltcasterSM = Recipe('Boltcaster SM', ('Iridium', 50), ('Iron', 50), ('Platinum', 100))
Homingbolt = Recipe('Homingbolt Adapter', ('AquaSphere', 5), ('Titanium', 200), ('Plutonium', 200))
ImpactDamageSigma = Recipe('Impact Damage Sigma', ('Iridium', 50), ('Iron', 50), ('Platinum', 100))
ImpactDamageTau = Recipe('Impact Damage Tau', ('Iridium', 50), ('Iron', 50), ('Platinum', 100))
ImpactDamageTheta = Recipe('Impact Damage Theta', ('Iridium', 200), ('Radnox', 80), ('Platinum', 200))
ImpactDamageOmega = Recipe('Impact Damage Omega', ('Copper', 200), ('Aluminium', 200), ('Heridium', 400))
PlasmaClipSigma = Recipe('Plasma Clip Sigma', ('Plutonium', 50), ('Titanium', 20), ('Microdensity Fabric', 2))
PlasmaClipTau = Recipe('Plasma Clip Tau', ('Plutonium', 50), ('Zinc', 20), ('Nickel', 10))
PlasmaClipTheta = Recipe('Plasma Clip Theta', ('Plutonium', 50), ('Zinc', 50), ('Nickel', 150))
RapidfireSigma = Recipe('Rapidfire Sigma', ('Nickel', 50), ('Iron', 20))
RapidfireTau = Recipe('Rapidfire Tau', ('Titanium', 200), ('Platinum', 100), ('Aluminium', 100))
RapidfireTheta = Recipe('Rapidfire Theta', ('Aluminium', 100), ('Platinum', 200))
RecoilSigma = Recipe('Recoil Stabilizer Sigma', ('Thamium9', 100), ('Titanium', 50), ('Chrysonite', 50))
RecoilTau = Recipe('Recoil Stabilizer Tau', ('Thamium9', 200), ('Titanium', 100), ('Chrysonite', 150))
RecoilTheta = Recipe('Recoil Stabilizer Theta', ('Heridium', 250), ('Zinc', 100), ('Platinum', 150))
ReloadSigma = Recipe('Reload Accelerant Sigma', ('Iron', 20), ('Heridium', 15), ('Zinc', 10))
ReloadTau = Recipe('Reload Accelerant Tau', ('Chrysonite', 50), ('Zinc', 100), ('Plutonium', 50))
ReloadTheta = Recipe('Reload Accelerant Theta', ('Calium', 50), ('Zinc', 100), ('Plutonium', 50))
RicochetSigma = Recipe('Ricochet Sigma', ('Platinum', 100), ('Iron', 200), ('Heridium', 200))
RicochetTau = Recipe('Ricochet Tau', ('Platinum', 300), ('Zinc', 150), ('Microdensity Fabric', 1))
RicochetTheta = Recipe('Ricochet Theta', ('Gold', 100), ('Plutonium', 100), ('Platinum', 100))
Shortburst = Recipe('Shortburst Adapter', ('Copper', 60), ('Heridium', 100), ('Zinc', 20))
Wideshot = Recipe('Wideshot Adapter', ('Copper', 40), ('Heridium', 100), ('Iron', 50))

PlasmaLauncher = Recipe('Plasma Launcher', ('Plutonium', 30), ('Heridium', 20), ('Carbon', 15))
DamageRadius = Recipe('Damage Radius', ('Zinc', 100), ('Iron', 50), ('Chrysonite', 150))
DamageRadiusTau = Recipe('Damage Radius Tau', ('Plutonium', 200), ('Emeril', 50))
Homing = Recipe('Homing', ('Aluminium', 100), ('Iron', 50), ('Gold', 100))
IntensitySigma = Recipe('Intensity Sigma', ('Thamium9', 150), ('Zinc', 20), ('Heridium', 200))
IntensityTau = Recipe('Intensity Tau', ('Iron', 200), ('Aluminium', 200), ('Nickel', 200))
IntensityTheta = Recipe('Intensity Theta', ('Neutrino Module', 4), ('Aluminium', 200), ('Nickel', 200))
Propulsion = Recipe('Propulsion', ('Zinc', 10), ('Platinum', 20), ('Chrysonite', 15))
PropulsionTau = Recipe('Propulsion Tau', ('Thamium9', 150), ('Zinc', 20), ('Chrysonite', 150))
Rebound = Recipe('Rebound', ('Zinc', 10), ('Platinum', 20), ('Chrysonite', 15))
ReboundTau = Recipe('Rebound Tau', ('Heridium', 200), ('Titanium', 200), ('Chrysonite', 250))
RangeBoostSigma = Recipe('RangeBoost Sigma', ('Thamium9', 30), ('Platinum', 15), ('Carbon', 30))
RangeBoostTau = Recipe('RangeBoost Tau', ('Thamium9', 120), ('Chrysonite', 120), ('Plutonium', 200))

AnalysisVisor = Recipe('Analysis Visor', ('Iron', 50))
Scanner = Recipe('Scanner', ('Carbon', 50))
ScanRangeBoostSigma = Recipe('RangeBoost Sigma', ('Thamium9', 30), ('Platinum', 15), ('Carbon', 30))
ScanRangeBoostTau = Recipe('RangeBoost Tau', ('Thamium9', 120), ('Chrysonite', 120), ('Plutonium', 200))

Laser = [BeamCoolantSigma, BeamCoolantTau, BeamCoolantTheta,BeamFocusSigma, BeamFocusTau, BeamFocusTheta, BeamIntensifierSigma,
         BeamIntensifierTau, BeamIntensifierTheta, CombatAmpSigma, CombatAmpTau, CombatAmpTheta, CombatAmpOmega, Railshot]
Projectile = [Boltcaster, BoltcasterClipSigma, BoltcasterSM, Homingbolt, ImpactDamageSigma, ImpactDamageTau, ImpactDamageTheta,
              ImpactDamageOmega, PlasmaClipSigma, PlasmaClipTau, PlasmaClipTheta, RapidfireSigma, RapidfireTau, RapidfireTheta,
              RecoilSigma, RecoilTau, RecoilTheta,ReloadSigma, ReloadTau, ReloadTheta,RicochetSigma, RicochetTau, RicochetTheta,
              Shortburst, Wideshot]
Grenade = [PlasmaLauncher, DamageRadius, DamageRadiusTau, Homing, IntensitySigma, IntensityTau, IntensityTheta,
           Propulsion, PropulsionTau, Rebound, ReboundTau, RangeBoostSigma, RangeBoostTau]
ToolScan = [AnalysisVisor, Scanner, ScanRangeBoostSigma, ScanRangeBoostTau]

Multitool = [Laser, Projectile, Grenade, ToolScan]

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

Special = [TechnologyComponents, EnergySources]

Recipes = [HealthSigma, HealthTau, HealthTheta, ShieldboostSigma, ShieldboostTau,
           ShieldboostTheta, CoolantNetworkSigma, CoolantNetworkTau, CoolantNetworkTheta,
           RadiationSigma, RadiationTau, RadiationTheta, ThermicSigma, ThermicTau,
           ThermicTheta, ToxinSigma, ToxinTau, AerationSigma, AerationTau, AerationTheta,
           StaminaSigma, StaminaTau, StaminaTheta, JetpackSigma, JetpackTau, JetpackTheta,
           LifeSupportSigma, LifeSupportTau, AcceleratedFireTau, AcceleratedFireSigma,
           AcceleratedFireTheta, AdvancedCoolingSigma, AdvancedCoolingTau,
           AdvancedCoolingTheta, BeamImpactSigma, BeamImpactTau, BeamImpactTheta,
           CannonDamageSigma, CannonDamageTau, CannonDamageTheta, PhaseBeam,
           PhaseCoolantSigma, PhaseCoolantTau, PhaseCoolantTheta, DeflectionEnhancementSigma,
           DeflectionEnhancementTau, DeflectionEnhancementTheta, PulseJetTau,
           PulseJetSigma, WarpReactorSigma, WarpReactorTau, WarpReactorSigma, PhotonixCore,
           BeamCoolantSigma, BeamCoolantTau, BeamCoolantTheta,BeamFocusSigma, BeamFocusTau,
           BeamFocusTheta, BeamIntensifierSigma, BeamIntensifierTau, BeamIntensifierTheta,
           CombatAmpSigma, CombatAmpTau, CombatAmpTheta, CombatAmpOmega, Railshot, Boltcaster,
           BoltcasterClipSigma, BoltcasterSM, Homingbolt, ImpactDamageSigma, ImpactDamageTau,
           ImpactDamageTheta, ImpactDamageOmega, PlasmaClipSigma, PlasmaClipTau,
           PlasmaClipTheta, RapidfireSigma, RapidfireTau, RapidfireTheta, RecoilSigma,
           RecoilTau, RecoilTheta,ReloadSigma, ReloadTau, ReloadTheta,RicochetSigma,
           RicochetTau, RicochetTheta, Shortburst, Wideshot, PlasmaLauncher, DamageRadius,
           DamageRadiusTau, Homing, IntensitySigma, IntensityTau, IntensityTheta,
           Propulsion, PropulsionTau, Rebound, ReboundTau, RangeBoostSigma, RangeBoostTau,
           AnalysisVisor, Scanner, ScanRangeBoostSigma, ScanRangeBoostTau, CariteSheet,
           MicrodensityFabric, ElectronVapor,SuspensionFluid, Antimatter, DynamicResonator,
           ShieldingShard, ShieldingPlate, PowerGel, PowerCanister, UnstablePlasma, WarpCell]




getInventory()
root = Tk()
RW = RecipeWindow(root)
IW = InventoryWindow(Tk(), RW)
root.mainloop()
outfile = open('inventory.csv', 'w')
print "Saving inventory..."
for k, v in sorted(inventory.iteritems()):
    outfile.write('%s, %d\n'%(k,v))
outfile.close()
root.destroy()
