
import numpy as np

class Input:
	def __init__(self, value):
		self.value = value

	def getOutput(self):
		return self.value

class Neuron:
	def __init__(self, previousLayerNeurons):
		self.inputs = previousLayerNeurons
		self.bias = 0
		self.weigths = [0] * len(previousLayerNeurons)

	def activation(self, z):
		raise NotImplementedError

	def getOutput(self):
		outputs = [neuron.getOutput() for neuron in self.inputs]
		projection = 0
		for (output, weight) in zip(outputs, self.weights):
			projection += output * weight
		response = self.activation(self.bias + projection)
		return response

class SigmoidNeuron(Neuron):
	def activation(self, z):
		return (1 / (1 + np.exp(-z)))

class Perceptron(Neuron):
	def activation(self, z):
		if z > 0:
			return 1
		else:
			return 0

#
# first layer: 
#

def trainNN(X, y, numHiddenLayers, neuronsPerLayer):
	nn = NNModel()
	# ...
	return nn

# if nHL = 1
# if nPL = [2]

outputNeuron = StepNeuron()
hiddenLayers = list()
hiddenLayers[0] = [StepNeuron() for i in range(0, nPL[0])]

n2 = StepNeuron()



