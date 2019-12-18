import os
import sys

inp1 = os.path.join(f"{sys.argv[1]}.metrics")
inp2 = os.path.join(f"{sys.argv[1]}_flagstat.txt")


def extract_from_metrics(in_file):
    with open(in_file) as f:
        d = {}
        for line in f:
            ln = line.rstrip()
            if ln.startswith("%"):
                d["perc_none"] = ln.split()[-1]
            elif ln.startswith("mean"):
                d["mean_cov"] = ln.split()[-1]
    return d


def extract_from_flagstat(in_file):
    with open(in_file) as f:
        d = {}
        for i, line in enumerate(f):
            ln = line.rstrip()
            if i == 4:
                d["num_reads"] = ln.split()[0]
                d["perc_mapped"] = ln.split()[4].split("%")[0].lstrip("(")
    return d


def format_this(d):
    return f"{d.get('samp_nm')},{d.get('num_reads')},{d.get('perc_mapped')},{d.get('perc_none')},{d.get('mean_cov')}"


def main():
    metrics_dict = extract_from_metrics(inp1)
    metrics_dict.update(extract_from_flagstat(inp2))
    metrics_dict.update({"samp_nm": sys.argv[1]})
    print(format_this(metrics_dict))



if __name__ == '__main__':
    main()