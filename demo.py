from recursion import factorial, sum_list, binary_search
from stack import Stack

print("=== Факториал ===")
for n in [0, 1, 5, 10]:
    print(f"{n}! = {factorial(n)}")

print("\n=== Сумма списка ===")
data = [1, 2, 3, 4, 5, 100]
print(f"Список: {data}")
print(f"Сумма:  {sum_list(data)}")

print("\n=== Бинарный поиск (рекурсивный) ===")
sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Массив: {sorted_arr}")
for target in [1, 9, 19, -5, 100, 7]:
    idx = binary_search(sorted_arr, target)
    if idx != -1:
        print(f"  {target} найден по индексу {idx}")
    else:
        print(f"  {target} не найден, результат = -1")

print("\n=== Стек ===")
s = Stack()
print(f"Пустой? {s.is_empty()}")

s.push(10)
s.push(20)
s.push(30)
print(f"После push(10, 20, 30): {s}")
print(f"peek() = {s.peek()} (не убирает)")
print(f"pop()  = {s.pop()} (убирает)")
print(f"pop()  = {s.pop()}")
print(f"Сейчас в стеке: {s}")
print(f"Пустой? {s.is_empty()}")
s.pop()
print(f"После ещё одного pop: пустой? {s.is_empty()}")