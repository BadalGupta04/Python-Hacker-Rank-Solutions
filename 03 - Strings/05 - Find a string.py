def count_substring(string, sub_string):
    a = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            a += 1
    return a
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)