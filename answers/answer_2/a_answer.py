import b

def function_a():
    print('function_a')
    return b.function_b()

try:
    function_a()
except:
    pass