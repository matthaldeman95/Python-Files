import math

A0 = input('Amplitude: ')
amp = A0 * 0.37
print amp

f = input('Frequency: ')
t2 = float(input('Time 2 (ms): ')) / 1000
t1 = float(input('Time 1 (ms): ')) / 1000
q = (t2-t1) * f * 2 * math.pi
print("Quality factor: %s" % (q))


