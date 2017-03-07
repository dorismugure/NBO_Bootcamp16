def data_type(slack): 
	
    if slack is None:
        return 'no value'
        
    if isinstance(slack, str):
        return len(slack)
        
    elif isinstance(slack, bool):
        return slack
       
    elif isinstance(slack, int):
    	
        if slack < 100:
            return "less than 100"
        elif slack == 100:
            return "equal to 100"
        return "more than 100"
       
    elif type(slack) == list:
		    if len(slack) < 3:
			      return None
		    else:
			      return slack[2]
			  