def split_and_join(line):
    x = line.split()
    line = '-'.join(x)
    return line
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)