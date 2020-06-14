

p1 >> play("x-o(---=)" , dur = 1/2)


p2 >> pluck(P[0,1,2,3,4,5,6] ,
oct = 6 ,
sample  = 2  ,
mix = 2 ,
drive = 1 ,
sus= 0.5 ,
dur = PDur(3,8)
)


p2.stop()

p3 >> sitar(P[0,1,2,3,4,5,6],
oct = (5,6) ,
sample = 4,
mix = 1 ,
shape = 0 ,
room = 0 ,
sus = 2 ,
decay = 1 ,
dur = [1,2,2,1,1],
)



p4 >> glass(P[2,3,1,4] , amp = 2 , sample = 2)
