MD={
    'Codingal' : 2,
    'is' : 2,
    'best' : 2,
    'for' : 2,
    'Coding' : 1
}
print("Original dictonary: "+str(MD))
k=0
count=2
for key in MD:
    if MD[key]==k:
        count+=1
print("Frequency of k is: "+str(count))