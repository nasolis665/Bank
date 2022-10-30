balance=0
def withdrawal(x):
  balance -= x
  print(f"You withdrew ${x} your balance is now ${balance}")
def deposit(y):
  balance += y
  print(f"You deposited ${y} your balance is now ${balance}")
print("If you would like to add money to your account type deposit(y), y being how much money you want to add. If you would like to take money from your account type withdrawal(x), x being how much money you want to take")