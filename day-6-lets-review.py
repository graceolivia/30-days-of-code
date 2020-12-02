# Enter your code here. Read input from STDIN. Print output to STDOUT

num = input()
for i in num:

print(word + word2 + word3)
evens = ""
odds = ""

for i in range(len(word)):
    if i % 2 == 0:
        evens = evens + word[i]
        print(evens)
    else:
        odds = odds + word[i]
        print(odds)

print(odds)
print(evens)
