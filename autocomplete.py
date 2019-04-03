def autoComplete(s,ls):
    found = []
    for l in ls:
        if(l.startswith(s)):found.append(l)
    return found

if __name__ == "__main__":
    print(autoComplete('de',['dog', 'deer', 'deal']))
