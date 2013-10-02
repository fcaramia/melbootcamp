import sys

num = int(sys.argv[1])

if num<50 and num > 0:
    print "Minor"
elif num>=50 and num < 1000 :
    print "Major"
else:
    print "Severe"
