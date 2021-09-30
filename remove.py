#!/usr/bin/env python

"""
When  : 18/11/2015
Where : Home
What  : A program to remove duplicate words inside a wordlist
Why   : Because it seems like a good idea at that time,
        to know, understand or even create a better algorithm for it.
How   : With Sublime Text Editor and linux
"""

import timeit
import os

overwriteMode = True


def f7(seq):
    """
    The following function f7 is from this file.
    www.peterbe.com/plog/uniqifiers-benchmark/uniqifiers_benchmark.py
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def Convsize(filename):
    """
    This module's purpose is to convert the file size that
    is in Bytes to suitable human readable file size such as
    2 KB instead of 2324 bytes
    2.5 MB instead of 25235436 bytes
    """
    filesize = (os.path.getsize(filename) / (1024.0))
    if len(str(filesize)[:str(filesize).index('.')]) >= 3:
        # if the filesize has 3 or more digits on the left of the decimal place
        # it means it could be converted to MegaBytes
        return "%.2f MB" % (int(filesize) / 1024.0)
    else:
        return "%.2f KB" % (filesize)


def main(filename):
    print("[+] Original File Size : %s" % Convsize(filename))

    start_time = timeit.default_timer()
    content = [i.replace('\n', '') for i in open(filename, encoding="utf-8", errors="ignore").readlines()]
    # generates a list with the words inside wordlist without '\n'
    org_len = len(content)

    result = f7(content)
    stop_time = timeit.default_timer()
    duration = "%.5f" % (stop_time - start_time)
    # .5f to convert millisecond to seconds
    result_len = len(result)

    if not org_len == result_len:
        # That means original length and the resultant length is not the same
        # Which means there is duplication
        print("[+] Processed : [%s] Lines in %s seconds" % (org_len, duration))
        print("[+] <{:,}> duplicates found".format(org_len - result_len))
        # {:,} is a python built-in method to put 'commas' inside an integer
        if overwriteMode:
            newfilename = filename
        if not overwriteMode:
            newfilename = "%s-no-dup.txt" % (filename.replace('.txt', ''))
        newfile = open(newfilename, 'w')
        for i in result:
            newfile.write(i + '\n')
        newfile.close()
        print("[+] Saved as %s" % newfilename)
        print("[+] New File Size : %s" % (Convsize(newfilename)))

    else:
        print("[+] Processed : [%s] Lines in %s seconds" % (org_len, duration))
        print("[+] No Duplicates found")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("removeduplicate.py wordlist.txt")
    else:
        main(sys.argv[1])
