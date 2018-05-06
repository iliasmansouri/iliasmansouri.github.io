class Coffee:
  pass

class Child:
    def __init__(self,name,age):
        self.name = name
        self.age = age


if __name__ == "__main__":
  cup1 = Coffee()
  cup2 = cup1

  cup1.brew = "test"
  cup1
  cup1.__dict__

  c = Child("Ilias",445)

  c
  c.__dict__
  
