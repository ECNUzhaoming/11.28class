
# coding: utf-8

# In[3]:

class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
        
    def set_size(self,size):
        assert(size[0]>=0 and size[1]>=0)
        self.width,self.height=size
        
    def get_size(self):
        return self.width,self.height
    
    size=property(get_size,set_size)
    
rect=Rectangle()
rect.set_size((3,4))
print(rect.get_size())


# In[7]:

#静态方法和类方法
class MyClass:
    def static_method():#在类里面定义的函数，没有绑定任何参数，专门给类用的，这样的函数成为静态函数，既不能访问类，也不能访问类的对象
        print("This is a static method.")
    static_method=staticmethod(static_method)
    
    def class_method(cls):#类的方法是有参数的
        print("class method",cls)
    class_method=classmethod(class_method)
    
MyClass.static_method()
MyClass.class_method()


# In[ ]:

class MyClass:
    @staticmethod#修饰器
    def static_method():
        print("This is a static method.")
    #static_method=staticmethod(static_method)
    
    @classmethod
    def class_method(cls):#类的方法是有参数的
        print("class method",cls)
    #class_method=classmethod(class_method)
    
MyClass.static_method()
MyClass.class_method()


# In[ ]:

class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0;
        
    def __setattr__(self,name,value):
        if name=="size":
            self.width,self.height=value
        else:
            self.__dict__[name]=value
            
    def __getattr__(self,name):
        if name=="size":
            return self.width,self.height
        else:
            return self.__dict__[name]b


# In[13]:

import math 

math.sin(0)


# In[14]:

print("Hello,world")


# In[15]:

jg


# In[ ]:



