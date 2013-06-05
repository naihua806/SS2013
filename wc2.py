import sys
f = sys.stdins = f.read()
f.close()

words = s.split()

d = {}for w in words:
if d.has_key(w):
d[w] += 1
else:
d[w] = 1sored_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)

print "all: %d" % len(d)i = 0
for k in sored_keys:    
if i == 20:        
break    
print k, ": ", d[k]    
i += 1
