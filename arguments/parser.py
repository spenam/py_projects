import argparse
parser = argparse.ArgumentParser()
defau=45
parser.add_argument("--quality", type=int, help="enter some quality limit", nargs='?', default=0 , const=0)
parser.add_argument("--velo", type=float, help="enter some velo", default=defau )
args = parser.parse_args()
print(args)
print(args.quality)
print(args.velo)
