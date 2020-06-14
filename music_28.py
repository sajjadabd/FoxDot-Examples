

Root.default.set("F")


Scale.default.set("minor")

Clock.bpm = 110


song1 = [0]*7

print(song1)

dur1 = P[1 , rest(1) , 1 , rest(1) , 1 , rest(5/2) , 1/2 ]


print(dur1)


song2 = [0,0,0,2,0,3,0,4,2]


print(song2) 



dur2 = P[ 1/2 , rest(1/2) , 1,1,1/2,1/2, rest(3) , 1/2, 1/2]

print(dur2)


p1 >> bass( song1 + song2 , dur = dur1 | dur2 )


p2 >> play("x" , dur = 1)


p3 >> play(" cc(ct)" , dur = 1/2 , amp = [0 , 0.8 , 0.5 , 0.8])


p4 >> play("x-o-").every(2 , "amen")

















