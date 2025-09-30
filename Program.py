numbers = open("INPUT.TXT", mode="r").read().split()
open("OUTPUT.txt", mode="w").write(str(int(numbers[0]) + int(numbers[1])))