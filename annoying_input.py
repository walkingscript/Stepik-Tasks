def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            x = int(input())
        except ValueError:
            print(error_message)
            continue
        break
    print(end_message)
    return x
