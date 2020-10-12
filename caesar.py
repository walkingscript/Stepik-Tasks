alphabet = ' abcdefghijklmnopqrstuvwxyz'

key = int(input())
text = input().lower()
length = len(alphabet)

encode_list = [alphabet[(alphabet.index(c)+key) % length] for c in text]
encoded_text = ''.join(encode_list)

print(f'Result: "{encoded_text}"')
