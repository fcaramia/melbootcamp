from rodents import Rodent

rodents= {}
f = open('rodent.csv')
for l in f:
    t,w = l.rstrip().split(',')
    if t in rodents:
        rodents[t].add_weight(float(w))
    else:
        n = Rodent(t)
        n.add_weight(float(w))
        rodents[t] = n




print "No rodents" , len(rodents)

for r in rodents:
    print r , rodents[r].weights
