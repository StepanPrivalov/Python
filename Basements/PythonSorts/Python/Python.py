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


'''
a = int(input("Enter number: "))
count = 0
temp = a
while temp > 0:
	count += 1
	temp //= 10
num = [0] * count
count -= 1
i = 0
while (count) >= 0:
	num[count] = a // (10 ** i) % 10
	i += 1
	count -= 1


res = num[0:2]
for j in range(1, len(num) - 1):
	temp = num[j:j+2]
	if temp > res:
		continue
	else:
		res = temp


print(*num)
print(*res, sep = "")
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

def lcs(A, B):
	#Выводит саму подпоследовательность и ее длину
	F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i-1] == B[j-1]:
				F[i][j] = 1 + F[i-1][j-1]
			else:
				F[i][j] = max(F[i][j-1], F[i-1][j])
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in F]))
	f = F[-1][-1]
	nums = []
	i = len(A) 
	j = len(B) 
	while True:
		if j == 0 or i == 0:
			break
		if F[i][j - 1] == f:
			j -= 1
		elif F[i - 1][j] == f:
			i -= 1
		else:
			nums.append(A[i - 1])
			i -= 1
			j -= 1
			f = F[i][j]
	print(*nums[::-1])
			
	return F[-1][-1]

def gis(A):
	#НВП - наибольшая возрастающая подпоследовательность
	F = [0] * (len(A))
	for i in range(len(A)):
		m = 0
		for j in range(i):
			if A[i] > A[j] and F[j] > m:
				m = F[j]
				print(m + 1, "(", A[i], A[j], ")",  end = ", ")
		F[i] += m + 1
	return F[len(A) - 1]

#https://youtu.be/m4HOkVeN4Mo?t=626

def isDigitInNum(num, digit):
	while num > 0:
		if digit == (num % 10):
			print("YEP")
			return True
		num //= 10
	print("NOPE")
	return False


'''
a = list(input())
for i in range(len(a)):
	a[i] = int(a[i])
res = [0] * len(a)
tries = 0

while True:
	count = 0
	tries += 1
	for i in range(len(a)):
		if res[i] == a[i]:
			count += 1
	if count == len(a):
		break




	if res[-1] == 9:
		if res[-2] == 9:
			if res[-3] == 9:
				res[-3] = 0
				res[0] += 1
			else:
				res[-2] = 0
				res[-3] += 1
		else:
			res[-1] = 0
			res[-2] += 1
	else:
		res[-1] += 1

	
print(*res)
print("All tries -", tries)
'''



def MagickCube():
	sum, temp = 0, 0
	n = int(input("Enter the length of cube:"))

	cube = [[0] * n for i in range(n)]
	for i in range(n):
		for j in range(n):
			cube[i][j] = int(input())
		sum += cube[i][i]

	for row in cube:#chek sum in row
		for elem in row:
			temp += elem
		if temp != sum:
			print("Nope")
			return "Nope"
		temp = 0

	for j in range(n):#check sum in column
		for i in range(n):
			temp += cube[i][j]
		if temp != sum:
			print("Nope")
			return "Nope"
		temp = 0

#and 2 diagonals 
	for i in range(n):
		temp += cube[i][i]

	if temp != sum:
			return "Nope"
	temp = 0

	for i in range(n - 1, -1, -1):
		temp += cube[i][i]

	if temp != sum:
			return "Nope"
	temp = 0

	for row in cube:
		print(' '.join([str(elem) for elem in row]))
	print("Yep")

MagickCube()