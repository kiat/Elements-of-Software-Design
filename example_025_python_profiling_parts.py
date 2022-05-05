import sys
import argparse
# import numpy as np
import cProfile
import pstats
import io


class Part:
    # 'PARTKEY', 'NAME', 'MFGR', 'BRAND', 'TYPE', 'SIZE', 'CONTAINER', 'RETAILPRICE', 'COMMENT'

    def __init__(self, **kwargs):
        self.partkey = kwargs.get('partkey', "0")
        self.name = kwargs.get('name', "0")
        self.mfgr = kwargs.get('mfgr', None)
        self.brand = kwargs.get('brand', None)
        self.type = kwargs.get('type', "")
        self.size = kwargs.get('size', "0")
        self.container = kwargs.get('container', "")
        self.retailprice = kwargs.get('retailprice', "0")
        self.comment = kwargs.get('comment', "")

    def __str__(self):
        return "CUSTOMER : ("+str(self.partkey) + " - " + self.name + " - " + \
            self.mfgr + " - " + self.brand + " - " + self.type + " - " + \
            str(self.size) + " - " + self.container + " - " +  \
            str(self.retailprice) + " - " + self.comment + ")"

    def __eq__(self, other):
        return self.partkey == other.partkey




def read_lines(filename):
    '''This functions reads each line of a file and returns a list of string lines.'''
    file = open(filename, 'r')

    lines = []
    count = 0

    while True:
        count += 1

        #  Get next line from file
        line = file.readline()

        # if line is empty end of file is reached
        if not line:
            break
        else:
            lines.append(line)
    return lines


def parse_lines(lines):
    parsed_values = []

    for line in lines:
        values = line.split("|")
        parsed_values.append(values)

    return parsed_values


def convert_toNumbers(parsed_values):
    '''Drop the first line which is the header and convert the remaining lines'''
    values = []
    count = 0

    for i in range(1, len(parsed_values)):

        values.append(
            [int(parsed_values[i][0]), parsed_values[i][1], parsed_values[i][2],
             parsed_values[i][3], parsed_values[i][4], int(
                 parsed_values[i][5]),
             parsed_values[i][6], float(parsed_values[i][7]), parsed_values[i][8]])
        i += 1

    return values


def convert_to_parts(values):
    ''' Find the max in a Part    
    '''
    parts = []

    for item in values:
        p = Part(partkey=item[0],
                 name=item[1],
                 mfgr=item[2],
                 brand=item[3],
                 type=item[4],
                 size=item[5],
                 container=item[6],
                 retailprice=item[7],
                 comment=item[8]
                 )

        parts.append(p)

    return parts


def find_max_price(parts):
    ''' Find the max in a Part List '''
    max_retailprice = 0.0
    max_part = None
# We do linear search in the list
    for part in parts:
        if(part.retailprice > max_retailprice):
            max_retailprice = part.retailprice
            max_part = part

    return max_part


def find_duplicates(parts):
    duplicates=[]
    while parts:
        part = parts.pop()
        if part in parts:
            duplicates.append(part)
    
    return duplicates


def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):

        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

@profile
def main():
    # filename = sys.stdin.read()
    parser = argparse.ArgumentParser(description='Example Program')

    parser.add_argument('--filename', type=str, default='./datasets/part.tbl',
                           help='use the correct input file.')

    args = parser.parse_args()

    lines = read_lines(args.filename)
    values = parse_lines(lines)
    converted_results = convert_toNumbers(values)

    # print(converted_results[0])
    parts = convert_to_parts(converted_results)
    # print(parts[0].retailprice)

    max_part = find_max_price(parts)
    print(max_part)

    duplicates = find_duplicates(parts)
    for part in duplicates:
        print(part)


if __name__ == "__main__":
    main()
