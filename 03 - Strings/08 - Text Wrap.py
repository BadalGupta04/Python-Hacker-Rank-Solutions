import textwrap

def wrap(string, max_width):
    Cloudy = '\n'.join(textwrap.wrap(string, max_width))
    return Cloudy
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)