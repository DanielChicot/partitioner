#!/usr/bin/env python

import fileinput
import gzip


def main():
    blobs = {}
    counts = {}
    for line in fileinput.input():
        prefix = line[:3]
        counts[prefix] = counts[prefix] + 1 if prefix in counts else 1
        blobs[prefix] = blobs[prefix] if prefix in blobs else []
        blobs[prefix].append(line.encode())
        if len(blobs[prefix]) == 7:
            output_file = f"partitioned/{prefix}-{counts[prefix]:06d}.txt.gz"
            with gzip.open(output_file, 'wb') as f:
                for guid in blobs[prefix]:
                    f.write(guid)
                print(f"Wrote {output_file}")


if __name__ == '__main__':
    main()
