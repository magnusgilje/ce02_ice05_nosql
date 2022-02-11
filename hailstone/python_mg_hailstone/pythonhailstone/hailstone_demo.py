import sys
import getopt
import logging
# import matplotlib.pyplot as plt

sys.path.insert(0,"..")
import hailstone

def main(argv):
    """Main function for circle code to process the file arguments """

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.WARNING)

    n = None #int(input('your starting n'))
    try:
        opts, _args = getopt.getopt(argv, "n:", ["starting n="])
    except getopt.GetoptError:
        print('hailstone_demo.py -n <start>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('hailstone_demo.py -n <start>')
            sys.exit()
        elif opt in ("-n", "--start"):
            n = arg

    if n is None:
       print('hailstone_demo.py -n <start>')
    else:
        try:                
            myH = hailstone.Hailstone(int(n))
            print(myH.plot())
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

if __name__ == "__main__":
    main(sys.argv[1:])
