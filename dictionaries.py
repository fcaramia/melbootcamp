import sys

seq = sys.argv[1].upper()

valid = 'TCGAU'

my_dict = {x: seq.count(x) for x in seq if x in valid}

my_len = 0
for x in my_dict.keys():
    my_len += my_dict[x]
    print x, my_dict[x] 
    

print 'GC content' , my_dict['G']+my_dict['C']/float(my_len)
