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




mydrum = "C:/Users/sajjad/Desktop/drums135.wav"
kano = "C:/Users/sajjad/Desktop/kano.wav"

p1 >> loop(mydrum , dur = 1)

p1.stop()


p1 >> loop(mydrum, P[:4])

p1.stop()



p1 >> loop(mydrum, P[:4], tempo=135)

p1 >> loop(mydrum, P[:8]/2, dur=1/2, tempo=135)

p1 >> loop(mydrum, P[:4].offadd(1, 0.25), tempo=135)

p1 >> loop(mydrum, P[:4], tempo=135).every(4, "offadd", 1.5, 0.25)

p1 >> loop(mydrum, P[:4], tempo=135).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3)

p1 >> loop(mydrum, P[:4], tempo=135).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3).every(8, "shuffle")








Clock.bpm=140

p1 >> loop(kano, dur=4)

d1 >> play("x-o-")

# Ouch, not very good so far as we don't know the tempo!

p1 >> stretch(kano, dur=4)

# Sound better?

Clock.clear()








d1 >> play("X", dur=PDur(3, 8))

d1 >> play("X", dur=PDur(var([3,5], [6,2]), 8))

d1 >> play("X", dur=PDur(var([3,5], [6,2]), 8, var([0,1])))

d2 >> play(" -H-")

Clock.clear()










p1 >> pluck(oct=PStep(4, var([4,6], [6,2]), 5), dur=1/4)

p1 >> pluck(oct=PStep(4, var([4,6], [6,2]), 5), dur=1/4, formant=PRand(5))

d1 >> play("X", dur=PDur(var([3,5], [6,2]), 8, var([0,1])))

d2 >> play(" -H-")

Clock.clear()






print(var([0,1]), linvar([0,1]))






p1 >> dirt([0, 6, 4, 2], dur=1/4, hpf=linvar([0, 4000], 16))

p1.stop()





# We can even use a duration of 0 to instantly reset the linvar:

p1 >> dirt([0, 6, 4, 2], dur=1/4, hpf=linvar([0, 4000], 16))

p1.stop()









p1 >> dirt([0, 6, 4, 2], dur=1/4, hpf=linvar([0, 4000], [16, 0]), hpr=linvar([1,0.1],12), pan=linvar([-1,1], 4))

d3 >> play("<X:><  O >", lpf=linvar([0, 0, 4000, 100],[12, 0, 4, 0]))

b1 >> bass(var([0,2],8), dur=PDur(3,8), drive=0.5, formant=linvar([0,8],[16,0]), amp=1/2)

b1.stop()

Clock.clear()


def hello():
    print("Hello, the current beat is", Clock.now())

# This function prints a message to the console saying hello and the current clock beat.
# Activate (aka 'call') the function by running:

hello()





p1 >> pluck(P[:8], dur=1/4)

b1 >> sawbass(var([0, 2, 3, 4]))

d1 >> play("x-")


p1.stop()






Root.default=-3.5; Scale.default="minor"

#p1 >> loop(mydrum, P[:4], tempo=135).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3)

p2 >> stretch(kano, dur=4, amp=PDur(0,1).palindrome())

b1 >> sawbass(var([0,2,-1],[8,4,4]), dur=PDur(3,8))

p2.stop()
b1.stop()

b2 >> dirt(b1.pitch + P[0, 2, 4, 7].palindrome(), dur=1/4, oct=var([5,6],1), hpf=linvar([0,4000],16), drive=0.5)

d1 >> play("+", dur=PDur(var([3,5],[6,2]),8,var([0,1])), pan=linvar([-1,1],8), amp=1.5)

Clock.schedule(Clock.clear)










b1 >> bass([0, 1, -2], dur=[4, 4, 8])

b2 >> dirt(b1.pitch + [7, 4, 2, 0,], amp=PRand([0,1])[:16], dur=1/4, hpf=linvar([0,2000],16), hpr=linvar([1,0.1],12))

