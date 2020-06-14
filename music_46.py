
Scale.default = Scale.major

Scale.default = Scale.minor

Root.default = "D"

p1 >> piano(var(P[[2,3],2,3,[4,2,4],5,[2,3],7],[2,1,2,[2,3],1,2,[1,2]]), dur = PDur(var([3,5]),8) , sus = 1 , chop = 0 , lpf=linvar([1000,2500],4) , hpf=linvar([100,3000],4) , amp = 2 )


p1.stop()

p2 >> play("---")

p3 >> play("x-o-" , sample = 4)

p4 >> play("V ")

p5 >> play("!" , dur = 12)

p5.stop()

p6 >> play("C" , dur = 12)


l1 >> play("#")

l1.stop()


b1 >> sawbass(p1.pitch[0] , dur = PDur(3,8) , pan=linvar([-1,1],8) )



b2 >> blip(P[3,4,5,5,6,7] , dur = 1/2 , amp = 2  )


b3 >> pluck(P[1,2,3,6,5,4].palindrome() , dur=PDur(3,8) , sus = 2 ).every(5 , "reverse")



b4 >> space(P[3,4,5,2,1] , dur = PDur([3,5],8) )


k1 >> sitar(b2.pitch , dur = PDur(3,8) , sus = 2 )








