Clock.bpm = 120

print("Hello Fox")


print(P+[1,2])

print(PTri(0,8))

print(PDur(3,8))

p1 >> play("x-x-")

p2 >> dbass(P[0,1,2,3,4] , dur=PDur(3,8) )

p3 >> pluck(P[3,2,5,4].palindrome() , amp = 0.6 , pan=linvar([-1,1], 4))

p4 >> sinepad(P[4,2,1,3,0,4,3], dur = PDur(3,8) )

b1 >> space(P[0,1,2,3,4].shuffle() , dur = [1, 1/2 , 1/2 , 1/2])



b2 >> sitar(P[0,1,2,3,4].reverse()  , oct = (6,7) , dur = PDur(2,5) )

b3 >> marimba(P[0,0,0,1,2,3,3,3] + 2 , amp = 2)


m1 >> glass(P[0,1,2,3] , dur = PDur(2,5))


m2 >> feel(P[2,2,3,1] , dur = 1)


m3 >> charm(P[0,1,1,2,3].palindrome() , amp = 1.7 , dur =[1,1/2,1/2,1/2])

m3.stop()

k1 >> pluck(P[2,2,1,1,1,1,2,3,3,2].reverse() , dur = (1,1.5) , oct = 4)

k2 >> pads(P[0,1,1,1,2,2,2,3] , oct = 2 , amp = 1 , dur=PDur(3,8) )


k3 >> blip(P[0,2,2,1,1,1].palindrome() , dur=[1,1/2] , oct = 8 )


k4 >> saw(P[0,0,1,1,1,2,2,3] , dur=PDur(2,5))

k4.stop()

n1 >> noise(P[1,1,2,2,2])

n1.stop()


n2 >> swell(P[2,2,1,0,0,1,1] , dur=[1/2,1,1/2,1/2])


l1 >> blip(n2.pitch)

p1 >> play("x-o-").every(8, "amen")

print(P[0, 1, 2, 3].offlayer("rotate"))

p1 >> pluck(P[0, 1, 2, 3].offlayer("rotate"))


print(P[0, 1, 2, 3].offlayer("rotate", 2))

p1 >> pluck(P[0, 1, 2, 3].offlayer("rotate", 2))




p1 >> pluck(P[0, 1, 2, 3].offlayer(lambda x: (x * 2) + 1) , dur=PDur(3,8))


p1 >> pads(P[0, 1, 2, 3].offlayer(lambda x: (x * 2) + 1) , oct = 5 )




print(var([1,2,3,4,5],[1,2,3,2,1]))


p1 >> pluck(var([1,2,3,4,5],[1,2,3,2,1]) , dur=PDur(3,8))

p1.lpf = 1000
p1.stop()

p2 >> play("V ")
p2.stop()

p3 >> play("x-x-")
p3.stop()


p4 >> play()


p1 >> karp(P[1,1,1,1,2,3,3,2,2,3] , oct = 7)