p1 >> blip(dur=PDur(3,8)*2, sus=4) + (0,9)

p2 >> space([b1.pitch + 2, 4], dur=[6, 2], sus=8)

p3 >> bell(P[b1.pitch,2,4,2][:6], dur=PDur(3,8), oct=6)

d1 >> play("X:")

Clock.clear()


b1.stop()

b2.stop()

p1.stop()

p2.stop()

p3.stop()

d1.stop()





print(PDur([1,2,3],2))


print (PDur(1,2,3))


p1 >> sitar(P[0,1,2,3], oct = 7 , formant = 3 , dur=PDur( [1,2,3], [1,2,3,4,5] ) )




p1 >> sitar(P[3,4,5] , oct = 7  , formant = 3 , dur = [1/2,1/4,1/4,1/2,1/2,1/2] )




p1 >> midi([0,1,2,3,4,5], dur=PDur(3,8), amp=[1,1/2,1/2]).every(6, "stutter", 4, dur=3, oct=6)

p1.stop()




p1 >> midi([0, 4])
 
p2 >> play("x * ")











print(Scale.names())

# To set the "default scale", just assign the scale name to Scale.default,
# and all the players will updated immediately:

p1 >> pluck((0, 2, 4))

p2 >> blip(P[:8], dur=1/2)

Scale.default = "minor"

Clock.clear()













print(Scale.major, Scale.major.pentatonic)

# You can specify a player object to use a different scale to the default
# by using the 'scale' keyword like so:

p1 >> pluck((0, 2, 4))

p2 >> blip(P[:8], dur=1/2)

p2 >> blip(P[:8], dur=1/2, scale=Scale.minor.pentatonic)

Clock.clear()








p1 >> pluck((0, 2, 4))

p2 >> blip(P[:8], dur=1/2).penta()

Scale.default = "major"

Scale.default = "minor"

Clock.clear()






p1 >> pluck((0, 2, 4))

p2 >> blip(P[:8], dur=1/2).penta()

Root.default = 2

Root.default = -2

Root.default = "F#"

Root.default = "Eb"

Root.default = var([0, 2], 8)

Clock.clear()








Root.default = 0

p2 >> blip([0, 7, 6, 4, 2], dur=1/4, sus=2, root=var([0, 2], 8))

Clock.clear()






p1 >> pluck(P[:4])

Clock.bpm = 130

Clock.bpm = 145

Clock.bpm = 100

Clock.clear()








p1 >> pluck(P[:4])

Clock.bpm = 10

Clock.update_tempo_now(100)

Clock.clear()






Clock.bpm = 120


p1 >> pluck((0, 2, [4, 6, 7]), dur=PDur(3,8), sus=2, chop=4)

d1 >> play("x-o-")

Clock.bpm = var([120, 60, 30], [12, 2, 2])

Clock.clear()










Clock.bpm = 120

p1 >> pluck([0, 2, 3, 4, 5], pan=-1)

p2 >> pluck([0, 2, 3, 4], pan=1, bpm=180)


# Part 2: Groups of players
# -------------------------

# When you have multiple players playing at once, it can be useful
# to stop/start or apply effects to groups of players in one command.
# FoxDot allows you to group players together by simply wrapping them
# in a Group() object:

p1 >> play("X-O-")

p2 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])

p3 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)

Group(p1, p2, p3).lpf = 400

Group(p1, p2, p3).lpf = 0

Group(p1, p2, p3).stop()









p1 >> play("X-O-")

p2 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])

p3 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)

p4 >> play("#", dur=32, amp=2)

Group(p1, p2, p3, p4).amplify=var([1, 0],[28, 4])

Clock.clear()







p1 >> play("X-O-")

p2 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])

p3 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)

p4 >> play("#", dur=32, amp=2)

p_all.amplify=var([1, 0],[28, 4])

p_all.stop()













d1 >> play("X-O-")

d2 >> play("#", dur=32, amp=2)

d3 >> play("{ +[ +]}")

