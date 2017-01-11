import numpy as np
from gaussien_kde import Gaussien_kde

class FuzzyEngine(object):

	def __init__(self, n_partitions = 3):
		self.dataset = None
		self.target = None
		self.partitions = []
		self.n_partitions = []
		self.map = []
		self.hyperarea = []

	def fit(self, x, y):
		pass


	def create_partitions():
		for x in self.dataset:
			g_kde = Gaussien_kde(x)
			np.vectorize(g_kde.ppf)
			partition = zip(np.linspace(0,1, self.n_partition + 1)
				
		

	def create_rules():
		pass

	def create_hyperarea():
		pass

