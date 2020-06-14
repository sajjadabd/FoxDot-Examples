Root.default.set("E")

Clock.bpm = 136

#p7 >> pluck(P[5])

#p7.stop()


dur = P[1 , 0.5 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0.5 , 1 , 1 , 0.5 , 1 , 1 , 1 , 1 , 0.5]

song = P[[3 , 3 , 3 , 3 , 3 , 3 , 4 , 4, 5 , 5, 5 , 5 , 5 , 5 , 5, 7 , 7 , 7]]



p1 >> dbass( song - 7 + 2 , dur = dur , amp = 0.2)

p2 >> pluck( song - 7 + 4 , dur = dur)

p3 >> pluck( song - 7 + 4 , dur = dur)


p4 >> play("x " , sample = 0 , amp = 0.8)


m1 >> sinepad(P[0 , 0 , 0, 0 , 1 , 1 ] + 7 , dur = [1,0.5,0.5,0.5,0.5,5] )

m1.stop()

m2 >> sinepad(P[1,1,0,1,2,3,2] + 7 , dur = [1 , 0.5 , 0.5 , 0.5 , 0.5 , 0.5, 4.5])

m2.stop()
























