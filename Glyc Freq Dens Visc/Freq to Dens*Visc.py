import math
roq = 2.648                              #density of quartz = 2.648 g cm^-3
muq = 2.947E11                           #shear modulus of quartz = 2.947E11 g cm^-1 s^-2

harmonic = input('Harmonic Number:  ')        #Harmonic Number

dens = input('Known liquid density:  ')       #Dnsity g * cm^-3
f0 = input('Resonant Frequency (Hz):  ')      #Nominal crystal resonant frequency (Hz)
deltaf = input('Frequency Shift (Hz):  ')        #Change in frequency

f03 = float(f0**3)
df2 = float(deltaf**2)

ronu = ((df2/f03) / (harmonic)) * math.pi * 2.648 * 2.947E11
ronu = ronu*100 / dens
print ("Viscosity:  "),
print(ronu)







