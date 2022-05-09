from bit import Key
from threading import Thread
import time
import sys

class parameters:
    loop = True
    t = 0
    ms = 0
    st = 0
    ds = 0
    p2s = "Address.txt"
    op = ""
    p2pf = ""

class score:
    total = 0
    found = 0

def array(array_pattern):
    try:
        while parameters.loop:
            key = Key()
            address = key.address
            for pattern in array_pattern:
                if (address[1:len(pattern)+1] == pattern):
                    wif = key.to_wif()
                    print(f"\n Address : {address}\n Wif : {wif}\n")
                    if parameters.ds == 0:
                        try:
                            with open(parameters.p2s, "a") as w:
                                w.write(f"Address - {pattern} : {address} | Wif : {wif}\n")
                        except:
                            print("\n ERROR : Failed to save result.")
                    if parameters.st == 1:
                        parameters.loop = False
                    score.found += 1
            score.total += 1
    except Exception as e:
        print(f"\n ERROR : {e}.")
        exit()

def one(pattern):
    try:
        while parameters.loop:
            key = Key()
            address = key.address
            if (address[1:len(pattern)+1] == pattern):
                wif = key.to_wif()
                print(f"\n Address : {address}\n Wif : {wif}\n")
                if parameters.ds == 0:
                    try:
                        with open(parameters.p2s, "a") as w:
                            w.write(f"Address - {pattern} : {address} | Wif : {wif}\n")
                    except:
                        print("\n ERROR : Failed to save result.")
                score.found += 1
                if parameters.st == 1:
                    parameters.loop = False
            score.total += 1
    except Exception as e:
        print(f"\n ERROR : {e}.")
        exit()

def times():
    while parameters.loop:
        start_total = score.total
        time.sleep(1)
        speed = score.total - start_total
        print(f" Found : {score.found} | Total : {score.total} | Generation : {speed} /s")

def help():
    print(f""" Use : bag.py [-h] [-t %] [-ms] [-st] [-op %] [-ds] [-p2s %] [-p2pf %]
  [-h] - help message
  [-t] - number of threads
  [-ms] - max speed (no notifications)
  [-st] - stop after finding
  [-ds] - disable saving
  [-p2s] - path to save (standard "ADDRESS.TXT")
  [-op] - one pattern
  [-p2pf] - path to patterns file
  
 Enter without the front unit.
  
 Example:
  bag.py -t 2 -p2s addresses.txt -p2pf pattern.txt
  bag.py -t 2 -ms -ds -op address
""")

def level(len_pattern):
    if len_pattern > 0 and len_pattern <= 2:
        return "│░│░│░│░│░│"
    elif len_pattern > 2 and len_pattern <= 3:
        return "│█│░│░│░│░│"
    elif len_pattern > 3 and len_pattern <= 4:
        return "│█│█│░│░│░│"
    elif len_pattern > 4 and len_pattern <= 5:
        return "│█│█│█│░│░│"
    elif len_pattern > 5:
        return "│█│█│█│█│█│"

def main():
    print("""
 ┌────────┐ ┌────────┐
 █████████┘ █████████┘
 ██│  ┌───┐ ██└──────┐
 ██│  ████│ █████████│ GREYSERG.bag
 ██└────██│ ┌──────██│ 0.1
 █████████┘ █████████┘
""")
    ar = 0
    for ar in range(len(sys.argv)):
        if sys.argv[ar] == "-h":
            help()
            exit()
        elif sys.argv[ar] == "-t":
            ar += 1
            try:
                parameters.t = int(sys.argv[ar])
            except:
                print(f"\n ERROR : Incorrect number of threads.")
                exit()
        elif sys.argv[ar] == "-ms":
            parameters.ms = 1
        elif sys.argv[ar] == "-st":
            parameters.st = 1
        elif sys.argv[ar] == "-ds":
            parameters.ds = 1
        elif sys.argv[ar] == "-p2s":
            ar += 1
            parameters.p2s = sys.argv[ar]
        elif sys.argv[ar] == "-op":
            ar += 1
            parameters.op = sys.argv[ar]
        elif sys.argv[ar] == "-p2pf":
            ar += 1
            parameters.p2pf = sys.argv[ar]
    if 0 >= ar or ar >= 10:
        help()
        exit()
    if parameters.t <= 0:
        print(f"\n ERROR : Incorrect number of threads.")
        exit()
        
    if parameters.p2pf != "":
        try:
            with open(parameters.p2pf, "r") as f:
                array_pattern = [i.strip() for i in f]
        except:
            print(f"\n ERROR : Could not open the file - {parameters.p2pf}.")
            exit()
        
        for pattern in array_pattern:
            if len(pattern) <= 0 or len(pattern) >= 34:
                print(f"\n ERROR : Incorrect pattern length - \"{pattern}\".")
                exit()
            for letter in pattern:
                if (letter >= 'a' and letter <= 'k' or letter >= 'm' and letter <= 'z' or letter >= 'A' and letter <= 'H' or letter >= 'J' and letter <= 'N' or letter >= 'P' and letter <= 'Z' or letter >= '1' and letter <= '9'):
                    pass
                else:
                    print(f"\n ERROR : Invalid character - \"{pattern}\".")
                    exit()
        print(" Level: " + level(len(min(array_pattern, key=len))) + " - " + level(len(max(array_pattern, key=len))))
        for _ in range(parameters.t):
            Thread(target=array, args=(array_pattern, )).start()
    
    if parameters.op != "":
        if len(parameters.op) <= 0 or len(parameters.op) >= 34:
            print(f"\n ERROR : Incorrect pattern length.")
            exit()
        for pattern in parameters.op:
            if (pattern >= 'a' and pattern <= 'k' or pattern >= 'm' and pattern <= 'z' or pattern >= 'A' and pattern <= 'H' or pattern >= 'J' and pattern <= 'N' or pattern >= 'P' and pattern <= 'Z' or pattern >= '1' and pattern <= '9'):
                pass
            else:
                print(f"\n ERROR : Invalid character - \"{pattern}\".")
                exit()
        print(" Level: " + level(len(parameters.op)))
        for _ in range(parameters.t):
            Thread(target=one, args=(parameters.op, )).start()
    if parameters.ms == 0:
        Thread(target=times).start()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n ERROR : {e}.")
        exit()