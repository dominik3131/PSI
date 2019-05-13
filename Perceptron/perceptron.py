import random
class Perceptron:
	def __init__(self,no_ages):
		self.w1 = random.uniform(0, 1)
		self.w2= random.uniform(0, 1)
		self.b=random.uniform(0, 1)
		self.ages = no_ages
	def init(self,points):
		self.data=[]
		self.t=[]
	def setData(self,dataTab,tTab):
		self.data=dataTab
		self.t=tTab
	def learn(self):
		counter = self.ages
		while counter>0:
			counter-=1
			for i in range(len(self.data[0])):
				a=self.w1*self.data[0][i]+self.w2*self.data[1][i]+self.b
				if a>0:
					y=1
				else:
					y=0
				e=self.t[i]-y
				if e!=0:
					self.w1=self.w1+e*self.data[0][i]
					self.w2=self.w2+e*self.data[1][i]
					self.b=self.b+e
	def test(self):
		correct,bad=0,0
		for i in range(len(self.data[0])):
			a=self.w1*self.data[0][i]+self.w2*self.data[1][i]+self.b
			if a>0:
				y=1
			else:
				y=0
			if self.t[i]==y:
				correct+=1
			else:
				bad+=1
		print("correct matches ",correct," ;bad matches ",bad)