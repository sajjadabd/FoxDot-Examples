
print(P[:8])

p1 >> pluck(P[:8] , dur = 1/2)

p1.every(4, "reverse")


p1.stop_calling("reverse")


p1.every(4 , "stutter" , 4 , oct = 4)


print(p1.getattr(p1 , "stutter"))




