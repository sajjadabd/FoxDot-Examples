p1 >> pads(P[0, 4, 5, 3] , dur = 2)


p2 >> pluck(p1.pitch, dur=1/2)


Clock.clear()


p1 >> pluck(dur=1/2, amp=PRand([0, 1]))

p3 >> play("*", amp=p1.amp)

p3.stop()

p4 >> play("V ")

p5 >> play("x-o-")

p4.stop()

Clock.clear()


p1 >> sawbass([0, 4, 5, 3], dur=4)

p2 >> star([p1.pitch, 7, 6, 7], dur=1/2, sus=1)

p1 >> sawbass([0, 4, 5, 3], dur=2)

p2 >> star(p1.pitch + 2, dur=PDur(3,8))

Clock.clear()


p1 >> sawbass([0, 4, 5, 3], dur=2)

p2 >> star(p1.pitch + (0, 2, 4), dur=PDur(3,8))

Clock.clear()


p1 >> sawbass([0, 4, 5, 3], dur=2)

p2 >> star(p1.pitch + P[:6:2].palindrome(), dur=PDur(3,8))

Clock.clear()



p1 >> play("*", dur=PDur(3,8), pan=PRand([-1, 1]))

p2 >> play("+", dur=1/4, amp=PRand([0,1]), pan=p1.pan*-1)

Clock.clear()



p1 >> pluck(amp=PRand([0,1]), dur=1/2)

p2 >> play("x", amp=p1.amp != 1)

Clock.clear()





b1 >> sawbass(var([0, 1, 5, 3]), dur=PDur(3,8))

p1 >> star(b1.pitch.accompany())

Clock.clear()







b1 >> sawbass(var([0, 1, 5, 3]), dur=PDur(3,8))

p1 >> star(b1.pitch.accompany())

d1 >> play("(x )( x)i( [ i])")

d2 >> play("[--]")

Clock.clear()





print(Samples.loops)



p1 >> loop("foxdot", P[:4], dur=1)
 
# Or play the first 4 beats in random order:

p1 >> loop("foxdot", P[:4].shuffle(), dur=1)

# Or play a random selection of snippets quickly:

p1 >> loop("foxdot", PRand(32)[:16], dur=1/4)

d1 >> play("<(X )( X)O ><[--]>< + + ( [ +])>")

Clock.clear()









