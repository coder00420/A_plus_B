number = int(open("INPUT.TXT", "r").read())
is_negated = False
if number < 0:
    number = -number
    is_negated = True
sum_ = 1
i = 2
while i <= number:
    sum_ += i
    i += 1
if is_negated == True: sum_ = -sum_ + 1
open("OUTPUT.TXT", 'w').write(str(sum_))