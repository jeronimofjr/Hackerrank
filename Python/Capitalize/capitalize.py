# Complete the solve function below.
def solve(s):
    return ' '.join(list(map(str.capitalize, s.split(" "))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
