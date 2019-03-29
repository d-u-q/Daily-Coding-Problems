def LowestMissingInt(ln):
        for i in enumerate(ln): # Sorting the list via insertion sort
            index = i[0]
            val = i[1]
            while index > 0 and ln[index-1] > val:
                ln[index] = ln[index-1]
                index = index-1
            ln[index] = val
        print(ln)

        missing = ln[-1]+1
        for j in range(len(ln)-1):
            x = ln[j]
            if x != ln[j+1] and x+1 != ln[j+1] and x>0: missing = x+1
        return missing

if __name__ == "__main__":
    print(LowestMissingInt([3,4,-1,1]))
    print(LowestMissingInt([1,2,0]))