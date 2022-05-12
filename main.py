import sys
import argparse

def main() -> int:
    """Main function..."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--value", dest="val", type=int, help="Value to use.")
    args = parser.parse_args()

    print(args.val)

    return 0

if __name__ == "__main__":
    sys.exit(main())
