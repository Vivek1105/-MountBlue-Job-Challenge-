def decent_number(N):
    """
    Prints a decent number of N digits. -1 if no such number exists.
    """
    
    for fives in range(N, -1, -1):
        threes = N - fives
        if fives % 3 == 0 and threes % 5 == 0:
            return "5" * fives + "3" * threes
    return "-1"
    
def main():
    
    import sys
    
    count, *Ns = sys.stdin.readlines()
    
    for N in Ns:
        print(decent_number(int(N)))
    
if __name__ == "__main__":
    main()
