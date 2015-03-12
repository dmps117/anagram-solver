import fileinput, string


filein = fileinput.input(['a-z'])
letters = list(string.lowercase)

for letter in letters:
    f = open(letter, 'w')
    lines = [line.rstrip() for line in filein if line.startswith(letter)]
    # import ipdb; ipdb.set_trace()
    for line in lines:
        f.write('{}\n'.format(line))
    import ipdb; ipdb.set_trace()
    f.close()
