

p1 >> piano(var([P[1,2,1,2],P[1,2,3,4]],4) , dur = PDur(3,8) , sus = 0.5)

p1.solo(0)

p2 >> play("Xs")

p2.solo(0)

p3 >> play("--(--*--){-x-o-=}")


p3.solo(0)


l1 >> bell(p1.pitch , dur = PDur(3,8) , amp=var([0,1],4))



l2 >> space(P[1,2,3] , dur = PDur(var([3,5],8),8))


m1 >> swell(P[1,2,3].palindrome().shuffle() , dur = PDur(3,8))


n2 >> sitar(p1.pitch)


