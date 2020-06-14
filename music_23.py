#music_23

Clock.bpm = 120
Root.default = 1 
Scale.default.set = 'major'


p1 >> play("X-")

p1.lpf = 1000

p1.stop()

ch = var(  P[5,2,4,0].every(2 , "shuffle") , [4]  )

a = P[7,5,3,1,6,4,2,0]

b1 >> dbass(ch , chop = 4 , sus = 2 , amp = 0.5 , amplify = 0.3 , lpf= 500 , hpf = 200)


b1.lpf = 100

b1.stop()

b2 >> blip(a.shuffle() , dur=PDur(3,8)*(1,2) , chop = 4 , sus = 2 , delay = (0,1/4 ) , amp = 1 , lpf = 1000 ).spread() + ch


b2.lpf = 2000

b2.stop()

k1 >> play("----", dur = 1/4)

k1.lpf = 3000

k1.lpf = 0

k1.stop()

p2 >> charm(P[0,[2,4]]  , dur = 1 )

p2.lpf = 2000

p2.stop()

p3 >> space(P[7,3,4,0], dur=PDur(3,8)).spread()

p3.lpf = 2000

p3.stop()

#p4 >> prophet(P[4,0,2,0] + (0,4) , oct=(5,6) , dur = 2)

#p4.lpf = 2000

#p4.stop()

#p5 >> saw(P[:10] , dur=PDur(3,8) , drive=1/2 , amp=1/2 , pan=linvar([-1,1],4) ).penta()

#p5.lpf = 200

#p5.lpf = 100

p5.stop()

p6 >> dab(ch , dur = 1 , amp = 1/2 , chop = (0,32) , lpf = 200 )


p6.lpf = 100

p6.stop()

#p7 >> klank(P[7,0] , dur = 4 , chop = 32 , hpf=linvar([0,5000],32) , pan=linvar([-1,1],32))


#p7.lpf = 1000

#p7.stop()

p8 >> bell( P[0,1,2,3,5].shuffle() , dur = 1/2 , amp = 1/2 )

p8.lpf = 1000

p8.lpf = 0

p8.stop()




















