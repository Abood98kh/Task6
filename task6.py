# Question 1:
lst = [30, 75, 9, 97, 50, -4, 70, 59]
print((max(lst)))
lst.remove(min(lst))
lst.sort()
# this is the answer to point 4 in question 1 but it's not the same as the output
print(lst[:-5:-1])
# this is the output shown in the task:
lst.reverse()
print(lst[:-5:-1])
# Question 2:
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
python_times = 0
for item in main_lst:
    item.count("python")
    python_times = python_times + item.count("python")
print(python_times)
# Question 3:
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
sentence = ''
for element in my_lst:
    if element != my_lst[-1]:
        sentence = sentence + f'{element} '
    else:
        sentence = sentence + f'{element}'
print(sentence.title())
# Question 4:
my_lst_2 = [12, 3.8, "GSG", ["sKy", "zak"]]
copied_lst = []
for elem in my_lst_2:
    copied_lst.append(elem)
print(copied_lst)
# Question 5:
my_lst_3 = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst_3[2], my_lst_3[4] = my_lst_3[4], my_lst_3[2]
print(my_lst_3)
# Question 6:
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
sum = 0
for num in nums:
    sum = sum + num
print(sum)
# *******************************************************************
## This is a code if you have strings in the list:
# for num in nums:
#     if isinstance(num, int):
#         sum = sum + num
#     elif isinstance(num, float):
#         sum = sum + num
#     else:
#         continue
# print(sum)
# *******************************************************************
# Question 7 & 8:
tuple_1 = (4, 'python', 'GSG', [8, 3, 1])
tuple_1 = tuple_1 + (9,)
print(tuple_1)
tuple_1 = (4, 'python', 'GSG', [8, 3, 1])
tuple_2 = ('Java', 'C++', 7.8)
new_tuple = tuple_1 + tuple_2
print(new_tuple)