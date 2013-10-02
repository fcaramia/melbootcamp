import sys

sent1 = sys.argv[1]
sent2 = sys.argv[2]

my_set1 = set(''.join(sent1).lower())
my_set2 = set(''.join(sent2).lower())


common = len(my_set1.intersection(my_set2))
print "Common:" , common
print "Unique to 1:", len(my_set1)-common
print "Unique to 2:", len(my_set2)-common
