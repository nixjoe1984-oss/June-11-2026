td={
    "Coding":3,
    "is":2,
    "best":2,
    "for":2,
    "you":1
}
print("Original test dictonary: "+str(td))
k=int(input("Enter a number(1,2 or 3): "))
count=0
for key in td:
    if td[key]==k:
        count+=1
print("Frequency of the number",k,"is: "+str(count))