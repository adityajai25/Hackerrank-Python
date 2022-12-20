if __name__ == '__main__':
    N = int(input())
    mylst = []
    for i in range(0,N):
        command = input().split()
        if(command[0] == "insert"):
            mylst.insert(int(command[1]),int(command[2]))
        elif(command[0] == "print"):
            print(mylst)
        elif(command[0] == "remove"):
            mylst.remove(int(command[1]))
        elif(command[0] == "append"):
            mylst.append(int(command[1]))
        elif(command[0] == "sort"):
            mylst.sort()
        elif(command[0] == "reverse"):
            mylst.reverse()
        elif(command[0] == "pop"):
            mylst.pop()
            
