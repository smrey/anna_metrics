import os
import sys

inp = os.path.join(f"{sys.argv[1]}.cov")


# Count total number of entries in file
def total_entries_count(in_file):
    count = 0
    with open(in_file) as f:
        for line in f:
            count += 1
    return count


# Count number of zero coverage entries in file
def no_coverage_count(in_file):
    count = 0
    with open(in_file) as f:
        for line in f:
            if line.strip().split()[1] == "0":
                count += 1
    return count


# Pull out average depth of coverage over regions in file
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
    return cov/numb


# Pull out regions of no coverage in file
def no_coverage_regions(in_file):
    regions = []
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
                    regions.append(f"{first_coord}-{second_coord}")
                    set_print = False
                set_flag = False
            ln = line
            ln_cov = line.strip().split()[1]
    return regions


# Pull out regions of no coverage in file
def no_coverage_sizes(in_file):
    with open(in_file) as f:
        ln_cov = ""
        first_coord = ""
        second_coord = ""
        set_flag = False
        set_print = False
        max_len = 0
        min_len = 10000
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
                    #print(f"{first_coord}-{second_coord}")
                    length = int(second_coord.split(":")[1]) - int(first_coord.split(":")[1])
                    #print(length)
                    max_len = max_size(length, max_len)
                    min_len = min_size(length, min_len)
                    set_print = False
                set_flag = False
            ln = line
            ln_cov = line.strip().split()[1]
        return min_len, max_len


def max_size(sz, m):
    if sz > m:
        m = sz
    return m


def min_size(sz, m):
    if sz < m:
        m = sz
    return m


def main():
    if sys.argv[2] == "-g":
        no_cov = no_coverage_count(inp)
        tot = total_entries_count(inp)
        print(f"% no coverage {no_cov/tot*100}")
        print(f"mean coverage depth {average_depth(inp)}")
    elif sys.argv[2] == "-c":
        no_cov = no_coverage_count(inp)
        tot = total_entries_count(inp)
        print(f"% no coverage {no_cov/tot*100}")
        print(f"mean coverage depth {average_depth(inp)}")
        print(f"minimum size of contiguous regions with no coverage {no_coverage_sizes(inp)[0]}")
        print(f"maximum size of contiguous regions with no coverage {no_coverage_sizes(inp)[1]}")


if __name__ == '__main__':
    main()
