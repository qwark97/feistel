import argparse
import os


def generate_key():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file")
    parser.add_argument('-s', '--byte_size', type=int, default=16)
    args = parser.parse_args()
    key = os.urandom(args.byte_size)

    with open(args.output_file, 'wb') as f:
        f.write(key)


if __name__ == '__main__':
    generate_key()
