def calculate(expression):
    try:
        expression = expression.replace(" ", "")

        while '(' in expression:
            start = expression.rfind('(')
            end = expression.find(')', start)
            result = calculate(expression[start+1:end])
            expression = expression[:start] + str(result) + expression[end + 1:]

        while '/' in expression or '*' in expression:
            if '/' in expression and '*' in expression:
                div = expression.index('/')
                mul = expression.index('*')
                if div < mul:
                    index = div
                else:
                    index = mul
            
            elif '/' in expression:
                index = expression.index('/')
            else:
                index = expression.index('*')

            num1 = int(expression[index-1])
            num2 = int(expression[index+1])

            if expression[index] == '/':
                result = (num1//num2)
            else:
                result = num1*num2

            expression = expression[:index-1] + str(result) + expression[index+2:]

        while '+' in expression or '-' in expression:
            if '+' in expression and '-' in expression:
                add = expression.index('+')
                sub = expression.index('-')
                if add < sub:
                    index = add
                else:
                    index = sub
            
            elif '+' in expression:
                index = expression.index('+')
            else:
                index = expression.index('-')

            num1 = int(expression[index-1])
            num2 = int(expression[index+1])

            if expression[index] == '+':
                result = num1+num2
            else:
                result = num1-num2

            expression = expression[:index-1] + str(result) + expression[index+2:]

        return expression
    
    except (ValueError, ZeroDivisionError) as e:
        raise ValueError(e)

if __name__ == '__main__':
    while True:
        try:
            user_input = input("Enter expression: ")
            result = calculate(user_input)
            print(result)
            if user_input.lower() == 'bye':
                break
        except ValueError as ve:
            print(ve)