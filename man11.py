class Test:
	h=0

	def _init_(self):
		self,h=7

	def my_func(self,k):
		print("hii,i am in the class")
		self.h=k #assigning the value to instance variable
		print(self.h)
o=Test()
print(o.h)
o.my_func(3)
o.my_func(5)