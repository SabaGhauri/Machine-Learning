from agents import Agent

class Agent_sghauri(Agent):

	def will_buy(self,value,price,prob):
		
		if prob>0.8:
			return True
		elif price/value <=0.28:
			return True
		elif price/value >=0.56:
			return False
		elif prob<0.1:
			return False