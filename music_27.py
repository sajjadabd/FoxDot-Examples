
Clock.bpm = 120

p1 >> star([5,1,4,0,3,0] , dur = PSum(6,4) ) + (0 , 4 )

p2 >> prophet([0,2] , dur = [4] , amp = 2) + (0,4)

p3 >> blip(P[0,2,0,4,0,1] , dur = PDur(6,8) , amp = 1.2 )


d1 >> play("  * " , amp = 1.2)


s2 >> play("V   V  V")


d3 >> play("-{-=}-{-=}[--]-{-=}-[--]")


d4 >> play(P["  H     "] , amp = 2)



b1 >> dbass(var([5,1,4,0],[2,2,4,8]) , dur = PDur(5,16) , amp = 0.6 )




















