
# 1 1 1  1 1
# 1 0 1  0
# 0 0 1  1
# 0 0 0  0
# 1 0 0  1
# def addBinary(a,b):
#     carry = 0
#     for i in range(32):
#         s = a[i]+b[i]+carry
#         c[i] = s%2

# function addBinary(a: number[], b: number[]): number[]{
#     const c = [];
#     let carry = 0;
#     let i = 0;
#     for (i = 0; i < a.length; i += 1){
#         let s = a[i] + b[i] + carry;
#         c[i] = s % 2; 
#         carry = ~~(s / 2);
#     }
#     c[i] = carry;
#  return c;
# }
def getBit(i,n):
    return (bool(i&(1<<n)))
def getBitArray(i):
    l = []
    for x in range(32):
        l.append(getBit(i, x))
    return l
def getI(l):
    ret = 0
    a = 1
    for x in l:
        ret += a*x
        a = a<<1
    return ret
def add(a,b):
    a = getBitArray(a)
    b = getBitArray(b)
    c = [0 for x in range(32)]
    carry = 0
    for x in range(32):
        c[x] = int(a[x]^b[x]^carry)
        carry = int((carry&(a[x]|b[x]))|(a[x]&b[x]))
    return getI(c)
print(add(2,3))
# quit()
for x in range(100):
    for y in range(100):
        if(add(x,y)!=(x+y)):
            print("ntrue",x,y)