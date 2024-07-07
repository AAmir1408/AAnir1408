# AAnir1408
x = input("Whats your name?")
print('Hello,',x,'my name is AAA')
friends = []
count = int(input("Whos your friends?"))
for i in range(count):
    new_friend = input("Whos your friends?")
    friends.append(new_friend)
    count = len(friends)
    
print("You have",count, "friends")
