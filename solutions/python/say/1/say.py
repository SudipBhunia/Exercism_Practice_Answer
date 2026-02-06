def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def convert_chunk(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            result = tens[num // 10]
            if num % 10 != 0:
                result += "-" + ones[num % 10]
            return result
        else:
            result = ones[num // 100] + " hundred"
            remainder = num % 100
            if remainder != 0:
                result += " " + convert_chunk(remainder)
            return result
    
    billions = number // 1_000_000_000
    millions = (number % 1_000_000_000) // 1_000_000
    thousands = (number % 1_000_000) // 1_000
    remainder = number % 1_000
    
    parts = []
    
    if billions > 0:
        parts.append(convert_chunk(billions) + " billion")
    
    if millions > 0:
        parts.append(convert_chunk(millions) + " million")
    
    if thousands > 0:
        parts.append(convert_chunk(thousands) + " thousand")
    
    if remainder > 0:
        parts.append(convert_chunk(remainder))
    
    return " ".join(parts)
