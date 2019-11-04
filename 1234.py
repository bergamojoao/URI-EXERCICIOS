while True:
    try:
        word = input()
        upper=True
        new=""
        for w in word:
            if w != ' ':
                if upper:
                    new+=w.upper()
                    upper=False
                else: 
                    new+=w.lower()
                    upper=True
            else: new+=' '
        print(new)
    except EOFError:
        break