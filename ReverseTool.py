import os

path0 = "C:/Users/" + os.getlogin() + "/"
    

try:
    path = path0 + input("Please Enter the path your infecting.. " + "\nC:/Users/" + os.getlogin() + "/")
    if path[len(path) - 1] != "/":
        path = path + "/"
    files = os.listdir(path)
except:
    print("Invalid Path\n")
    path = path0 + input("Please Enter the path your infecting.. " + "\nC:/Users/" + os.getlogin() + "/")
    if path[len(path) - 1] != "/":
        path = path + "/"
    files = os.listdir(path)

def reverse(string):
    string = "".join(reversed(string))
    return string

for i in files:
    if os.path.isdir(path + i):
        os.rename(path+i, path+reverse(i))
        print(i + " is a folder that's INFECTED")

    if os.path.isfile(path + i):
        os.rename(path+i, path+reverse(i))
        print(i + " is a file that's INFECTED")

