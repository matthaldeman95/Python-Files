from __future__ import division
import math

roq = 2.648                              #density of quartz = 2.648 g cm^-3
muq = 2.947E11                           #shear modulus of quartz = 2.947E11 g cm^-1 s^-2


#f0 = float(input('Resonant Frequency (Hz):  '))      #Nominal crystal resonant frequency (Hz)
f0 = 4977600
rol = input('Sample density:  ')              #Liquid density
nul = input('Sample viscosity (cP): ')        #Liquid viscosity in centiPoise
nul = nul/100                                 #1 cP = 1/100 g cm^-1 s^-1
#L = (input('Dry inductance (mH):  ')/1000)            #Inductance of crystal when dry (H)
L = .061

deltaR =  (2 * f0 * L) * ((4 * math.pi * f0 * nul * rol) / (roq * muq))**0.5
print deltaR



