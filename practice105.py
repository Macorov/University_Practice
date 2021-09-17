def function_name(dic):
    
    while True:
        lst = []
        c = input("Enter course name: ")
        if c== "STOP":
            break
        for k,v in dic.items():
            if c in v:
                lst.append(k)
        print(lst)
given_dict = { 'Mike' : ['CSE110','ENG101','MAT110'],              
              'Simon' : ['CSE111','PHY111','MAT110', 'CSE230'],
              'Shawn' : ['CSE110','ENG101','MAT120','CSE230'],
              'Alice' : ['CSE110','ENG091','MAT092']  }
function_name(given_dict)