Scale.default = Scale.major

Root.default = "C"

#Root.default = "D"

#Root.default = "D#"

#Root.default = "Db"

Clock.bpm = 120


p1 >> blip([0,4] , dur=PDur(3,8), sus=2, chop = 4).every(3 , "offadd" , 2).every(5 , "stutter" , 4 , dur = 3 , oct = 6)


p2 >> klank(var([0,2],8) , rate = P[4:24].stutter(2) , lpf=800 )


p3 >> piano(var([0,3,5,4]) + (0,1,2,const(7),const(9)) , dur = PDur([5,5,7],16)*2 , oct=4 , delay = P(0,0.5).stretch(5) )


p1.solo()
p1.solo(0)


b1 >> sawbass(p3.pitch[0] , dur= PDur(5,8))

d1 >> play("X ")


d2 >> play("k", dur=PDur(3,8)*(1,2) , rate=0.8, room = 0.5 , sample = P[:5] , pan=(-1,1) , echo = 0.5)


d3 >> play("m", rate = [1,2,3,2] , dur = PDur(5,8) ).every(4 , "offmul" , 2).every(9 , "stutter" , 8 , dur = 1 , rate=P[:8] )



c1 >> play("#" , dur = 32 , room = 1 , amp = 2)


Clock.clear()
