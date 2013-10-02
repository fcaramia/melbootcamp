import sys

params = sys.argv[1:]
params.sort()
par2 = [x[0].upper() + x[1:] for x in params]
ret = ', '.join(par2[:-1]) + ' and '+ par2[-1]

print ret

