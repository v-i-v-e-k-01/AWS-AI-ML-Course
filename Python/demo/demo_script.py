print(2+3)
num = 8

def mean(num_list):
    return sum(num_list)/len(num_list)

def add_five(num_list):
    return [n+5 for n in num_list]

# the code inside the   if __name == '__main__':   block is
# executed only if the demo_script file is run directly
# if demo_script file is imported in other files, the code in 
# the block isn't executed

if __name__ == '__main__' : 
    print("Testing mean function")
    a_list = [34,44,24,48,12,24]
    correct_mean=31
    assert( mean(a_list) == correct_mean )

    print("Testing add_five function")
    correct_list=[39,49,29,53,17,29]
    assert( add_five(a_list) == correct_list )

    print("All tests passed")