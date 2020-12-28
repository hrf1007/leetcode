
class Demo:
    data1 = 100
    
    def set(self, num):
        self.data2 = num
   
    def __repr__(self):
       
        return 'repr转换：data1 = %s; data2 = %s'%(self.data1, self.data2)
    def __str__(self):
        return 'str转换：data1 = %s; data2 = %s'%(self.data1, self.data2)

demo = Demo()

demo.set('abc')

print(repr(demo))
print(str(demo))
print(demo)