p1 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])

p2 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)

d_all.lpf = 400

p_all.hpf = 1000

d_all.lpf = p_all.hpf = 0

Group(p_all, d_all).amplify = var([1,0], [28,4])

Clock.clear()














p1 >> pluck([0, 1, 2, 3], delay=[0, 0, 0.5])

p1.stop()









p1 >> pluck([0, 1, 2, 3], delay=[0, 0, (0, 0.5)])
 
# Delay a note to play *after* the following one

p1 >> pluck([0, 1, 2, 3], delay=[0, 0, (0, 1.5)])

p1.stop()










d1 >> play("X:")

p1 >> pluck(dur=1/4, amp=[1,1,1,1,1,0], amplify=var([1,0],[6,2])) 

Clock.clear()

# This is useful if you want to set Groups to be "on" or "off" at the same time:

d1 >> play("X:")

p1 >> pluck(dur=1/4, amp=[1,1,1,1,1,0])

p2 >> bass(var([0, 3], 8), dur=1/2)
 
p_all.amplify = var([1,0], [14,2])

Clock.clear()












p1 >> pluck([0, 1, 2, 3], shape=var([0, 0.25, 0.5, 1]))

p1.stop()

# <Fx 'vibrato' -- args: vib, vibdepth>

p1 >> pluck([0, 1, 2, 3], vib = var([0, 4, 12, 25]))

p1 >> pluck([0, 1, 2, 3], vib = var([0, 4, 12, 25]), vibdepth=var([0.01, 0.05, 0.1, 0.5], 32))

p1.stop()

# <Fx 'tremolo' -- args: tremolo, beat_dur>

p1 >> pluck((0, 2, 4), dur=4, tremolo=[0, 2, 4, 8])

p1.stop()











p1 >> pluck(P[0, 1, 2, 3])

p1 >> pluck(P[0, 1, 2, 3].offadd(2))

p1 >> pluck(P[0, 1, 2, 3], pan=P[-1,1])

p1 >> pluck(P[0, 1, 2, 3], pan=P[-1,1].offmul(-1))

p1.stop()

# This can be really useful when combined with the "every" method

p1 >> pluck([0, 4], dur=PDur(3,8)).every(3, "offadd", 2)

p1.stop()











p1 >> pluck([0, 4, 6, 7], lpf=4000, lpr=0.2).every(3, "lpf.offmul", 1/2)

p1.stop()

# We can also specify the duration to delay the note by, which defaults
# to half a beat, by specifying an extra argument, either named or un-named

p1 >> pluck(P[0, 1, 2, 3].offadd(2, dur=0.75))

p1 >> pluck(P[0, 1, 2, 3].offadd(2, 0.75))

p1 >> pluck(P[0, 1, 2, 3]).every(4, "offadd", 2, dur=0.25)

p1.stop()









p1 >> pluck(P[:8])

p1 >> pluck(P[:8].trim(3))

p1.stop()









p1 >> pluck(P[:8])

p1 >> pluck(P[:8].trim([3, 2]))

p1.stop()












p1 >> play(P["x-o-"].trim([3, 2]))

p1.stop()

# And, of course, can be used with the 'every' method:

p1 >> play("x-o-").every([12, 4], "trim", 3)

p1 >> play("x-o-").every([12, 4], "trim", [3, 2])

# Add some bass and percussion and it sounds like an organic drum fill

b1 >> bass(var([0, 1, 5, 3]), dur=1/2, drive=0.2)

b2 >> play("#", dur=16)

Clock.clear()










print(P["x-i-"].amen())









Clock.bpm=140

p1 >> play(P["x-i-"].amen())

p1 >> play("x-i-").every(8, "amen")

# Add some bass and percussion again...

b1 >> bass(var([0, 1, 5, 3]), dur=1/2, drive=0.2)

b2 >> play("#", dur=16)

Clock.clear()















p1 >> pads()

p1 >> pads(2)

p1 >> pads([0,2,4])

