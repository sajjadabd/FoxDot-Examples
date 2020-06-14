a = "C:/Users/sajjad/Desktop/drums135.wav"

b = "C:/Users/sajjad/Desktop/kano.wav"

p1 >> loop( a , dur = PDur(3,8) , chop = 0 ) # GOOD

p1 >> loop( a, P[2:3], dur =1)

p1 >> loop( a, P[:4].shuffle(), dur=1)

p1 >> loop( a, P[:4], dur=1, tempo=135) # GOOD

p1 >> loop( a, dur=4, beat_stretch=True , amp = 0.4) # GOOD

p1 >> loop( a, dur=3.5, beat_stretch=True , lpf=linvar([1000,4000] , 8) , amp = 0.8 ) # GOOD

p1 >> loop( a, dur=4, striate=100)

p1 >> loop( a, P[:8]/2, dur=1/2 )

p1 >> stretch( a, dur=4) # VERY BAD

l1 >> play("x-x-")

p2 >> loop( b , dur = 2 )

p2 >> loop( b , dur = PDur(3,8) , chop = 0 )

p2 >> loop( b, P[2:3], dur =1)

p2 >> loop( b, P[:4].shuffle(), dur=1)

p2 >> loop( b, P[:4], dur=1, tempo=135) # GOOD

p2 >> loop( b, dur=4, beat_stretch=True , amp = 0.4) # GOOD , GREAT

p2 >> loop( b, dur=4, striate=100)

p2 >> loop( b, P[:8]/2, dur=1/2, slide=[0,0,-2])

p2 >> stretch( b, dur=4)

p2.stop()
