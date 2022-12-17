def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    binar_number = []
    while decimal_number != 0:
        binar_number.append(decimal_number%2)
        decimal_number = int(decimal_number/2)
    return(binar_number[::-1])

def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    decimal_number = 0
    amp = 0
    for nums in binary_digits[::-1]:    
        if nums == 0:
            pass
        else:
            decimal_number += 2**amp 
        amp += 1
    return decimal_number


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    base_number = []
    while decimal_number != 0:
        base_number.append(decimal_number%destination_base)
        decimal_number =+ int(decimal_number/destination_base)
    return base_number[::-1]


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    decimal_number = 0
    amp = 0
    for nums in digits[::-1]:    
        if nums == 0:
            pass
        else:
            decimal_number += nums*(original_base**amp)
        amp += 1
    return decimal_number


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    digit_to_string = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    number = ''
    for nums in digits:
        if nums >= 10:
            number += digit_to_string.get(nums)
        else:
            number += str(nums)
            
    if base > 16:
        raise ValueError
    
    return number


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    decimal_number = 0
    amp = 0
    
    for nums in original_digits[::-1]:
        decimal_number += nums*(original_base**amp)
        amp += 1
    
    if original_base == 10 or destination_base == 10:
        return decimal_number
    
    destination_number = []
    while decimal_number != 0:
        destination_number.append(decimal_number%destination_base)
        decimal_number = int(decimal_number/destination_base)
    
    return destination_number[::-1]
