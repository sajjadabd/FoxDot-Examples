p1 >> play("N", sample=1)


mySynth = SynthDef("mySynth")

p1 >> mySynth(new_arg=[0,10,100])


p1 >> pluck(var([0,3,4,3]) + [0, 2, 2, 2], pshift=[0,0,1,0])



p2 >> blip([[0, 4], [2, 6], [3, 7], [2, 6], 3, 5, 5.5, 5])



p1 >> play("x-", dur=1/2)


p1 >> play("x-o-[xx]-o-x-o-[xx]-o[-o]")



p1 >> pads([0,1,2,3], dur=[1/4,3/4], sus=1, rate=4, scale=Scale.minor)



bd >> play("x( x)  ")

hh >> play("---[--]")

sn >> play("  o ")


p1 >> pluck()

p1 >> pluck([0,2,4], dur=[1,1/2,1/2], amp=[1,3/4,3/4])


p1 >> pluck(dur=1/2).follow(b1) + (0,2,4) # This adds a triad to the bass notes


d1 >> play("x-o-")



d1 >> play("xxox")


hh >> play("---(-=)", pan=0.5)





d1 >> play("x[--]o(=[-o])")





p1 >> pluck(PRange(5) | PRange(5,0,-1), scale=Scale.default.pentatonic)







p1 >> pluck(PTri(5), scale=Scale.default.pentatonic)






Scale.default="minor"
Clock.bpm=140

# Shift a sample's pitch
p2 >> play("C", dur=2, pshift=[0,1,2,3])

c1 >> play("@", dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4, pan=-0.5)
c2 >> play("#", dur=20, room=1, amp=2, pan=0.5)
d1 >> play("")
b1 >> dbass(dur=PDur(3,8), sus=2, chop=4, shape=PWhite(0,1/2), pan=PWhite(-1,1)).sometimes("offadd", 4) + var([0,2],4)
p1 >> space([7,6,4,P*(2,1),0], dur=8, pan=(-1,1))
Master().hpf=var([0,4000],[76,4])

p2.stop()

c1.stop()
c2.stop()
d1.stop()
b1.stop()
p1.stop()

p1 >> play("x-o-")





# Simple pattern
p1 >> play("(x-)(-x)o-")

# Nested brackets for more variety
p1 >> play("(x-)(-(xo))o-")




# Plays a triplet on the fourth steps
p1 >> play("x-o[---]", dur=1)

# Can be used in the round brackets
p1 >> play("(x-)(-[-x])o-")

# Can contain round brackets
p1 >> play("x-o[-(xo)]")



# Randomly pick a sample on the fourth step
p1 >> play("x-o{-ox}")

# Can contain [square brackets]
p1 >> play("x-o{[--]ox}")

# Can be put inside square brackets
p1 >> play("x-o[-{ox}]")


p1 >> play("x-o-", sample=1)



p1 >> play("x-o-", sample=[0, 1, 2])

p1 >> play("x-o-", sample=(0, 3))







# Plays sample=2 for the 'o' character
p1 >> play("x-|o2|-")

# Will override the sample keyword
p1 >> play("x-|o2|-", sample=3)






# Alternate the sample number
p1 >> play("x-|o(12)|-")

# Alternate the sample character
p1 >> play("x-|(o*)2)-")

# Play multiple different samples in one step
p1 >> play("x-|o[23]|-")

# Play random sample selection
p1 >> play("x-|o{1[23]}|-")




p1 >> play("x-o-")
p2 >> play("  + + [ +]")



# "Layers" the two sequences
p1 >> play("<x-o-><  + + [ +]>")

# Equivalent to:
p1 >> play(P["x-o-"].zip(P["  + + [ +]"]))






# Hard pan each sequence to left and right channels
p1 >> play("<x-o-><  + + [ +]>", pan=(-1, 1))

# Change the sample used in the first layer
p1 >> play("<x-o-><  + + [ +]>", sample=(2, 0))



p1 >> play("<x-o-><  + + [ +]>", sample=(2, 0)).every(4, "sample.offadd", 2)





# Slide effect added
p1 >> pluck(dur=4, slide=1, slidedelay=0.5)

# Slide effect not added
p1 >> pluck(dur=4, slide=0, slidedelay=0.5)

# Slide effect added, with zero delay
p1 >> pluck(dur=4, slide=1, slidedelay=0)




# One beat duration, half-beat duration
p1 >> pluck(dur=1, sus=1/2)





# Doubles the length of every other note
p2 >> pluck(dur=PDur(3,8), blur=[1, 2])




# Alternate between left, center, and right
p1 >> pluck(pan = [-1, 0, 1])

# Play two notes at the same time, but in different speakers
p1 >> pluck((0, 4), pan=(-1,1))

# Gradually move the sound's panning from left to right using a "linvar"
p1 >> pluck([0, 2, 4, 7], dur=1/4, pan=linvar([-1,1],8))




