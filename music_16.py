p1 >> play(P["X--(-[--])O--O(-=)-"].layer("mirror")
    , dur = PDur(5,8) , oct = 7 , sample = -1 , rate = var([1,4],[28,4]) )


p1.hpf = 2000

p1.stop()

print(PZip("Vs" , "  n "))

d2 >> play(PZip("Vs" , "  n "), sample = 2 ,
    hpf = var([0,4000],[28,4])).every(10 , "stutter" , dur = 1)


d2.hpf = 2000

d2.stop()



d3 >> dirt([0,-2,1,3] , dur=PDur(3,8) , bits = 4 , fmod = (0,1))

d3.hpf = 2000

d3.stop()



d4 >> karp(dur=1/4 , oct = var([6,7]) , amp = 0.7 , sus = 1 , rate=P[:32]*(1,2) ) + var([0,-1,1,0])

d4.hpf = 2000

d4.stop()
