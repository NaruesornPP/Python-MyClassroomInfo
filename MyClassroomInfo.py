class Student:
    def _init_(self,name,room):
        self.name=name;
        self.room=room;
        
    def PrintData(self):
        print(self.name,self.room);
    
    
s01 = Student();
s01.name='Kontee';
s01.room=1;

s01.PrintData();
