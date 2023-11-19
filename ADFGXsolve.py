from ADFGX_cryptosystem import part2

key = 'nobracket'
n = len(key)
key_index = [4, 2, 5, 7, 6, 0, 1, 3, 8]
key_reverse=[5, 6, 1, 7, 0, 2, 4, 3, 8]
letters = ["A", "D", "F", "G", "X"]
fd = open('output.txt', 'r')
output = fd.read()

print(len(output))

chunks = []

for i in range(0, len(output), len(output)//len(key)):
    chunk = output[i:i+(len(output)//len(key))]
    chunks.append(chunk)

assert ''.join(chunks) == output

pre_chunks = []

for i in range(len(output)//len(key)):
    pre_chunk = ''
    for chunk in chunks:
        pre_chunk += chunk[i]
    pre_chunks.append(pre_chunk)


new_chunks = []

for chunk in pre_chunks:
    new_chunk = ''
    for order in key_reverse:
        new_chunk += chunk[order]
    new_chunks.append(new_chunk)

assert part2(''.join(new_chunks)) == output

preciphertext = ''.join(new_chunks)

precipherlist = []

for i in range(0, len(preciphertext), 2):
    precipherlist.append(preciphertext[i:i+2])

for i in letters:
    for j in letters:
        print(i + j + ' : ' + str(precipherlist.count(i+j)*100/len(precipherlist))[:4] + '%')

file_out = open('pre_ciphertext', 'w')

file_out.write(preciphertext)

monoalpha = open('monoalphabet.txt', 'w')

decode = {
'A' : {'A' : 'A', 'D' : 'B', 'F' : 'C', 'G' : 'D', 'X' : 'E'},
'D' : {'A' : 'F', 'D' : 'G', 'F' : 'H', 'G' : 'I', 'X' : 'J'},
'F' : {'A' : 'K', 'D' : 'L', 'F' : 'M', 'G' : 'N', 'X' : 'O'},
'G' : {'A' : 'P', 'D' : 'K', 'F' : 'R', 'G' : 'S', 'X' : 'T'},
'X' : {'A' : 'U', 'D' : 'V', 'F' : 'X', 'G' : 'Y', 'X' : 'Z'}
}

for char in precipherlist[:-1]:
    monoalpha.write(decode[char[0]][char[1]])