p1.stop()

















p1 >> pads((0,2,4))

p1 >> pads([0,1,2,(3,5,7)])

p1.stop()









p1 >> pads([0,2,[4,7]])

p1.stop()



















p1 >> pads([0,1,2,3], dur=1)

p1 >> pads([0,1,2,3], dur=1/2)

p1 >> pads([0,1,2,3], dur=[1,1/2])

p1.stop()
















p1 >> pads([0,1,2,3], dur=[1,1/2,1/2])











d1 >> play("x-o-")

d1.stop()

# Each character is mapped to a folder of samples. "x" is a kick drum, "-" is a hi-hat, and "o" is a snare.
# To select a different file in the folder, we use the "sample" keyword:

d1 >> play("x-o-", sample=1)

d1 >> play("x-o-", sample=2)

d1 >> play("x-o-", sample=[0,1,2])

d1.stop()

# It can be a list of numbers too! We can make our drum pattern more complex by using brackets

d1 >> play("x-o[--]")

d1 >> play("x-o(-o)")

d1 >> play("x-o{-o*}")

d1.stop()

# Can you work out what the brackets are doing? The square bracket plays multiple samples in the
# space of one step:

d1 >> play("x-o[--]")

d1 >> play("x-o[---]")

d1 >> play("x-o[-------]")

d1.stop()

# The round brackets alternates the sound used:

d1 >> play("x-o(-o)")

d1 >> play("x-o(-[-o])")

d1 >> play("x-o(-[-(-o)])")

d1.stop()

# And the curly braces selects a sample at random for more variety

d1 >> play("x-o{-o}")

d1 >> play("x-o{-[--]o}")

d1.stop()

# Just like before we can use keyword arguments:

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1])

# You can also change the rate the audio is played 

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=1)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=2)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=0.5)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=-1)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=[1,2,0.5,-1])

d1.stop()

# To play things at the same time, just use multiple Players. Try changing the values and adding keyword
# arguments to the code below:

p1 >> pads([0,2,4,9,7], dur=1/4)

d1 >> play("x-x-")

d2 >> play("  * ")

# To stop everything, press "Cmd+." or run the line of code below.

Clock.clear()














x1 >> blip([0,2,3,4])

# Every 3 beats, play a note on the off-beat that is 4 steps higher

x1 >> blip([0,2,3,4]).every(3, "offadd", 4) 

# You can "chain" more than one repeated function together, just like you did with "stop" earlier:

x1 >> blip([0,2,3,4]).every(3, "offadd", 4).every(7, "stutter", 4)

# Try changing some of the keywords

x1 >> blip([0,2,3,4]).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6)

# Chain together as many different functions as you like!

x1 >> blip([0,2,3,4]).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=5).every(8, "reverse")











p1 >> blip(dur=4, sus=1)

p1 >> blip(dur=4, sus=1, room=1, mix=0.5)

p1 >> blip(dur=1, sus=1, room=[0,0.25,0.5,1], mix=[0, 0.1, 0.3, 0.5])

p1.stop()

# Could you hear the difference? Below are some other effects to try out. See if
# you can apply them to other SynthDefs, not just the ones written below. Remember
# Ctrl+. will stop all the sound.

# High Pass Filter - only lets frequencies *above* this value into the signal

d1 >> play("x-o-")

d1 >> play("x-o-", hpf=500)

d1 >> play("x-o-", hpf=5000)

d1 >> play("x-o-", hpf=[0,100,250,500,1000,2000,4000,8000])

d1.stop()

# Low pass filter - only lets frequences *below* this value into the signal

d1 >> play("x-o-")

d1 >> play("x-o-", lpf=5000)

d1 >> play("x-o-", lpf=500)

d1 >> play("x-o-", lpf=[50,100,200,400,800,1600,3200,6400])

d1.stop()

# Chop - chops the signal into "n" parts

p1 >> pluck([0,4], dur=4, chop=4)

p1 >> pluck([0,4], dur=4, chop=8)

