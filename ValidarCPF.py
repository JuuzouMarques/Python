def validateCPF(cpf):
    firts9digits = cpf[:9] # Takes the first nine digits of the CPF
    firstCheckDigit = secCheckDigit = 0 # Check Digits

    # Calculate First Check Digit
    summation = 0
    multiplier = 10  
    for digit in firts9digits:
        summation += digit * multiplier
        multiplier -= 1
    restDivision = summation % 11
    if restDivision < 2:
        firstCheckDigit = 0
    else:
        
    



if __name__ == '__main__':
    cpf = input('Enter a CPF for validation: ')
    cpf = cpf.strip().replace('.','').replace('-', '')
    print(cpf)
    