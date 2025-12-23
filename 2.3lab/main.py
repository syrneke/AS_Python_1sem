#вар9
def InvertStr(S, K, N):
    if K > len(S):
        return ""
    start = K - 1
    end = min(start + N, len(S))
    return S[start:end][::-1]
print(InvertStr("Hello", 2, 3)) 
print(InvertStr("Hi", 3, 5)) 
print(InvertStr("Python", 3, 10)) 
