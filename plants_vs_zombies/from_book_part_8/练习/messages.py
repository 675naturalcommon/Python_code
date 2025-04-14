list = ['hello', 'world', 'python']
print(list)

def greetings(list):
    new_lst = list[:]
    for i,word in enumerate(new_lst[:]):
        new_lst[i] = word.upper()
        #new_lst.append(word.upper())
    return new_lst

new_list = greetings(list)
print(new_list)
print(list)