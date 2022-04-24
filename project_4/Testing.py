from NeuralNetUtil import buildExamplesFromCarData, buildExamplesFromPenData
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


# question 5
penResult = []
carResult = []

for _ in range(5):
    nnet, j = testPenData()
    nnet, i = testCarData()

    penResult.append(j)
    carResult.append(i)

print('penResult, max: ', max(penResult), ' average: ',
      average(penResult), ' sd: ', stDeviation(penResult))
print('carResult, max: ', max(carResult), ' average: ',
      average(carResult), ' sd: ', stDeviation(carResult))

# question 6
tempPerceptron = 0
penFinalResult = []
carFinalResult = []

for _ in range(9):
    penResult = []
    carResult = []

    for _ in range(5):
        nnet, j = testPenData([tempPerceptron])
        nnet, i = testCarData([tempPerceptron])

        penResult.append(j)
        carResult.append(i)

    tempPerceptron += 5
    penFinalResult.append(penResult)
    carFinalResult.append(carResult)

for i in range(9):
    penResult = penFinalResult[i]
    print(i, ', penResult, max: ', max(penResult), ' average: ',
          average(penResult), ' sd: ', stDeviation(penResult))

for j in range(9):
    carResult = carFinalResult[j]
    print(j, ', carResult, max: ', max(carResult), ' average: ',
          average(carResult), ' sd: ', stDeviation(carResult))
