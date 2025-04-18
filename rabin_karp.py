import time
def hash_function(pattern):
    h = 0
    for i in range(len(pattern)):
        h += ord(pattern[i]) * ((256) ** (len(pattern)-i-1)) 
    h = h % 101
    return h

def rabin_karp(pattern, text):
    start_time = time.process_time()
    num = 0
    hpattern = hash_function(pattern)
    # print("hpattern: ", hpattern)
    h_old = hash_function(text[0:(len(pattern))]) #length of ascii hash   
    if h_old == hpattern and pattern == text[i:i+3]:
        num += 1
    for i in range(1, len(text)-len(pattern)+1):
        h_new = ((256 * (h_old - (ord(text[i-1]) * ((256) ** (len(pattern)-1)))))  + ord(text[i+len(pattern)-1])) % 101
        # print("i: ",i, "    hnew: ", h_new)
        h_old = h_new
        if h_new == hpattern and pattern == text[i:i+3]:
            num += 1
    end_time = time.process_time()
    cpu_time = end_time-start_time
    print("CPU Time:", cpu_time, "seconds")
    return num

print("Occurrences:", rabin_karp("CCB", "cjoisdCCBiodjCCB"))

# print(hash_function("cjo"))
# print(hash_function("joi"))
# print(hash_function("dCC"))


# cjoisdCCBiodjCCB
# 0123456789012345
     
#aaabbb
#123456
# ...
