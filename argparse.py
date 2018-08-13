from argparse import ArgumentParser


parser = ArgumentParser()
parser.addadd_argument('--name', default='xxx')
parser.addadd_argument('--data', default=None)
args = parser.parse_args()

name = args.name
if args.data is None:
    pass
else:
    data = args.data
