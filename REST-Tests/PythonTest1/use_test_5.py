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
    {"firstDecimal": 0, "secondDecimal": 0}, #both Decimals were set
    {"firstDecimal": 0}, # Only first Decimal was set
    { "secondDecimal": 0}, # Only second Decimal was set
    {} # No Decimals were set
    ] 
expectedErrorResults = ['None', 'Both decimals should be set', 'Both decimals should be set', 'Both decimals should be set']

for i in range(len(operations)):
    response = requests.post(url + operations[i], json=inputs[i])
    if((str(response.json()['error'])==expectedErrorResults[i])):
        print('Test '+ str(i+1) + ": " + operations[i] + ' passed')
    else:
        print('Test '+ str(i+1)+ ": " + operations[i] + ' failed' + ' Expected: ' + str(expectedErrorResults[i]) + ' Actual: ' + str(response.json()['error']))
    
    