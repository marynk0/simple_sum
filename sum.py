def main():
    user_input= input("Insert numbers here:")
    x,y,z = user_input.split(",")
    x= int(x)
    y= int(y)
    z= int(z)
    sum = (x+y+z)
    print(sum)  
if __name__ == "__main__":
    while True:
        main()