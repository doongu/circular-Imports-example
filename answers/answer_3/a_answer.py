import b_answer

def function_a():
    print('function_a')
    return b_answer.function_b()

try:
    function_a()
except:
    pass