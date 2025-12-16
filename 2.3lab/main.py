#вар9
def InvertStr(S, K, N):
    """Возвращает инвертированную подстроку строки S с позиции K длиной N символов"""
    if K > len(S):
        return ""
    
    start = K - 1
    end = min(start + N, len(S))
    
    return S[start:end][::-1]

print(InvertStr("Hello", 2, 3))  # "leH" (подстрока "ell" → "lle")
print(InvertStr("Hi", 3, 5))     # "" (K > длины)
print(InvertStr("Python", 3, 10)) # "nohtyP" (с 3-го до конца: "thon" → "noht")
