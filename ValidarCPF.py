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

if __name__ == '__main__':
    cpf = input('Enter a CPF for validation: ')
    cpf = cpf.strip().replace('.','').replace('-', '')
    print('This CPF is VALID!' if validateCPF(cpf) else 'This CPF is INVALID!')
    
    