import re
import sys

def semantic_wrap(text):
    return re.sub(r'(?<=[\.?!])( *)(?!\s+|$)', '\n', text)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        # flush the data out without print putting a newline on there
        sys.stdout.write(semantic_wrap(f.read()))
        sys.stdout.flush()
        # python3 way
        #print(semantic_wrap(f.read()), end="")
