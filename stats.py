# A collection of stats functions, writing as practice to teach myself Python.

import panda as pd

def findWeightedAverage(numbers, weights):
	sumCombined = 0
	sumWeights = 0
	for i in range(len(numbers)):
		sumCombined = sumCombined + numbers[i] * weights[i]
		sumWeights = sumWeights + weights[i]

	return round(float(sumCombined)/sumWeights, 1)

def calculateStdDeviation(numbers):
	sum = 0
	for i in range(len(numbers)):
		sum = sum + numbers[i]

	mean = sum / len(numbers)
	distFromMean = []
	for i in range(len(numbers)):
		distFromMean.append((numbers[i] - mean) ** 2)

	distFromMeanSum = 0
	for i in range(len(dist)):
		distFromMeanSum = distFromMeanSum + distFromMean[i]

	stdv = (distFromMeanSum / len(numbers)) ** (1/2)
	return round(stdv, 1)

def calculateQuartiles(numbers):
	n = len(numbers)
	front = true
	q1 = 0
	q2 = median(numbers, n, front)
	q3 = 0

	if n % 2 == 0:
		front = true
		q1 = median(numbers, int((n/2)-1), front)
		front = false
		q3 = median(numbers, int((n/2)), front)
		print(q1)
		print(q3)

	elif n % 2 != 0:
		front = true
		q1 = median(numbers, int((n-1)/2), front)
		front = false
		q3 = median(numbers, int((n-1)/2), front)
		print(q1)
		print(q3)
		

def calculateMedian(numbers, n, front):
	med = []
	q = 0
	if front:
		for i in range(n):
			med.append(numbers[i])
		q = pd.median(med)
		return q
		
	else:
		for i in range(n, len(numbers)):
			med.append(numbers[i])
		q = pd.median(med)
		return q