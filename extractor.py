#!/usr/bin/python
# Domino Hash Extracter v1.0
# Coded By Joel Noguera - @niemand_sec

import sys
import binascii
import argparse

# Check if we are running this on windows platform
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
    except:
        print("[!] Error: Coloring libraries not installed ,no coloring will be used")
        G = Y = B = R = W = G = Y = B = R = W = ''
else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    _ = "_"
    print('''%s
                ###################
                   ___                      _                     _  _                    _
                  |   \    ___    _ __     (_)    _ _      ___   | || |   __ _     ___   | |_
                  | |) |  / _ \  | '  \    | |   | ' \    / _ \  | __ |  / _` |   (_-<   | ' \\
                  |___/   \___/  |_|_|_|  _|_|_  |_||_|   \___/  |_||_|  \__,_|   /__/_  |_||_|
                _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|
                "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
                ###################%s%s
                # Coded By Joel Noguera - @niemand_sec
    ''' % (R, W, Y))


def parser_onerror(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "[!]Error: " + errmsg + W)
    sys.exit()


def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -l ListFile\r\n\t"
                                                                                     "python " + sys.argv[0] + " -f FileName\r\n")
    parser.error = parser_onerror
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-l', '--list', help="File Name of the list of user.id files")
    parser.add_argument('-f', '--file', help="File Name of only one user.id file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    list = args.list
    file = args.file


    # Printing Banner
    banner()

    if list:
        print "[#]Getting user.id files..."
        with open("list", "rb") as list:
            for line in list:
                with open(line.strip("\r\n"), "rb") as f:
                    bytes = f.read()
                    a = binascii.hexlify(bytes)
                    f.seek(216)
                    print f.name + ":" + binascii.hexlify(f.read(56))
    if file:
        print "[#]Getting user.id file..."
        with open(file.strip("\r\n"), "rb") as f:
            bytes = f.read()
            a = binascii.hexlify(bytes)
            f.seek(216)
            print f.name + ":" + binascii.hexlify(f.read(56))
    else:
        print "Invalid parameters"
