import json
def main():
    Dictionary = open("Dictionary.json",'r')
    t = json.load(Dictionary)
    x = input("Enter U:For User or D:for Developer: ")
    if x == 'U':
        u(t)
    else:
        d(t)

def u(t):
    while True:
        English = input("English word:")
        if English == 'exit':
            break
        print(t[English])
        

def d(t):
    while True:
        English = input("English word:")
        if English == 'exit':
            break
        Arabic = input("Arabic word:")
        t[English]=Arabic
    Dictionary = open("Dictionary.json",'w')
    json.dump(t,Dictionary)

main()
