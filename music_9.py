p1 >> blip([0,4] , dur=PDur(3,8), sus=2, chop = 4).every(3 , "offadd" , 2).every(5 , "stutter" , 4 , dur = 3 , oct = 6)

p1.stop()

p2 >> klank(var([0,2],8) , rate = P[4:24].stutter(2) , lpf=800 ) 

p2.stop()

p3 >> piano(var([0,3,5,4]) + (0,1,2,const(7),const(9)) , dur = PDur([5,5,7],16)*2 , oct=4 , delay = P(0,0.5).stretch(5) )

p3.stop()

p1.solo()
p1.solo(0)


b1 >> sawbass(p3.pitch[0] , dur= PDur(5,8))

b1.stop()

d1 >> play("X ")

d1.stop()

d2 >> play("k", dur=PDur(3,8)*(1,2) , rate=0.8, room = 0.5 , sample = P[:5] , pan=(-1,1) , echo = 0.5)

d2.stop()

d3 >> play("m", rate = [1,2,3,2] , dur = PDur(5,8) ).every(4 , "offmul" , 2).every(9 , "stutter" , 8 , dur = 1 , rate=P[:8] )

d3.stop()

c1 >> play("#" , dur = 32 , room = 1 , amp = 2)

c1.stop()


Scale.default="minor"
Clock.bpm=140

c1 >> play("@", dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4, pan=-0.5)

c1.stop()

c2 >> play("#", dur=40, room=1, amp=2, pan=0.5)

c2.stop()

c_all.stop()

d1 >> play("")

b1 >> dbass(dur=PDur(3,8), sus=2, chop=4, shape=PWhite(0,1/2), pan=PWhite(-1,1)).sometimes("offadd", 4) + var([0,2],4)

b1.stop()

p1 >> space([7,6,4,P*(2,1),0], dur=8, pan=(-1,1))
Master().hpf=var([0,4000],[76,4])

p1.stop()


p5 >> play("V{-s}", amp = 1)

p5.stop()


chords = var([0, 4, 5, 3])

p3 >> blip(chords + (0, 2, 4), dur=4)

p3.stop()

p4 >> pasha(chords + [0, 2, 3, 4, 7, 9], dur=1/4)

p4.stop()





Clock.clear()

