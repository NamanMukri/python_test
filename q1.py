def display_result(string1):
    for i in range(len(string1)):
        if i%2==0:
            print(string1[i])
        continue

if __name__=="__main__":
    str=input("Enter String: ")
    display_result(str)
