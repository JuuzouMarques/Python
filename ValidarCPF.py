def validateCPF(cpf):
    firts9digits = cpf[:9] # Takes the first nine digits of the CPF
    firstCheckDigit = secCheckDigit = 0 # Check Digits

    # Calculate First Check Digit
    summation = 0
    multiplier = 10  
    for digit in firts9digits:
        summation += int(digit) * multiplier
        multiplier -= 1
    restDivision = summation % 11
    if restDivision >= 2:
        firstCheckDigit = 11 - restDivision

    # Calculate Second Check Digit
    firts10digits = firts9digits + str(firstCheckDigit)
    summation = 0
    multiplier = 11
    for digit in firts10digits:
        summation += int(digit) * multiplier
        multiplier -= 1
    restDivision = summation % 11
    if restDivision >= 2:
        secCheckDigit = 11 - restDivision
    
    cpfVerified = firts9digits + str(firstCheckDigit) + str(secCheckDigit)
    return True if cpf == cpfVerified else False
    print('This CPF is VALID!' if cpf == cpfVerified else 'This CPF is INVALID!')

def validateCNPJ(cnpj):
    first12 = cnpj[:12] # Takes the first twelve digits of the CNPJ
    firstCheckDigit = secCheckDigit = 0 # Check Digits
 
    # Calculate First Digit Check
    multiplier = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    summation = 0
    for fat, num in zip(multiplier, first12):
        summation += fat * int(num)
    restDivision = summation % 11
    if restDivision >= 2: firstCheckDigit = 11 - restDivision
 
    # Calculate Second Digit Check
    first13 = first12 + str(firstCheckDigit)
    multiplier = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    summation = 0
    for fat, num in zip(multiplier, first13):
        summation += fat * int(num)
    restDivision = summation % 11
    if restDivision >= 2: secCheckDigit = 11 - restDivision
    cnpjValid = first12 + str(firstCheckDigit) + str(secCheckDigit)
    return True if cnpjValid == cnpj else False

if __name__ == '__main__':
    response = input('CPF [1] or CNPJ [2]?' )
    if response == '1':
        cpf = input('Enter a CPF for validation: ')
        cpf = cpf.strip().replace('.','').replace('-', '')
        print('This CPF is VALID!' if validateCPF(cpf) else 'This CPF is INVALID!')
    elif response == '2':
        cnpj = input('Enter a CNPJ for validation: ')
        cnpj = cnpj.strip().replace('.', '').replace('-', '').replace('/', '')
        print('This CNPJ is VALID' if validateCNPJ(cnpj) else 'This CNPJ is INVALID')
    else:
        print('You entered an invalid value!')
