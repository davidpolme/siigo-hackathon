''' 
This is a test script for validate the functionality of the 
operations in the the REST API Calculator

The test script will test the following endpoints:
- /divide/
- /multiply/
- /add/
- /substract/
'''
import requests

base = 'http://localhost:5000'
path= '/Calculator'
endpointDivide = '/divide/'
endpointMultiply = '/multiply/'
endpointAdd = '/add/'
endpointSubtract = '/substract/'

url= base + path

operations = [ endpointAdd, endpointSubtract, endpointDivide, endpointMultiply]

inputs = [
    {"firstDecimal": 14, "secondDecimal": 15}, #1 >= X >= 20 positive integers
    {"firstDecimal": 0.2, "secondDecimal": 0.5}, ## Decimals
    {"firstDecimal": 1, "secondDecimal": 1}, # X = 1 Digit (lower limit)
    {"firstDecimal": 12345678901234500000, "secondDecimal": 12345678901234500000}] ## X = 20 Digits (limite Superior) upper limit
expectedResults = [29, -0.3, 1, 0]

for i in range(len(operations)):
    response = requests.post(url + operations[i], json=inputs[i])
    if expectedResults[i] == response.json()['value']:
        print('Test '+ str(i+1) + ": " + operations[i] + ' passed')
    else: print('Test '+ str(i+1)+ ": " + operations[i] + ' failed' + ' Expected: ' + str(expectedResults[i]) + ' Actual: ' + str(response.json()['value']))
    
    



