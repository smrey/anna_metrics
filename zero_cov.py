import os
import sys

inp = os.path.join(f"{sys.argv[1]}.cov")


def total_entries_count(in_file):
    count = 0
    with open(in_file) as f:
        for line in f:
            count += 1
    return count


def no_coverage_count(in_file):
    count = 0
    with open(in_file) as f:
        for line in f:
            if line.strip().split()[1] == "0":
                count += 1
    return count


def no_coverage_regions(in_file):
    with open(in_file) as f:
        ln_cov = ""
        first_coord = ""
        second_coord = ""
        set_flag = False
        set_print = False
        for line in f:
            if ln_cov == "0" and ln_cov == line.strip().split()[1] and not set_flag:
                first_coord = ln.strip().split()[0]
                second_coord = line.strip().split()[0]
                set_flag = True
                set_print = True
            elif ln_cov == "0" and ln_cov == line.strip().split()[1] and set_flag:
                second_coord = line.strip().split()[0]
            else:
                if set_print:
                    print(f"{first_coord}-{second_coord}")
                    set_print = False
                set_flag = False
            ln = line
            ln_cov = line.strip().split()[1]


def main():
    no_cov = no_coverage_count(inp)
    tot = total_entries_count(inp)
    print(no_cov)
    print(tot)
    print(no_cov/tot*100)


if __name__ == '__main__':
    main()
