import sys

nums = sys.argv[1:]

s = 0
for x in nums:
    s+= int(x)

print "Sum:", s
