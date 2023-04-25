def find_even_numbers(n):
    evens = []
    for i in range(n+1):#WE ADD 1 SO WHEN WE PUT A NUMBER LIKE 10(EVEN) IT RETURNS IT.
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(5))