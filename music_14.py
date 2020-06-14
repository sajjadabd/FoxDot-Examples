p1 >> pluck([0,4], dur=[3/4,3/4,1/2], chop=4, sus=2)

p1.stop()

p2 >> blip(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate() | P[[9,11]], dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

p2.stop()

p_all.hpf = 1000

p_all.hpf = 0


d1 >> play("Xs")

d_all.lpf = 1000

d_all.lpf = 0

d1.stop()


var.chords = var([0,-1,3], dur=[4,4,8])

c1 >> blip([var.chords,2,3,4], sus=2)

c1.stop()

c2 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4)

c2.stop()

c3 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6)

c3.stop()

c4 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6).every(8, "reverse")

c4.stop() 


c5 >> star(var.chords + (0, 2, 4), dur=PDur(3,8))

c5.stop()


c6 >> star(b1.pitch + (0, 2, 4), dur=PDur(3,8))

c6.stop()


c_all.hpf = 1000

c_all.hpf = 0




e1 >> sawbass(var.chords, dur=PDur(3,8)*2)


e1.stop()
 
e_all.hpf = 1000

e_all.hpf = 0 



r1 >> pluck(P+(0, 4), dur=PDur(3,8), sus=1)

r1.stop()

r2 >> pluck(P+(0, 4), dur=PDur(3,8), sus=2)

r2.stop()


  

r_all.hpf = 1000

r_all.hpf = 0




f1 >> play("<|x2|s><  |*(3[33])| ><(+  )+( [( +)+])>", pan=P(0, 0, [-1,1]))

f1.stop()


 
 
f_all.hpf = 1000

f_all.hpf = 0




Scale.default = "minor"

print(SynthDefs) # Pick your own synths!

z1 >> sawbass(var([0, 2], 8), dur=1)

z1.stop()

z2 >> keys(b1.pitch + (0, 2, 4), dur=8)

z2.stop()

z3 >> blip(P[0, 2, 4].stretch(8), dur=1/2, sus=2) + var([0, 2], [6, 2])
    
z3.stop()

z4 >> play("<xs><  * ><(+  )+( [( +)+])>")


z4.stop()



  

z_all.hpf = 1000

z_all.hpf = 0


