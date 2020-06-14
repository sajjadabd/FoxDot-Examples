
p1 >> pluck([0,2,4], dur=[1,1/2,1/2], amp=[1,3/4,3/4])

b1 >> bass([(0,9),(3,7)] , amp = 0.2 , dur=4, pan=(-1,1))

b1 >> bass([0,2,3,4], dur=4)


p1 >> pluck(dur=1/2).follow(b1) + (0,2,4) # This adds a triad to the bass notes
