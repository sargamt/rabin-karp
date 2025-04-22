import time
import tracemalloc
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
    h_old = hash_function(text[0:(len(pattern))]) # length of ascii hash   
    if h_old == hpattern and pattern == text[i:i+3]:
        num += 1
    for i in range(1, len(text)-len(pattern)+1):
        h_new = ((256 * (h_old - (ord(text[i-1]) * ((256) ** (len(pattern)-1)))))  + ord(text[i+len(pattern)-1])) % 101
        h_old = h_new
        if h_new == hpattern and pattern == text[i:i+3]:
            num += 1
    end_time = time.process_time()
    cpu_time = end_time-start_time
    return num, cpu_time

# print("Occurrences:", rabin_karp("XYZ", "cjoisdCCBiodjCCB"))

s1 = 'abc' * 30000
s2 = 'abc' * 60000
s3 = 'abc' * 90000
s4 = 'abc' * 120000
s5 = 'abc' * 150000
s6 = 'abc' * 180000
s7 = 'abc' * 210000
s8 = 'abc' * 240000

print("String Length (characters):", len(s1), "     CPU Time:", rabin_karp("XYZ", s1)[1]) # 90k characters
print("String Length (characters):", len(s2), "     CPU Time:", rabin_karp("XYZ", s2)[1]) # 180k characters
print("String Length (characters):", len(s3), "     CPU Time:", rabin_karp("XYZ", s3)[1]) # 270k characters
print("String Length (characters):", len(s4), "     CPU Time:", rabin_karp("XYZ", s4)[1]) # 360k characters
print("String Length (characters):", len(s5), "     CPU Time:", rabin_karp("XYZ", s5)[1]) # 450k characters
print("String Length (characters):", len(s6), "     CPU Time:", rabin_karp("XYZ", s6)[1]) # 540k characters
print("String Length (characters):", len(s7), "     CPU Time:", rabin_karp("XYZ", s7)[1]) # 630k characters
print("String Length (characters):", len(s8), "     CPU Time:", rabin_karp("XYZ", s8)[1]) # 720k characters

tracemalloc.start()
rabin_karp("1234567890", s1)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
rabin_karp("12345678901234567890", s1)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
rabin_karp("123456789012345678901234567890", s1)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
rabin_karp("1234567890123456789012345678901234567890", s1)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

tracemalloc.start()
rabin_karp("12345678901234567890123456789012345678901234567890", s1)
print(tracemalloc.get_traced_memory())
tracemalloc.stop()



# algorithm without cpu time and memory usage measurements

# def hash_function(pattern):
#     h = 0
#     for i in range(len(pattern)):
#         h += ord(pattern[i]) * ((256) ** (len(pattern)-i-1)) 
#     h = h % 101
#     return h

# def rabin_karp(pattern, text):
#     count = 0
#     hpattern = hash_function(pattern)
#     h_old = hash_function(text[0:(len(pattern))]) 
#     if h_old == hpattern and pattern == text[i:i+3]:
#         count += 1
#     for i in range(1, len(text)-len(pattern)+1):
#         h_new = ((256 * (h_old - (ord(text[i-1]) * ((256) ** (len(pattern)-1)))))  + ord(text[i+len(pattern)-1])) % 101
#         h_old = h_new
#         if h_new == hpattern and pattern == text[i:i+3]:
#             count += 1
#     return count