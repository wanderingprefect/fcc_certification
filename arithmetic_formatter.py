def arithmetic_arranger(problems, showAnswer=False):
    if len(problems) > 5:
        return('Error: Too many problems.')
    line1, line2, line3, line4 = '', '', '', ''
    lastline = False
    for i,p in enumerate(problems):
        if i+1 == len(problems):
            lastline = True
        operator = p.split(' ')[1]
        #checks if input is valid
        try:
            number1 = int(p.split(' ')[0])
            number2 = int(p.split(' ')[2])
        except ValueError:
            return('Error: Numbers must only contain digits.')
        if number1 > 9999 or number2 > 9999:
            return('Error: Numbers cannot be more than four digits.')
        if operator == '+':
            answer = number1 + number2
        elif operator =='-':
            answer = number1 - number2
        else:
            return('Error: Operator must be \'+\' or \'-\'.')
        #makes sure its correctly formatted to fit numbers
        if number1 > number2:
            spacer = len(str(number1))
        else:
            spacer = len(str(number2))
        #correctly formats each line
        line1 += f'{number1 : >{2+spacer}}'
        line2 += f'{operator}{number2 : >{1+spacer}}'
        line3 += '-'*(2+spacer)
        line4 += f'{answer : >{2+spacer}}'
        #seperates columns if it's not the last line
        if not lastline:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            line4 += '    '
        #adds answers if it is asked
        elif lastline:
            if showAnswer:
                result = '\n'.join((line1,line2,line3,line4))
            else:
                result = '\n'.join((line1,line2,line3))
    return(result)