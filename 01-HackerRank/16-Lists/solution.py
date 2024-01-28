if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command = input().split()
        cmd = command[0]

        if cmd == 'insert':
            i, e = map(int, command[1:])
            lst.insert(i, e)
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            e = int(command[1])
            lst.remove(e)
        elif cmd == 'append':
            e = int(command[1])
            lst.append(e)
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