p1 >> pluck([0,4], dur=4, chop=320)

p1.stop()

# -- What happens when you use a different sustain than duration?

p1 >> pluck([0,4], dur=[3/4,3/4,1/2], chop=4)

p1 >> pluck([0,4], dur=[3/4,3/4,1/2], chop=4, sus=2)

p1.stop()

# Shape - wave shape distortion

b1 >> bass(dur=8)

b1 >> bass(dur=8, shape=0.5)

b1 >> bass(dur=8, shape=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

# -- Try combining different effects in the same player:
    
b1 >> bass(dur=8, shape=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], chop=16, room=0.5, mix=0.2)











p1 >> blip(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate() | P[[9,11]], dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

d1 >> play("Xs")

b1 >> dbass([0, 2, 3, 4], dur=8)

Clock.clear()














p1 >> blip(P[:10:2], dur=PDur(5,8)*2, sus=2, oct=PStep(7,5,6)).every(6, "reverse").often("trim", 3).every(9, "stutter", 4, dur=3)

d1 >> play("Xs")

b1 >> dbass([0, 2, 3, 4], dur=8)

Clock.clear()









p1 >> blip(PRand(0, 8))

p1.stop()

# Generate random values from a list

p1 >> blip(PRand([0, 2, 4]))

p1.stop()












p1 >> blip(pan=PWhite(-1, 1), amp=PWhite(0, 1))

p1.stop()

# A cool example of combining indexing and random values to create interesting rhythms:

d1 >> play("x-o ")


p1 >> blip(dur=1/4, amp=PRand([0,1])[:8])













b1 >> bass([0, 3], dur=8)

# What if we want to change the duration but keep playing the notes for 8 beats each?

b1 >> bass([0, 3], dur=PDur(3,8))










b1 >> bass(var([0, 3], dur=8), dur=PDur(3,8))

b1.stop()

# It played each pitch for 8 beats each, even though the durations were less than 8.
# We create a "var" by using the code - var(list_of_values, dur=duration)

b1 >> bass(var([0, 3], dur=8), dur=PDur(3,8))

# Notice the difference between changing the duration in the bass and the duration in the var

b1 >> bass(var([0, 3], dur=8), dur=PDur(5,8))

b1 >> bass(var([0, 3], dur=[6, 2]), dur=PDur(5,8))

b1.stop()













b1 >> sawbass([0,-1,3], dur=[4,4,8])

# Let's create a var called "chords" so we can use in more than player:

var.chords = var([0,-1,3], dur=[4,4,8])

b1 >> sawbass(var.chords, dur=1)

# We can now change the duration to whatever we want...

b1 >> sawbass(var.chords, dur=PDur(3,8)*2)

# ...and other instructions to create interesting patterns!

b1 >> sawbass(var.chords, dur=PDur(3,8)*2, oct=[5,5,[6,4],5], pan=[0,[-1,1]]) + [0,0,4,0,7]

# We can use the "var.chords" variable as a single note in a list:

p1 >> blip([var.chords,2,3,4], sus=2)

# Listen to the first note in the sequence, it changes with the chords. We can continue
# to add all sorts of functions to the sequence to make it more interesting

p1 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4)

p1 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6)

p1 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6).every(8, "reverse")

# Now let's introduce our triads again. This time we'll use "var.chords" instead
# of "b1.pitch" when adding (0, 2, 4).

p2 >> star(var.chords + (0, 2, 4), dur=PDur(3,8))

# Question: What happens if we do use b1.pitch? Why does it happen?

p3 >> star(b1.pitch + (0, 2, 4), dur=PDur(3,8))

p3.stop()
# Let's introduce some percussion again!

d1 >> play("x-")

d2 >> play("  H ")
















var.filter = var([0,8000], dur=[28,4])

d1 >> play("x-", hpf=var.filter)

d2 >> play("  H ", hpf=var.filter)













p1 >> pads(P(0, 2, 4, 6), dur=4)

