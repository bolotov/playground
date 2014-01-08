def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

fle = open('E:\Sasha\cow_fix.pgm', 'r')
version = int(fle.readline().split('P')[1])
w,h = (int(i) for i in fle.readline().split())
colors = int(fle.readline().split()[0])
# ValueError exception may happen

print version
print w, h
print colors

cow = fle.readline()
print cow
for i in chunks(cow, w):
    pass
   # print i
   # print '\n'
