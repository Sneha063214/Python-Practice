#args and kwargs 

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('Maths','physics',name='sneha',rollno=194)

#unpacking the dictionaries and list using kwargs and args

courses=['maths','chemistry']
details={'name':'sneha','rollno':194}

def info(*args,**kwargs):
    print(args)
    print(kwargs)
info(courses,details) #this should pass the list and dictionary as whole ,it won't unpack it 
info(*courses,**details) #this will unpack the elements in list and dictionary
