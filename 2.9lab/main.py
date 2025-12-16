#вар9
def is_symmetric(m):
    """Проверяет симметричность матрицы"""
    n = len(m)
    for i in range(n):
        for j in range(i+1, n):
            if abs(m[i][j] - m[j][i]) > 1e-10:
                return False
    return True

def process_matrices():
    """Основная функция в краткой форме"""
    with open("matrices.txt", 'r') as f:
        k = int(f.readline())
        mats = []
        for _ in range(k):
            n = int(f.readline())
            mat = [list(map(float, f.readline().split())) for _ in range(n)]
            mats.append((n, mat))
    
    sym, non_sym = [], []
    for n, mat in mats:
        if is_symmetric(mat):
            sym.append((n, mat))
        else:
            non_sym.append((n, mat))
    
    # Запись в файлы
    for name, data in [("sym.txt", sym), ("non_sym.txt", non_sym)]:
        with open(name, 'w') as f:
            f.write(f"{len(data)}\n")
            for n, mat in data:
                f.write(f"{n}\n")
                for row in mat:
                    f.write(" ".join(f"{x:.4f}" for x in row) + "\n")
    
    # Вывод на экран
    for name in ["matrices.txt", "sym.txt", "non_sym.txt"]:
        print(f"\n{name}:")
        with open(name, 'r') as f:
            print(f.read())