# Simple flanger effect
p1 >> pluck(fmod = 2)

# Vary the effect over time
p1 >> pluck(fmod=linvar([-10,10],8), dur=1/4, sus=1)






p1 >> pads(dur=4, vib=4)

p1 >> pads(dur=4, vib=4, vibdepth=0.1)

p1 >> pads(dur=4, vib=4, vibdepth=1)





# Slide one octave up
p1 >> pluck(dur=4, slide=1)

# Slide to 0
p1 >> pluck(dur=4, slide=-1)

# Delay the slide effect to start half way through the note
p1 >> pluck(dur=4, slide=0.5, slidedelay=0.5)





# Slide from one octave up
p1 >> pluck(dur=4, slidefrom=1)

# Slide from 0
p1 >> pluck(dur=4, slidefrom=-1)

# Delay the slide effect to start half way through the note
p1 >> pluck(dur=4, slidefrom=0.5, slidedelay=0.5)





# Bends one octave up and back again
p1 >> pluck(dur=4, bend=1)

# Bend to 0 and back again
p1 >> pluck(dur=4, bend=-1)

# Delay the bend effect to start half way through the note
p1 >> pluck(dur=4, slide=0.5, bend=0.5)







# Using chop
c1 >> play("C", dur=4, chop=16, coarse=0)

# Using coarse
c1 >> play("C", dur=4, coarse=16, chop=0)





b1 >> bass(dur=2, chop=4, coarse=0)



b1 >> bass(dur=2, coarse=4, chop=0)






# Set the high pass filter cutoff to 2000 Hz
d1 >> play("x-o-", hpf=2000)


# Set the cutoff to change over time using a linvar
d1 >> play("x-o-", hpf=linvar([0,2000],32))




# Set the high pass filter cutoff to 2000 Hz
d1 >> play("x-o-", hpf=2000)

# Set the resonance to 0.2 - can you hear the difference?
d1 >> play("x-o-", hpf=2000, hpr=0.2)


# Set the cutoff *and* resonance to change over time using linvar
d1 >> play("x-o-", hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28))






# Set the low pass filter cutoff to 400 Hz
d1 >> play("x-o-", lpf=400)

# Changing the resonance - can you hear the difference?
d1 >> play("x-o-", lpf=400, lpr=0.2)

# Use a linvar to vary both values over time
d1 >> play("x-o-", lpf=linvar([500,5000],32), lpr=linvar([1,0.1],28))



d1 >> play("X" , crush=4)

d1 >> play("O" , crush=4)

d1 >> play("X O X X O ", crush=4)


# Apply the bit-crusher effect
d1 >> play("X O ", crush=4)


# Reduce the number of bits for more distortion
d1 >> play("X O ", crush=4, bits=4)


# Or reduce the sample rate for a different style of distortion!
d1 >> play("X O ", crush=32, bits=8)





# Add distortion to both sample and synth players
d1 >> play("x * ", dist=0.2)


p1 >> dirt([0,5], dist=0.3, dur=8) + (0,4)




# Add distortion to both sample and synth players
d1 >> play("x * ", shape=0.5)

p1 >> dirt([0,5], shape=0.5, dur=8) + (0,4)





# Add overdrive distortion
p1 >> dirt(dur=1/2, drive=1)






# Emulate playing the sounds in a small room
p1 >> play("x o ", room=0.25)

# Emulate playing the sounds in a larger room
p1 >> play("x o ", room=0.8)

# Make the signal more 'wet'
p1 >> play("x o ", room=0.8, mix=0.8)




# We don't hear any echo effect
d1 >> play("x-o-", dur=1, echo=0.75)

# Add reverb and we do
d1 >> play("x-o-", dur=1, echo=0.75, room=0.5)







# Only hear one echo
p1 >> blip(dur=4, echo=1)

# Now we hear several
p1 >> blip(dur=4, echo=1, echotime=8)

# We can use echo to make drum loops more interesting too
d1 >> play("(x )( x)o ", room=0.1, echo=0.75/2, echotime=4)




# Move the pan left to right 4 times across 4 beats
p1 >> pads(dur=4, spin=4)

# Move the pan left to right 4 times across 1 beat
p1 >> pads(dur=4, sus=1, spin=4)






# Stop a sound immediately instead of it's natural decay
p1 >> pads(dur=4, cut=0.75)

# Shorten samples to a tenth of their normal length
d1 >> play("x-o-", cut=0.1)






# Loop through the different levels we can apply the filter
p1 >> pluck(formant=P[:8])







p1 >> pads(dur=4, tremolo=2)






# Shift a synth's pitch
p1 >> pads(pshift=[0,1,2,3])

# Shift a sample's pitch
p2 >> play("C", dur=2, pshift=[0,1,2,3])

# Can be used to make chords
p2 >> play("C", dur=2, pshift=[0, (0,4,7)], sample=3)
