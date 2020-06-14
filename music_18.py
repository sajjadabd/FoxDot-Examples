print(PTri(5))

Scale.default = Scale.dorian2

print(Scale.names())

p1 >> marimba( PTri(5).palindrome().reverse() , dur=[1, 1/2, 1/2], amp=0.75) 

p1.stop()

p2 >> play("x[--]{x}[--]")

p2.stop()

p3 >> pluck(P[0, 1, 2, 3].palindrome().rotate() , dur=PDur(3,8) , amp=PTri(1,3) , rate=PDur(1,3) , oct=(3,4) )





