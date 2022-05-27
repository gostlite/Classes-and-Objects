class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name, age: int, tracks, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self,new_name):
        self.name = new_name
        print(f"My new name is {self.name}")
        return

    def change_age(self,new_age):
        self.age = new_age
        print(f"My new age is {self.age}")
        return
    
    def add_track(self,new_track):
        self.tracks = new_track
        print(f"My new track is {self.tracks}")
        return

    def get_score(self):
         print(f"My score is {self.score}")
        


        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
