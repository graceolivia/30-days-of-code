# Enter your code here. Read input from STDIN. Print output to STDOUTp\\\\\\
#take in the input
# then split the name/phone combos and add to dict
#search dict for each one

n = int(input())
dictn = dict()
for i in range(n):
    pair = input()
    pair = pair.split()
    dictn.update({pair[0]:pair[1]})


while(1):
    try:
        name = input()
        if name in dictn:
            print("{}={}".format(name, dictn[name]))
        else:
            print("Not found")
    except:
        break
