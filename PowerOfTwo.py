# изначальный вариант:
""" number = open("INPUT.TXT", "r").read()[:-1]
if number:
    number = int(number)
else: number = 0
res = str(number * (number + 1)) + "25"
while True:
    if res[0] != "0":
        break
    res = res[1:]
open("OUTPUT.TXT", 'w').write(res) """
# правильный вариант:
number = open("INPUT.TXT", "r").read()
open("OUTPUT.TXT", 'w').write(str(pow(int(number), 2)))