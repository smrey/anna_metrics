import os
import sys

inp = os.path.join(f"{sys.argv[1]}.cov")


def average_depth(in_file):
    cov = 0
    numb = 0
    with open(os.path.join(in_file)) as f:
        for line in f:
            try:
                cov += int(line.strip().split()[1])
                numb += 1
            except:
                numb += 1
            #print(f"No numbers in line {line.strip()}")
    return cov/numb


def main():
    print(average_depth(inp))


if __name__ == '__main__':
    main()