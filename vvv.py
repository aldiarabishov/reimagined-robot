class Film():
   def __init__(self):
       self.name = "Avatar 2"
       self.year = str(2022)
       self.director = "Neitiri"
       self.box_office = str(100)
       self.duration = str(155)
       self.rate = str(1000)


   def get_name(self):
       return self.name


   def change_name(self):
       self.name = str(input())
       def get_director(self):
          return self.director
        
   def show_info(self):
        print(self.name)
        print(self.director)
        print(self.year)
        print(self.box_office + "water")

Film().show_info()