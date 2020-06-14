Scale.default = Scale.minor


m = P[0,4,9,0,1,2,3,5]

p1 >> sinepad(m , dur = 1 , room = 2 , lpf = 300)

d1 >> play("x" , dur = 1 , room = 2 , lpf = 500)

d2 >> play("-o-o", dur = 1 , room = 2 , hpf = 700)


d3 >> play("----", dur = 2 , room= 2 , hpf = 700)

print(P[0].stretch(8))

n = P[0].stretch(8)

d4 >> sinepad(P[0].stretch(8) , dur = 1 , room = 2 , lpf = 300)


d5 >> sinepad( [ m + n ] * 2 , dur = 0.25 , room = 2 , lpf = 250 )





