p1 >> pluck(P[0, 3 , 2, 1, 4].reverse().stutter(8), dur=[1/2,1/4,1/4,1/2]) + (0, 2, 4)

p2 >> play("X-O-")

p2.stop()

p3 >> play("x-o-")

p3.stop()

help(TimeVar)

p1 >> pluck(var([0, 3, 0, 4], 8), dur=[1,1/4,1/4,1/2]) + (0, 2, 4)

p1.stop()

p2 >> piano(var([0, 3, 0, 4], 8), dur=[1,1/4,1/4,1/2]) + (0, 2, 4)

p2.stop()

p3 >> blip(var([0, 3, 0, 4], 8), dur=[1,1/4,1/4,1/2]) + (0, 2, 4)

p3.stop()


p1 >> pluck(dur=1/4, pan=linvar([-1, 1], 8))

# Skip every 3rd note
p1 >> pluck([0, 1, 2, 3], dur=[1, 1, 0])

# Rest every 3rd note for 2 beats
p1 >> pluck([0, 1, 2, 3], dur=[1, 1, rest(2)])






# Play the major scale by default
p1 >> pluck([0, 2, 4, 6, 7])

# Change to minor
p1 >> pluck([0, 2, 4, 6, 7], scale=Scale.minor)



p1 >> pluck([0, 2, 4, 6, 7], scale=Scale.aeolian)



p1 >> pluck([0, 2, 4, 6, 7], scale=Scale.majorPentatonic)





# Start a player in the default scale (Major)
p1 >> pluck([0, 2, 4, 6, 7])

# Change the default scale to Dorian
Scale.default = Scale.dorian





p1 >> pluck(
      dur=1/4, 
      amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1]
)




p1 >> pluck(
    dur=1/4, 
    amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1], 
    amplify=var([1,0],[6,2])
) 









p1 >> pluck(dur=1/4, amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1])
p2 >> bass(var([0, 3], 8), dur=1/2)

Group(p1, p2).amplify = var([1,0],4)





# One beat duration, half-beat duration
p1 >> pluck(dur=1, sus=1/2)






# Simple flanger effect
p1 >> pluck(fmod = 2)
 
# Vary the effect over time
p1 >> pluck(fmod=linvar([-10,10],8), dur=1/4, sus=1)






# Chop a sound into 4 parts
p1 >> pluck([0,1,2,3], dur=4, chop=4)
 
# If the duration varies, the sizes of chop will vary too
p1 >> pluck([0,[4,6,7]], dur=PDur(3,8), chop=4)
 
# Changing a single value for "sus" evens out the sizes and creates a nice overlapping echo effect
p1 >> pluck([0,[4,6,7]], dur=PDur(3,8), chop=4, sus=2)


p3 >> play("V-")







# Using chop
c1 >> play("C", dur=4, chop=16, coarse=0)
 
# Using coarse
c1 >> play("C", dur=4, coarse=16, chop=0)







# Apply the bit-crusher effect
d1 >> play("X O ", crush=4)
 
# Reduce the number of bits for more distortion
d1 >> play("X O ", crush=4, bits=4)
 
# Or reduce the sample rate for a different style of distortion!
d1 >> play("X O ", crush=32, bits=8)






# Add distortion to both sample and synth players
d1 >> play("x * ", dist=0.2)
 
p1 >> dirt([0,5], dist=0.3, dur=8) + (0,4)








# We don't hear any echo effect
d1 >> play("x-o-", dur=1, echo=0.75)
 
# Add reverb and we do
d1 >> play("x-o-", dur=1, echo=0.75, room=0.5)






# Move the pan left to right 4 times across 4 beats
p1 >> pads(dur=4, spin=4)
  
# Move the pan left to right 4 times across 1 beat
p1 >> pads(dur=4, sus=1, spin=4)







# Stop a sound immediately instead of it's natural decay
p1 >> pads(dur=4, cut=0.75)
  
# Shorten samples to a tenth of their normal length
d1 >> play("x-o-", cut=0.1)


d1 >> play("x-o-")







# Glide to and from the 5th note in the scale (7th semitone)
p1 >> pluck([0, 4], dur=4, glide=[7,-7])






exit()


chords = var([0, 4, 5, 3])

p1 >> blip(chords + (0, 2, 4), dur=4)

p2 >> pasha(chords + [0, 2, 3, 4, 7, 9], dur=1/4)




