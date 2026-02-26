def merge_without_extra_space(a, b):
    n, m = len(a), len(b)

    def next_gap(g):
        if g <= 1:
            return 0
        return (g // 2) + (g % 2)

    gap = next_gap(n + m)

    while gap > 0:
        i = 0


        while i + gap < n:
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
            i += 1


        j = gap - n if gap > n else 0
        while i < n and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1

    
        if j < m:
            j = 0
            while j + gap < m:
                if b[j] > b[j + gap]:
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1

        gap = next_gap(gap)


# Example 
a1 = [2, 4, 7, 10]
b1 = [2, 3]
merge_without_extra_space(a1, b1)
print(a1, b1)

a2 = [1, 5, 9, 10, 15, 20]
b2 = [2, 3, 8, 13]
merge_without_extra_space(a2, b2)
print(a2, b2)

a3 = [0, 1]
b3 = [2, 3]
merge_without_extra_space(a3, b3)
print(a3, b3)