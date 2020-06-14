

song =  [1,1,1,1,1,1,3,3,3]

dur = P[1,1,1,rest(2),1,1,1,rest(2),2,2,2] * 0.5

print(dur)

p1 >> viola(song , dur = dur)

p2 >> piano(P[0,1,2,3,4].stutter(2).palindrome().shuffle() , dur=PDur(3,8) )

p1 >> play("X ")

nextBar(Clock.clear())
