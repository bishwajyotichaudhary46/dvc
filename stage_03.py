with open("artifact.txt","r") as f:
    text = f.read()

print(text)

with open("artifact.txt","w") as f:
    text = f.write(text+"i write some")

print(text)
print("it is end of stage 3")