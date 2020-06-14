

p1 >> pads([0, 4, 5, 3], dur=4 , amp = 0.3)

p2 >> pluck(p1.degree, dur=1/2)



p1 >> pads([0, 4, 5, 3], dur=4 , amp = 0.3)

p2 >> pluck(p1["degree"], dur=1/2)







p1 >> pads([0, 4, 5, 3], dur=4 , amp = 0.4)


p2 >> pluck(p1.pitch.map({4: 1, 3: 0}, default=2))







p1 >> bass([0, 4, 5, 3], dur=4)

p2 >> pluck(p1.pitch + (0, 2, 4), dur=1/2)








p1 >> bass([0, 4, 5, 3], dur=4)

p2 >> pluck([p1.pitch, 7, 6, 7], dur=1/2)









p1 >> pluck([0, 2, 6, 3, 2, 4, 1, -2], dur=1/2, pan=[-1, 0.5, 0.25, -0.5, 0])

p2 >> blip(p1.pitch + 2, dur=1/2, pan=p1.pan * -1)








p1 >> pluck([0, 4, 5, 3], dur=4) + (0, 2, 4)

p2 >> blip(p1.pitch[0].accompany())
