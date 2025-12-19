def root(num1, num2):
    if num1 < 0 and num2 % 2 == 0:
        return 'error, negative number does not have root.'
    if num2 == 0:
        return 'error, root with index 0 does not exist.'
    
    z = num1 ** (1/num2)
    return f'{z:.5f}'


def interface():
    operations = ['addition', 'subtraction', 'multiplication', 'division', 'exponential', 'root']
    print('******************')
    op = str(input('OPERATION: ').strip().lower())
    if op not in operations:
        return 'error, operation not found.'
    try:
        num1, num2 = map(float, input().split())
    except ValueError:
        return 'error, invalid input.'
    print('******************')
    
    if op == 'addition':
        z = num1 + num2
        return f'{z:.3f}'
    elif op == 'subtraction':
        z = num1 - num2 
        return f'{z:.3f}'
    elif op == 'multiplication':
        z = num1 * num2 
        return f'{z:.3f}'
    elif op == 'division':
        if num2 == 0:
            return 'error, division by zero.'
        z = num1 / num2 
        return f'{z:.3f}'
    elif op == 'exponential':
        z = num1 ** num2
        return f'{z:.3f}'
    elif op == 'root':
        return root(num1, num2)

print(interface())