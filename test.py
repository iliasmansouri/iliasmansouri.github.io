class Coffee:
  pass

if __name__ == "__main__":
  cup1 = Coffee()
  cup2 = cup1

  cup1.brew = "test"
  cup1
  cup1.__dict__
