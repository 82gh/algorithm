month = int(input())
if(month % 12 <= 2):
    print("winter")
elif(month % 12 <= 5):
    print("spring")
elif(month % 12 <= 8):
    print("summer")
elif(month % 12 <= 11):
    print("fall")
