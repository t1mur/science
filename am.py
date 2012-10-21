class AMState:
	def __init__(self,total_j,projection_m):
		self.changeState(total_j,projection_m)


	def changeState(self, total_j, projection_m):
		if total_j<0 or abs(projection_m)>total_j:
			print 'Invalid J and m: J<0 or |m|>J. Created a zero state.'
			self.zeroState=True
		self.j=int(total_j*2)/2.0
		self.m=int(projection_m*2)/2.0
		self.zeroState=False
		if self.j % 1 != self.m % 1:
			print 'Invalid J and m: J,m must both be half integer, or both integer. \nCreated a zero state.'
			self.zeroState=True


test=AMState(3,0.5)
print test.j
print test.m
