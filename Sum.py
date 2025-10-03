number = int(open("INPUT.TXT", "r").read())
sum_ = 0
i = 1
while i <= number:
    sum_ += i
    i += 1
open("OUTPUT.TXT", 'w').write(str(sum_))