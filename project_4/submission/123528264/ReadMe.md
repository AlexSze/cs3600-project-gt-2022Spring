Question 8:

max,	average,	standard deviation
0.98475609756097600,	0.97591463414634100,	0.00504662968208747

The data I have used is a banknote dataset by (Brownlee, 2021). It is a binary (0 for authentic, 1 for inauthentic) classification dataset which takes the following attributes:
1. Variance of Wavelet Transformed image (continuous).
2. Skewness of Wavelet Transformed image (continuous).
3. Kurtosis of Wavelet Transformed image (continuous).
4. Entropy of image (continuous).

Firstly, I use getNNQ8Data() to shape the data into a readable format by the model. Secondly, I used buildExamplesFromExtraData() to get both training and testing data from its respective txt file. After that, I use the follow code to call the above functions to shape the data and to execute the learning model with some parameters: 

xorData = buildExamplesFromExtraData()
def testXorData(hiddenLayers=[25]):
    return buildNeuralNet(xorData, maxItr=500, hiddenLayerList=hiddenLayers)
q8Result = []
for _ in range(5):
    nnet, j = testXorData()
    q8Result.append(j)
print('q8Result, max: ', max(q8Result), ' average: ',
      average(q8Result), ' sd: ', stDeviation(q8Result))

The above code will print the max, average and sd of the accuracy in the 5 restarted network. 