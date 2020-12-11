#!/usr/bin/env python3

import fileinput
import gzip


def main():
    batches = {}
    counts = {}
    for line in fileinput.input():
        prefix = line[:3]
        batches[prefix] = batches[prefix] if prefix in batches else []
        batches[prefix].append(line.encode())
        if len(batches[prefix]) > 10_000:
            process_batch(batches, counts, prefix)
        elif len(batches[prefix]) % 1_000 == 0 and prefix == "aaa":
            print(f"{prefix} size: {len(batches[prefix])}")

    for prefix in batches:
        process_batch(batches, counts, prefix)


def process_batch(batches, counts, prefix):
    counts[prefix] = counts[prefix] + 1 if prefix in counts else 1
    write_batch(batches[prefix], counts[prefix], prefix)
    batches[prefix] = []


def write_batch(batch, count, prefix):
    output_file = f"partitioned/{prefix}-{count:06d}.txt.gz"
    with gzip.open(output_file, 'wb') as f:
        contents = b''.join(batch)
        f.write(contents)
    print(f"Wrote batch {output_file}")


if __name__ == '__main__':
    main()
