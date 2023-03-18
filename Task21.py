# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
              {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

result_set = set()
for dict_ in dict_list:
    for val in dict_.values():
        result_set.add(val)

print(result_set)

# result_set = set()
# for dict_ in dict_list:
#     val_set = set(dict_.values())
#     result_set |= val_set

# print(result_set)