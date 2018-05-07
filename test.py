class Coffee:
  pass

class Child:
    characteristic = "Hooman"
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Account:
    def __init__(self):
        self.username = None
        self.pwd = None

    def set_id(self,username):
        self.username = username

    def set_pwd(self,pwd):
        self.pwd = pwd


if __name__ == "__main__":
  acc = Account()
  print(acc.username)
  acc.username = "Lulu"
  print(acc.username)
