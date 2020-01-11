while 1:
    try:
        inp = input()
        resul=""
        for s in inp:
            if s=='l':
                resul+='1'
            elif s=='o' or s=='O':
                resul+='0'
            elif s==',' or s==' ':
                pass
            else:
                resul+=s
        try:
            number = int(resul)
            if number>2147483647:
                print("error")
            else:
                print(number)
        except:
            print("error")
    except EOFError:
        break