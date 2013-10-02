import sys, string

params = sys.argv[1:]
my_set = set(''.join(params).lower())
print "Unique:" ,len(my_set)

