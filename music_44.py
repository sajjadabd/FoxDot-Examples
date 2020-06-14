
a = P[0,1,2,3,4,5]

dur = [1/2,1/2,1/2,1/2]

p1 >> viola(a.shuffle().reverse() , dur = dur ,  pshift=[0 , [0,4,2]]  )

p2 >> play("X-X-")

p4 >> play(" H ")

p5 >> play("[--]")

p3 >> piano(P[0,1,2,5,4,2] , dur=PDur(3,8) , chop = 1 ,  pshift=[ 0 , (0,1)] )



p1 >> pluck([0, 4], dur=4, glide=[7,-7])



# Shift a synth's pitch
p1 >> pads(pshift=[0,1,2,3])



# Shift a sample's pitch
p2 >> play("C", dur=2, pshift=[0,1,2,3])



# Can be used to make chords
p2 >> play("x", dur=2, pshift=[0, (0,4,7)], sample=3)






p1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7] , dur=PDur(5,8)).every(8, "reverse")


p2 >> play("x-x-")


p3 >> play("[--]")



# Play a note 2 steps higher delayed 1/2 a beat
p1 >> pasha([0, 4], dur=[3/4, 3/4, 1/2]).every(3, "offadd", 2)



# Play a note 4 steps higher delayed 3/4 of a beat
p1 >> pasha([0,1,3,4], dur=1/2).every(5, "offadd", 4, 3/4)






p1 >> play("x-o-").every(4, "stutter", 4, dur=Cycle([3, 2]) )
