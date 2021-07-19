from sympy import *


symbols_ =["a_"+str(i)+"_" for i in range(32)]
one = 0
def rotate(l, n):
	return l[n:] + l[:n]
def shift(l, n):
	return l[n:] + l[:n]
def getBit(i,n):
	return (bool(i&(1<<n)))
def getBitArray(i):
	l = []
	for x in range(32):
		l.append(getBit(i, x))
	return l
class BitArr(object):
	def __init__(self,initialize=True):
		if(initialize==True):
			global one,symbols
			one+=1
			vars_ = ",".join([symbol+str(one) for symbol in symbols_])
			self.args = list(symbols(vars_))
		else:
			self.args = list([0 for x in range(32)])
	def assign(self,args_c):
		self.args = args_c.copy()
	def __xor__(self,other):
		ret = BitArr(initialize=False)

		if(type(other)==BitArr):
			arrs = other.args[x]
		if(type(other)==int):
			arrs = getBitArray(other)

		for x in range(32):
			ret.args[x]=self.args[x]^arrs[x]
		return ret
	def __str__(self):
		return str(self.args[::-1])
	def L_ROTR(self,count):
		self.args = rotate(self.args, -count)
		return self
	def R_ROTR(self,count):
		self.args = rotate(self.args, count)
		return self
	def __lshift__(self,count):
		if(count ==0):
			ret.args = self.args
			return ret
		ret = BitArr(initialize=False)
		ret.args = rotate(self.args, -count)
		ret.args[:count] = [0 for x in range(count)]#(self.args[c])
		return ret
	def __rshift__(self,count):
		ret = BitArr(initialize=False)
		if(count ==0):
			ret.args = self.args
			return ret
		ret.args = rotate(self.args, count)
		ret.args[-count:] = [0 for x in range(count)]#(self.args[c])
		return ret
	def __len__(self):
		return len(self.args)
	def __add__(self,other):
		ret = BitArr(initialize=False)
		a = self.args
		if(type(other)==BitArr):
			b = other.args
		if(type(other)==int):
			b = getBitArray(other)
		carry = False
		for x in range(32):
			ret.args[x] = a[x]^b[x]^carry
			carry = (carry&(a[x]|b[x]))|(a[x]&b[x])#(c&(a|b))|(a&b)#int((a[x]&b[x])|(a[x]&carry)|(b[x]&carry))
		# return getI(c)
		# ret.args = c
		# if(carry): print("overflowed")
		return ret
