import os
import sys

inp = os.path.join(f"{sys.argv[1]}.metrics")


def extract_from_metrics(in_file):
    with open(in_file) as f:
        d = {}
        for line in f:
            ln = line.rstrip()
            if ln.startswith("%"):
                d["perc_none"] = ln.split()[-1]
            elif ln.startswith("mean"):
                d["mean_cov"] = ln.split()[-1]
            elif ln.startswith("minimum"):
                d["min_size"] = ln.split()[-1]
            elif ln.startswith("maximum"):
                d["max_size"] = ln.split()[-1]
    return d


def format_this(d):
    return f"{d.get('samp_nm')},{d.get('perc_none')},{d.get('mean_cov')},{d.get('min_size')},{d.get('max_size')}"


def main():
    metrics_dict = extract_from_metrics(inp)
    metrics_dict.update({"samp_nm": sys.argv[1]})
    print(format_this(metrics_dict))


if __name__ == '__main__':
    main()