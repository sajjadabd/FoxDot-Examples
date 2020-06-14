Clock.bpm = 120
Root.default = 1 
Scale.default.set = 'major'


p1 >> play("X-")

ch = var(  P[5,2,4,0].every(2 , "shuffle") , [4]  )

a = P[7,5,3,1,6,4,2,0]

b1 >> dbass(ch , chop = 4 , sus = 2 , amp = 0.5 , amplify = 0.3 , lpf= 500 , hpf = 200)


b2 >> blip(a.shuffle() , dur=PDur(3,8)*(1,2) , chop = 4 , sus = 2 , delay = (0,1/4 ) , amp = 1 , lpf = 700 ).spread() + ch


k1 >> play("----", dur = 1/4)



p2 >> charm()



