"""
You have been given a binary string containing only the characters "0" and "1". A binary string is considered valid if each of its 
substrings of at least a certain length contains at least one "1" character. Given the binary string, and the minimum length of 
substring, determine how many characters of the string need to be changed in order to make the binary string valid.

Note that string  v is a substring of string w if it has a non-zero length and can be read starting from some position in string w. 
For example, string "010" has six substrings: "0", "1", "0", "10", "01", "010".

For example, let's say the binary string s = "0001" of length n = 4, and the minimum substring length is d = 2. This is currently not
valid because one of its substrings, "000", of length 3 has no "1"s in it. By changing the second character to a "1", the string becomes
"0101". In this case, all of its substrings of length 2 or more has at least one "1" character: "01", "10", and "01". Because this 
required 1 change, the answer is 1.

Input Format

The first line contains the binary string, s.

The second line contains the integer d.

Constraints :
  1 <= n <= 10^6
  1 <= d <= n
  
Output Format

Print a single integer denoting the minimum number of changes required to make the binary string valid

Sample Input 0

00100
2
Sample Output 0

2
Explanation 0

We can make the string "10101" by changing the first and the last characters. Here, every substring with a length of at least 2 contains
at least one "1". There's no way to do this in less than 2 operations.

Therefore, the answer is 2.
"""

def minimumMoves(s, d):
    # Write your code here
    length = len(s)
    if d == length:
        if '1' in s:
            return 0
        return 1
    
    if '1' not in s:
        return int(math.floor(length/d))
    
    i = 0
    x = d
    count = 0
    
    while x <= length:
        if '1' not in s[i:x]:
            count += 1
            i = x 
            x += d
        else:
            for j in range(x-1, i-1, -1):
                if s[i] == '1':
                    indx = j
            
            i = j + 1
            x = d + i
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)

    fptr.write(str(result) + '\n')

    fptr.close()
