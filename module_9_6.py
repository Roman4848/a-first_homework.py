def all_variants(text):
    
    subsequences = []

    for start in range(len(text)):

        for end in range(start + 1, len(text) + 1):
            subsequences.append(text[start:end])
    subsequences.sort(key=len)

    for subseq in subsequences:
        yield subseq


a = all_variants("abc")
for i in a:
    print(i)