def arithmetic_arranger(problems, showAnswer=False):
    if len(problems) > 5:
        return('Error: Too many problems.')
    #creates 4 empty strings each representing 1 line for the columns
    line1, line2, line3, line4 = '', '', '', ''
    lastline = False
    for i,p in enumerate(problems):
        #checks if loop has reached the last line
        if i+1 == len(problems):
            lastline = True
        #extracts the operator from the input
        operator = p.split(' ')[1]
        #checks if input is valid
        try:
            number1 = int(p.split(' ')[0])
            number2 = int(p.split(' ')[2])
        #if returns a ValueError the input must not be a digit
        except ValueError:
            return('Error: Numbers must only contain digits.')
        #makes sure the numbers are not longer than 5 digits
        if number1 > 9999 or number2 > 9999:
            return('Error: Numbers cannot be more than four digits.')
        #calculates the correct answer and returns an error if a different operator than + or - was given
        if operator == '+':
            answer = number1 + number2
        elif operator =='-':
            answer = number1 - number2
        else:
            return('Error: Operator must be \'+\' or \'-\'.')
        #checks how wide the column has to be to properly fit the largest number (with one space between the operator and the largest number)
        if number1 > number2:
            spacer = len(str(number1))
        else:
            spacer = len(str(number2))
        #correctly formats each line by aligning to the proper width
        line1 += f'{number1 : >{2+spacer}}'
        line2 += f'{operator}{number2 : >{1+spacer}}'
        line3 += '-'*(2+spacer)
        line4 += f'{answer : >{2+spacer}}'
        #seperates columns (from the next) if it's not the last line
        if not lastline:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            line4 += '    '
        #joins all lines into 1 string, with the option of adding the answers if the second parameter is set to True
        elif lastline:
            if showAnswer:
                result = '\n'.join((line1,line2,line3,line4))
            else:
                result = '\n'.join((line1,line2,line3))
    return(result)
