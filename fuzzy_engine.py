import numpy as np
from gaussien_kde import Gaussien_kde

class FuzzyEngine(object):

	def __init__(self, n_partitions = 3):
		self.dataset = None
		self.target = None
		self.xpartitions = []
		self.ypartitions = []
		self.n_partitions = []
		self.map = []
		self.hyperarea = []

	def fit(self, x, y):
		pass


	def create_partitions():
		for x in self.dataset:
			g_kde = Gaussien_kde(x)
			np.vectorize(g_kde.ppf)
			parts = g_kde.ppf(np.linspace(0,1, self.n_partition + 1))
			parts = [i for i in zip(self.parts[:-1], self.part[1:])]
			self.xpartitions.append(parts)
			
		for y in self.target:
			g_kde = Gaussien_kde(y)
			np.vectorize(g_kde.ppf)
			parts = g_kde.ppf(np.linspace(0,1, self.n_partition + 1))
			parts = [i for i in zip(self.parts[:-1], self.part[1:])]
			self.ypartitions.append(parts)

	def create_rules():
		rules = np.copy(self.dataset)
		

	def create_hyperarea():
		pass

