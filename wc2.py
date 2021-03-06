import sys

argc = len(sys.argv) 
if argc == 1:     
  f = sys.stdin
elif argc == 2:    
    try:
      f = open(sys.argv[1], "rU")
      s = f.read()
      f.close()
    except IOError:        
      print >>sys.stderr, "wc: %s: No such file or directory" % (sys.argv[1])        
      sys.exit()
else:    
    print >>sys.stderr, "usage: python wc.py [filename]"    
    sys.exit()
words = s.split()
d = {}
for w in words:
  if d.has_key(w):
    d[w] += 1
  else:
    d[w] = 1
      
sored_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)
print "all: %d" % len(d)

i = 0
for k in sored_keys:
  if i == 20:
  break
  print k, ": ", d[k]
  i += 1
