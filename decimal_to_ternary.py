def decimal_ternay_conv(number_input):

    '''
    KeyWord:
    number_input : Giving a certain decimal number to be convert
    '''
    result = []
    while True:
        divide = number_input//3
        mod = number_input % 3
        number_input = divide
        result.append(mod)
        if number_input == 0:
            result = result[::-1]
            result = [str(i) for i in result]
            result = ''.join(result)
            break

    return result



