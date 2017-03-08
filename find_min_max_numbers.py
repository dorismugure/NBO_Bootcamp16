def find_max_min(num):
 
  if min(num)!=max(num):
    list=[]
    list.append(min(num))
    list.append(max(num))
    return list
  else:
    list=[]
    list.append(len(num))
    return list


