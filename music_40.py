


p1 >> pluck(P[0,1,2,3,4] , dur = PDur(3,8))


p2 >> sitar(p1.pitch[0] , dur = PDur(3,8))


p4 >> play("V ")


p5 >> play("x-x-" , amp = 2)


p6 >> charm(P[0,1,2,3].palindrome() , dur= PDur(3,8) , amp = 2)

p1 >> play("X X ")



p2 >> play("xxx--oo-[-x-]---[-x-]" , amp = 2)

p5 >> play("x-x-")




p1 >> piano(P[0,1,2,3,4].palindrome().shuffle() , dur=PDur(3,8))

p2 >> play("V ")
