'''
def recursive_way_2Multiply(x, i, result):
        if i <= 0:
            return result
        result += x
        i = i-1
        return recursive_way_2Multiply(x, i, result)
def fact(n):
      if n == 1:
        return n
      return n*fact(n-1)


def printMove(fr, to):
    print(f"Move from {fr} to {to}")
    
def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n-1, fr, spare, to) 
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)
'''

def get_stats(class_list):
    new_list = []
    for index in class_list:
        print(f'Student: {index[0][0]}')
        new_list.append([index[0], index[1], avg(index[1])])
    return new_list
def avg(grades):
    assert not len(grades) == 0, f'No grades data : {grades}'
    print("Everything Okay\n")
    return sum(grades)/len(grades)
    try:
        result = sum(grades)/len(grades)
        print("Everything Okay\n")
        return result
    except ZeroDivisionError:
        print("Warning! No grades data\n")
        return 0.0

class_list = [
              [ ['Peter', 'Parker'], [7.0, 8.0, 8.5]],
              [ ['Bruce', 'Wayne'], [10.0, 8.0, 7.5]], 
              [ ["Clark", "Kent"], [2.0, 3.0, 8.5]],
              [ ["Deadpool"],[]]   
             ]

print(get_stats(class_list))
