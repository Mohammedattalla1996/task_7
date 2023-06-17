#                                                     Q1
print(">>>>>>>>>>>Q1<<<<<<<<<<<<<<")
# name = ["Tarteel", "Asmaa", "Ahmed"]
# name.insert(0, "Sabrin")
# print(name)
# name.pop()
# print(name)
# name.append("Hamda")
# print(name)
# del name[2]
# print(name)

#                                                     Q2
print(">>>>>>>>>>>Q2<<<<<<<<<<<<<<")
# frinds = ["Adel", "Ahmed"]
# employees = ["Samah", "Amjad"]
# school = ["Ali", "Basma"]
# frinds.extend(employees)
# frinds.extend(school)
# print(frinds)

#                                                     Q3
print(">>>>>>>>>>>Q3<<<<<<<<<<<<<<")
# dic1 = {1: 10, 2:20}
# dic2 = {3: 30, 4:40}
# dic3 = {5: 50, 6:60}
# new_dic = dic1 | dic2 | dic3
# print(new_dic)

#                                                     Q4
print(">>>>>>>>>>>Q4<<<<<<<<<<<<<<")
# my_dic = {}
# for i in range(1, 15):
#     val = i * i
#     my_dic[i] = val
# print(my_dic)

#                                                     Q5
print(">>>>>>>>>>>Q5<<<<<<<<<<<<<<")
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 150, 'b': 200, 'd': 400}
#
# new_d = d2
# for m, a in d1.items():
#     if m in d2:
#         new_d[m] = a + d2[m]
#     else:
#         new_d[m] = a
# print(new_d)

#                                                     Q6
print(">>>>>>>>>>>Q6<<<<<<<<<<<<<<")
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# new_dict = {}
# for key in keys:
#     for value in values:
#         new_dict[key] = value
#         values.remove(value)
#         break
# print(new_dict)

#                                                     Q7
print(">>>>>>>>>>>Q7<<<<<<<<<<<<<<")
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# print(sampleDict['class']['student']['marks']['history'])


#                                                     Q8
print(">>>>>>>>>>>Q8<<<<<<<<<<<<<<")
my_Dict = {1: "Alaa", 5: "Hadeel", 7: "Hanin", 13: "Malak"}
new_list = []
for key, value in my_Dict.items():
   if key < 10:
      new_list.append(value)
result= '->'.join(new_list)
print(result)
