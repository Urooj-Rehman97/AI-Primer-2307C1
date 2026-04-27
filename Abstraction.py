from abc import ABC, abstractmethod

class person:
  @abstractmethod
  def intro(self):
      pass

class teacher(person):
      def intro(self):
          print("I am Teacher")

class student(person):
    def intro(self):
        print("I am a Student")


p = person()
p.intro()

t = teacher()
t.intro()
s = student()
s.intro()