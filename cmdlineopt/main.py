import argparse


parser = argparse.ArgumentParser(description="probe images from nsq")

parser.add_argument(
    '--server',
    type=str,
    help="NSQ Server",
    required=True)
parser.add_argument(
    '--topic',
    type=str,
    help="topic(s) to read",
    nargs="+")
args = parser.parse_args()


print(args.topic)
