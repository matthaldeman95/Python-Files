import math
roq = 2.648                              #density of quartz = 2.648 g cm^-3
muq = 2.947E11                           #shear modulus of quartz = 2.947E11 g cm^-1 s^-2

#harmonic = input('Harmonic Number:  ')        #Harmonic Number
harmonic = 1

#f0 = input('Resonant Frequency (Hz):  ')      #Nominal crystal resonant frequency (Hz)
f0 = 4977600
rol = input('Sample density:  ')              #Liquid density
nul = input('Sample viscosity (cP):  ')       #Liquid viscosity in centiPoise
nul = nul/100                                 #1 cP = 1/100 g cm^-1 s^-1
            

deltaf = - harmonic**0.5 *  (f0**1.5) * (((nul * rol) / (math.pi * roq * muq)) ** 0.5)
print deltaf





