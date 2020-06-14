a = P[0,0,0,0,1,1,1,1]

b1 >> bass(a , dur = 1 , room = 1 , lpf = 200)


b2 >> bass(a , dur = 0.5 , room = 1 , lpf = 200)

b2.lpf = 500

b2.lpf = 700

b2.hpf = 400


d1 >> play("xxxx" , dur = 1 , room = 1 , lpf = 1000 , hpf = 200)


d2 >> play("0-0-", dur = 0.5)


d3 >> bass(P[3,3,3,3] , dur = 0.5, lpf=150) + (0)




d4 >> bass(P[5,5,5,5] , dur = 0.5, lpf=150) + (11,14,16)




m1 >> play("----" , dur=1/4)





























