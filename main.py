#!/usr/bin/env python

import fileinput
import json


def main():
    blobs = {}
    counts = {}
    for line in fileinput.input():
        prefix = line[:3]
        counts[prefix] = counts[prefix] + 1 if prefix in counts else 1
        blob = blobs[prefix] if prefix in blobs else []
        blob.append(line.rstrip())
        blobs[prefix] = blob
        if len(blob) == 100:
            pass


    print(json.dumps(blobs))


if __name__ == '__main__':
    main()
