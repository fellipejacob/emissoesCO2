popA, popB, anos = 80000, 200000, 0
cresA, cresB = 0.03,0.015

while popA < popB:
    anos += 1
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)


print("Após %i anos o país A ultrapassou sua população ao país B." % anos)
print("País A: %0.f" % popA)
print("País B: %0.f" % popB)