__author__ = 'liujunyuan'

print ("the lenthgh of sequence is: ")
n = input()
a = [0]*n
print 0
print 1
for i in range(2,n,1):
    a[1] = 1
    a[i] = a[i-1] + a[i-2]
    print a[i]