p1.stop()

# PGroups can also be used to play notes in quick succession by putting
# different symbols between the 'P' and the brackets:

p1 >> pads(P(0, 2, 4, 6), dur=4)    

p1 >> pads(P*(0, 2, 4, 6), dur=4)

p1 >> pads(P*(0, 2, 4, 6), dur=2)

p1.stop()

# Notice the difference? The P* plays all the notes across the note's
# duration - just like the square brackets in the "play" synth. You
# can use the + symbol to spread the notes over a note's sustain
# as opposed to the duration, which can be useful when using varying
# lengths of durations:
    
p1 >> pluck(P*(0, 4), dur=PDur(3,8), sus=1)

p1 >> pluck(P+(0, 4), dur=PDur(3,8), sus=1)

p1 >> pluck(P+(0, 4), dur=PDur(3,8), sus=2)

p1.stop()















p1 >> pluck(P^(0, 2, 4, 0.5), dur=4) # delay of 0.5 beat

p1 >> pluck(P^(0, 2, 4, 0.75), dur=2) # delay of 0.75 beat

p1 >> pluck([P*(0, 3), P^(0, 2, 4, 0.75)], dur=2) # Combining multiple PGroups

p1.stop()

# So P[:4].offadd(4) is essentially just P[:4] + P^(0, 4, 0.5)!

p1 >> pluck(P[:4].offadd(4))

p1 >> pluck(P[:4] + (P^(0,4,0.5)))

p1.stop()

# These are useful to create variations in rhythm without having to create a
# complex "dur" argument. e.g. to create the simple melody below:
    
p1 >> pluck([[0, P*(0, 0)], 2, -3, 2])

# We would need to do this:
    
p1 >> pluck([0, 2, -3, 2, 0, 0, 2, -3, 2], dur=P[1,1/2,1].stutter([4,2,3]))

p1.stop()











d1 >> play("xs", sample=2)

d2 >> play("  * ", sample=2)

d3 >> play("(+  )+( [( +)+])", sample=2)

Clock.clear()











d1 >> play("<xs><  * ><(+  )+( [( +)+])>", sample=2)

d1.stop()

# Make sure there are no spaces between the different patterns! You
# can also use these brackets to play individual samples together in
# a sequence like this:
    
d1 >> play("x-<*><o>-")

# Although sometimes its easier to split them up into separate sequences:
    
d1 >> play("<x-*-><  o >")

d1.stop()















d1 >> play("x-*-", sample=[0,0,2,0])

d1.stop()

# But what happens when you change the sequence?

d1 >> play("x-*(-[-*])", sample=[0,0,2,0])

# You then need to *also* update the sample keyword argument to this:

d1 >> play("x-*(-[-*])", sample=[0,0,2,[0,(0,2)]])

d1.stop()













d1 >> play("x-|*2|-")

d1 >> play("x-|*2|(-[-|*2|])")

d1.stop()

# You can also use sequences / patterns in this way too!

d1 >> play("x-o|n[01]|")

d1 >> play("x-|o(02)|-")

d1 >> play("x-|o(0[20])|-")

d1 >> play("x-o|a{0123}|")

d1.stop()

# Note: This overrides the sample keyword

d1 >> play("x-*-", sample=2)

d1 >> play("x-|*1|-", sample=2)

d1.stop()

# Put this all together for a funky beat in one line of text:

d1 >> play("<|x2|s><  |*(3[33])| ><(+  )+( [( +)+])>", pan=P(0, 0, [-1,1]))

d1.stop()









Scale.default = "minor"

print(SynthDefs) # Pick your own synths!

b1 >> sawbass(var([0, 2], 8), dur=1)

p1 >> keys(b1.pitch + (0, 2, 4), dur=8)

p2 >> blip(P[0, 2, 4].stretch(8), dur=1/2, sus=2) + var([0, 2], [6, 2])
    
d1 >> play("<xs><  * ><(+  )+( [( +)+])>")

Clock.clear()


























