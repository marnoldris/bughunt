import time

indent = 0
indentIncreasing = True

    while True:
        print(f' ' * indent, end='')
        print(f'**************')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent % 20 == 0:
                indentIncreasing = alse
        else:
            indent = indent
            if indent <= 0:
                indentIncreasing = True
