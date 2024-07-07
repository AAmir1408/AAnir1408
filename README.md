x = input("Whats your name?")
print('Hello,',x,'my name is AAA')
count = 0
while True:
    friend = input("Who your friends?")
    if friend =='все':
        print("You have",count, "friends")
    else:
        count += 1
