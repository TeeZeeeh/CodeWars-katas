# Code by Tajrina Promela
# Date 7th November 2022, 9:46 AM
# Program that returns the first longest string consisting of k strings taken in array

'''
# Thinking process
strn = []
strn = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz", 'dfvdf']
enList = [len(word) for word in strn]
print(enList)
res = ' '.join(strn[:2]) + ' ' + ''.join(strn[-2:])
print(res)

print(strn[0:3]) # if k=3
print(strn[2:5])
print(strn[4:7])

print(strn[0:2]) # if k=2
print(strn[1:3])
print(strn[2:4])

print(strn[0:1]) # if k=1
print(strn[1:2])
print(strn[2:3]) 

strn = ["zones", "abigail", "theta", "form", "libe"]
for string in range(len(strn)):
    print(len(strn[string]))
for string in strn:
    print(range(len(string)))



# 1st Method: Found max resultant string from consecutively combined k strings

def longest_consec(strarr, k):
    strarr.append('')
    length = len(strarr)
    cons_list = []
    end = k
    start = 0
    freq = -length/2
    final_string = []
    largest = max(strarr, key=len, default='')
    if k == 1:
        return largest
    elif 1 < k < length:
        while(freq <= 1):
            cons_list.append(strarr[start:end])
            start += k-1
            end += k-1
            freq += 1
        for index in cons_list:
            final_string.append(''.join(index))
        return max(final_string, key=len, default=0)  
    else:
        return ""

print(longest_consec(["zone", "abigail", "theta", "form", "libe"], 3))


# 2nd Method: Compared lengths on both sides of largest single string
# Not consecutively combined
# Doesn't account for case when largest single string is in middle


def longest_consec(strarr, k):
    strarr.append('0')
    length = len(strarr)
    largest = max(strarr, key=len, default=0)
    pos = int(strarr.index(largest))
    if k == 1:
        return largest
    elif 1 < k < length:
        prev_string = ''.join(strarr[pos+1-k:pos+1])
        middle_string = ''.join(strarr[pos+1-k:pos+1])
        next_string = ''.join(strarr[pos:pos+k])
        if len(prev_string) >= len(next_string):
            res = prev_string
        else: 
            res = next_string
        return res
    else:
        return ""

'''

# 3rd Method

def longest_consec(strarr, k):
    index = 0
    largest = ''
    res = ''
    if (k <= 0) or (k > len(strarr)):
        return ''
    while index <= (len(strarr) - k):
        start = ''.join(strarr[index:index+k])
        largest = max(largest, start, key=len)
        if largest == start:
            res = strarr[index:index+k]
        index += 1
    return largest

print(longest_consec(["zones", "abigail", "theta", "form", "libe"], 3))