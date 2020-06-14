


#p1 >> bass([1,3,4] , dur = [2,1,1] )


p2 >> play("x-o-" , amp = 1)

p3 >> bell([1,3,2] , dur = [2,1,1] , amp = 0.6)


p4 >> play("[nn]")



p5 >> soprano([[1,3,2,4] , [0,2,2,5]] , amp = 1)


p6 >> play(P["x( x) "].palindrome().zip("---[--]").zip(P["  o "].amen()) )

p7 >> gong([[1,3,2,4],[0,2,2,5]] , amp = 2 , room = 2 , dur = PDur(3,8) )


p8 >> play("x-o{-[--]o[-o]}")









