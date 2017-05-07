
def add(array1, array2, length):
    resultArray = [0] * (length + 1);
    for i in range(length-1, -1, -1):
        resultArray[i+1] = resultArray[i+1] + array1[i] + array2[i];
        if resultArray[i+1] > 1:
            resultArray[i] = 1;
            resultArray[i + 1] = resultArray[i+1] % 2;
    return resultArray;

print(add([1],[1], 1)); #10
print(add([1,0,1,0],[0,1,0,1], 4)); #01111
print(add([1,1,1,1],[1,1,1,1], 4)); #11110