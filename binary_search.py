class BinarySearch(list):
    
    def __init__(self,a,b):
      item = []
      item.append(b)
      length = 1
      while length < a:
        item.append(item[length -1] + b)
        length +=  1
      super(BinarySearch,self).__init__(item)
      self.length = len(item)

    def search(self,number):
        count  = 0
        first  = 0
        self.length = len(self)
        last  = self.length - 1
        middle_point = int((last) / 2)
        item_location = {'count':'','index':''}
        while first < middle_point:
            
            if (first == middle_point) and (self[first] > number):
                index = -1 
                item_location["count"] = self.length
                item_location["index"] = index
                return item_location
            
            elif self[first] == number:
                index = first
                item_location["count"] = count
                item_location["index"] = index
                return item_location
            elif self[last] == number:
                index = last
                item_location["count"] = count
                item_location["index"] = index
                return item_location
            elif self[middle_point] == number:
                index = middle_point
                item_location["count"] = count
                item_location["index"] = index
                return item_location
            else:
                if self[middle_point] > number:
                    last = mid_point - 1
                    first = first + 1
                    middle_point = (last + first)//2
                else:
                    first = mid_point + 1
                    last = last - 1
                    middle_point = ((last + first)//2) + 1
            count += 1
        item_location = {'count':count,'index':-1}       
        return item_location
