def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

print(f"        {title:^55}")
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^15}")
print(f"{colorChange('purple')}{pause:>15}")
print()
print()
text = "WELCOME TO"
print(f"{colorChange('white')}{text:^25}")
text = "--  ARMBOOK  --"
print(f"{colorChange('blue')}{text:^44}")
text = "Definitely not a rip off"
print(f"{colorChange('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colorChange('yellow')}{text:>35}")
text = "networking site"
print(f"{colorChange('yellow')}{text:>39}")
text = "Honest."
print(f"{colorChange('red')}{text:^40}")
text = "Username: "
username = input(f"{colorChange('white')}{text:^40}")
text = "Password: "
password = input(f"{colorChange('white')}{text:^40}")
print()
username = "username"
password = "password"



