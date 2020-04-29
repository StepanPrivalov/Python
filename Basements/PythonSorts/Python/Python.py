'''Экранирование
from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.GREEN(BLACK, etc.) окрашивает цвет фона при выводе в терминале
print("He's a \" bad\" man") or print('He has a "bass"')
Формат вывода
a = 10.625
print("{:.2f}".format(a))'''
'''Конкатинация
age = input()
print("u're " + age + " y.o.")'''

'''Калькулятор(+, -)
	what = input("What re we doing(+, -): ")
	print("Enter 2 nums: ")
	a, b = map(float, input.split())

	if what == "+":
		print("Res = ", a + b)
	elif what == "-":
		print("Res = ", a - b)
	else:
		print("Invalid Operator")

'''

'''Работа с погодой
import pyowm
owm is openWeatherMap
owm = pyowm.OWM('your-API-key') api-key from their official site
place = input("The weather of what city u re intereted in?(city, country): ")

observation = owm.weather_at_place('place', Language = "ru") language argument translates the answer
w = observation.get_weather()
now from var w we can get all that we need: temp, humidity, wind, status = cloud and etc.
print(w)        
w.get_wind() 
w.get_humidity()
w.get_temperature('celsius')


'''

'''
# сортировка слиянием: слияние отсортированнных массивов в один
# сортировка меняет оригинальный массив а не создает новый
def merge(A:list, B:list):
	C = [0] * (len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			n += 1
			k += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C

def mergeSort(A:list):
	if len(A) <= 1:
		return
	middle = len(A) // 2
	l = [A[i] for i in range(middle)]
	r = [A[i] for i in range(middle, len(A))]
	mergeSort(l)
	mergeSort(r)
	C = merge(r, l)
	for i in range(len(C)):
		A[i] = C[i]

# сортировка тони хоара: быстрая сортировка
def hoarSort(A:list):
	if len(A) <= 1:
		return
	bar = A[0]
	l, m, r = [], [], []
	for x in A:
		if x < bar:
			l.append(x)
		elif x == bar:
			m.append(x)
		else:
			r.append(x)
	hoarSort(l)
	hoarSort(r)
	for x, k in l + m + r, range(len(A)):
		A[k] = x

#проверка упорядоченности массива за O(N)
def checkSorted(A, ascending = True):
	flag = True
	s = 2 * int(ascending) - 1
	for i in range(N - 1):
		if s * A[i] > s * A[i + 1]:
			flag = False
			break
	return flag

A = [5, 2 , 4, 1, 5, 8]
hoarSort(A)
print(A)
'''

'''
# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    print("partition")
    print(*nums)
    print(low, high)
    #pivot = nums[(low + high) // 2]
    pivot = nums[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            print("partition result:", *nums, "middle", pivot, "middle index", j)
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Verify it works
random_list_of_nums = [22, 5, 33, 1, 18, 101, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

'''

#бинарный поиск в отсортированном массиве

def leftBoundary(A, key):
	left = -1
	right = len(A)
	while right - left > 1:
		mid = (left + right) // 2
		if A[mid] < key:
			left = mid
		else:
			right = mid
	return left

def rightBoundary(A, key):
	left = -1
	right = len(A)
	while right - left > 1:
		mid = (left + right) // 2
		if A[mid] <= key:
			left = mid
		else:
			right = mid
	return right

def fib(n):
	''' асимптотика алгоритма ой какая большая
	не дело кароч'''
	if n <= 1:
		return n
	return (fib(n-1) + fib(n - 2))

def countTrajectories(n, allowed:list):
	'''Исполнитель кузнечик может передвигать 3 способами:
	1) +1 клеточка      2) +2 клеточки     3) +3 клеточки
	Существуют клетки на которые кузнечик наступать не может
	Нужно найти всевозможные пути в клеточку N
	'''
	K = [0, 1, int(allowed[2])] + [0] * (n - 3)
	for i in range(3, n + 1):
		if allowed[i]:
			K[i] = K[i-1] + K[i-2] + K[i-3]
	return K[n]

def countMinCost(n, price:list):
	'''Исполнитель кузнечик может передвигать двумя способами:
	1) +1 клеточка      2) +2 клеточки
	У каждой клеточки своя стоимость
	Нужно найти минимальную стоимость прохода до N начиная с 1
	'''
	# add allowed:list
	C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (n - 2)
	for i in range(3, n + 1):
		C[i] = price[i] + min(C[i - 1], C[i - 2])
	return C[n]

def countMinCostWithAllowed(n, price:list, allowed:list):
	'''Исполнитель кузнечик может передвигать двумя способами:
	1) +1 клеточка      2) +2 клеточки
	У каждой клеточки своя стоимость
	Существуют клетки на которые кузнечик наступать не может
	Нужно найти минимальную стоимость прохода до N начиная с 1
	'''
	C = [float("-inf"), price[1], price[1] + price[2] if allowed[2] else 0] + [0] * (n - 2)
	for i in range(3, n + 1):
		if allowed[i]:
			C[i] = price[i] + min(C[i - 1], C[i - 2])
	return C[n]

f1 = [1, 5, 0, 5, 1, 5, 2, 3, 4]
f2 = range(10)

def lcs(A, B):
	#Вывести саму подпоследовательность
	F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i-1] == B[j-1]:
				F[i][j] = 1 + F[i-1][j-1]
			else:
				F[i][j] = max(F[i][j-1], F[i-1][j])
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in F]))
	return F[-1][-1]

print(lcs(f1, f2))

#https://youtu.be/m4HOkVeN4Mo?t=626

''' quest1
a = []
s, res = 0, 0
n = int(input())
for i in range(n):
	a.append(int(input()))
	s += a[i]
s /= n
for i in range(n):
	if a[i] > s:
		res += 1
print(res)
'''

'''quest2
a=[]
n=30
for i in range (n):
    a.append(int(input()))
x=int(input())
for i in range (n):
    if x==a[i]:
        print(i)
        break
'''

'''quest3
a = []
n = int(input())
for i in range(n):
	a.append(int(input()))
m1, m2 = a[i], 0
for i in range(n):
	if m1 < a[i]:
		m1 = a[i]
		m2 = m1
	elif m2 < a[i] and m1 != a[i]:
		m2 = a[i]
print(m2)'''

'''quest 4
a=[]
n=5
k=0
for i in range (n):
    a.append(int(input()))
for i in range (n):
    if a[i]>0:
        k+=1
    if k==3:
        print(i)
        break
'''
'''quest5
a = []
n = int(input())
s1, s2 = 0, 0
for i in range(0, n):
	a.append(int(input()))
l1, l2 = 1, 0
for i in range(1, n):
	if a[i] > a[i - 1]:
		l1 += 1
		s1 += a[i]
	elif l2 < l1:
		l2 = l1
		s2 = s1
		l1 = 1
		s1 = a[i]
print(s2)
'''

'''quest6
a = []
n = int(input())
s = 0
for i in range(0, n):
	a.append(int(input()))
	s += a[i]
s /= n
k = 0
for i in range(1, n):
	if abs(a[i] - s) < abs(a[k] - s):
		k = i
print(k)
'''


''' telegram bot
import telebot
bot = telebot.TeleBot("TOKEN")
token u receive from botFather in telegram while creating a new bot'''


