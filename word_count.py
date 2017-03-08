def words(word):
      try:
       word = word.split()
       my_dict = {}
       for item in word:
           if item.isdigit():
               if int(item) in my_dict:
                 my_dict[int(item)] = my_dict[int(item)]+1
               else:
                   my_dict[int(item)] = 1
           else:
               if item in my_dict:
                   my_dict[item] = my_dict[item]+1
               else:
                   my_dict[item] = 1
       return my_dict
      except Exception:
        return "invalid"
print(words("hello hello my dear mom 23 4 56"))

