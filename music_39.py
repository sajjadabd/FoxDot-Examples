
p1 >> nylon(P[1,2,3,4].palindrome() , channel = 6 , mix = 2 , chop = 1 , lpf = 1600 , hpf = 200 , dur = PDur(3,8) , cut = 6 , oct = 5, echo = 1 , sample = 4 , scale= Scale.minor)

p2 >> play("x-x-" , sample = 0 , fmod = 3 , rate = 1 , slide = 1)


p3 >> sitar(p1.pitch[0] , dur = PDur(3,8) , channel = 2 , lpf = 1900 , fmod = 3 , rate= 1 , slide = 2
  )

p3.stop()

p4 >> play("x-x-o-(-x)-(-x)-(---=)")


p5 >> play("   I   I  ")
