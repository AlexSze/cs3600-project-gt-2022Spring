from NeuralNetUtil import buildExamplesFromCarData, buildExamplesFromPenData, buildExamplesFromExtraData
from NeuralNet import Perceptron, buildNeuralNet
from math import pow, sqrt


def average(argList):
    return sum(argList)/float(len(argList))


def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean), 2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))


penData = buildExamplesFromPenData()


def testPenData(hiddenLayers=[24]):
    return buildNeuralNet(penData, maxItr=200, hiddenLayerList=hiddenLayers)


carData = buildExamplesFromCarData()


def testCarData(hiddenLayers=[16]):
    return buildNeuralNet(carData, maxItr=200, hiddenLayerList=hiddenLayers)


# # question 5
# penResult = []
# carResult = []

# for _ in range(5):
#     nnet, j = testPenData()
#     nnet, i = testCarData()

#     penResult.append(j)
#     carResult.append(i)

# print('penResult, max: ', max(penResult), ' average: ',
#       average(penResult), ' sd: ', stDeviation(penResult))
# print('carResult, max: ', max(carResult), ' average: ',
#       average(carResult), ' sd: ', stDeviation(carResult))

# # question 6
# tempPerceptron = 0
# penFinalResult = []
# carFinalResult = []

# for _ in range(9):
#     penResult = []
#     carResult = []

#     for _ in range(5):
#         nnet, j = testPenData([tempPerceptron])
#         nnet, i = testCarData([tempPerceptron])

#         penResult.append(j)
#         carResult.append(i)

#     tempPerceptron += 5
#     penFinalResult.append(penResult)
#     carFinalResult.append(carResult)

# for i in range(9):
#     penResult = penFinalResult[i]
#     print(i, ', penResult, max: ', max(penResult), ' average: ',
#           average(penResult), ' sd: ', stDeviation(penResult))

# for j in range(9):
#     carResult = carFinalResult[j]
#     print(j, ', carResult, max: ', max(carResult), ' average: ',
#           average(carResult), ' sd: ', stDeviation(carResult))


# question 7
xorData = [[([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])],
           [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]]


def testXorData(hiddenLayers=[10]):
    return buildNeuralNet(xorData, maxItr=500, hiddenLayerList=hiddenLayers)


xorPerceptron = [0]
k = 0
while k != 1.0:
    xorPerceptron[0] += 1
    nnet, k = testXorData(xorPerceptron)

nnet, p = testXorData([0])
print([0], p)
print(xorPerceptron, k)


# # question 8
# xorData = buildExamplesFromExtraData()


# def testXorData(hiddenLayers=[25]):
#     return buildNeuralNet(xorData, maxItr=500, hiddenLayerList=hiddenLayers)


# q8Result = []

# for _ in range(5):
#     nnet, j = testXorData()

#     q8Result.append(j)

# print('q8Result, max: ', max(q8Result), ' average: ',
#       average(q8Result), ' sd: ', stDeviation(q8Result))
