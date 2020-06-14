Root.default = "C"

p1 >> piano(P[1,2,3,4].palindrome() , chop = 1  , hpf = linvar([100,1000],8), dur = PDur(3,8) , oct=var([4,5]) ).every(6 ,"stutter" , 4 , dur = 1).every(8 , "reverse")

p2 >> play("Xs")

p2.stop()

p2 >> play("V " , amp =linvar([0.5,1.2],8))



p3 >> sawbass(p1.pitch , dur=PDur(3,8))

p3.stop()

m1 >> play("-{-[--]o}" , dur = 1 )



m2 >> play(" H " , dur = 12)

n1 >> bell(p1.pitch , dur = PDur(3,8))


n1.stop()




l1 >> dbass(p1.pitch , dur = PDur(3,8) , lpf = linvar([100,2000],8))


l2 >> play("x-o-" , sample = 2)











print(SynthDefs)
