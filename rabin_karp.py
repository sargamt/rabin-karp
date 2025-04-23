def hash_function(pattern):
    h = 0
    for i in range(len(pattern)):
        h += ord(pattern[i]) * ((256) ** (len(pattern)-i-1)) 
    h = h % 101
    return h

def rabin_karp(pattern, text):
    count = 0
    hpattern = hash_function(pattern)
    h_old = hash_function(text[0:(len(pattern))]) 
    if h_old == hpattern and pattern == text[i:i+3]:
        count += 1
    for i in range(1, len(text)-len(pattern)+1):
        h_new = ((256 * (h_old - (ord(text[i-1]) * ((256) ** (len(pattern)-1)))))  + ord(text[i+len(pattern)-1])) % 101
        h_old = h_new
        if h_new == hpattern and pattern == text[i:i+3]:
            count += 1
    return count

pattern = "XYZ"
text = "abcdefXYZghijklmnoXYZpqrstuvwXYZ"

print(f"Number of Occurrences of \"{pattern}\":", rabin_karp(pattern, text))