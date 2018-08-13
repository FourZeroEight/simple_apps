from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--name', default='xxx')
parser.add_argument('--data', default=None)
args = parser.parse_args()

name = args.name
if args.data is None:
    pass
else:
    data = args.data
