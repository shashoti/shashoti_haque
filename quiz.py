print("Which Pretty Little Liar are you?")
total = 0 

q1: input(str( "What's your favorite subject at school?\n(a) Art\n(b) Science\n(c) Ew School!\n(d) Gym\n"))
if q1  'a':
   total = total + 5 
elif q1 = 'b':
   total = total + 10 
elif q1 = 'c':
   total = total + 15
else:
   total = total + 20 
   
q2 = input(str("Pick a colour category!\n(a) Darks\n(b) Neutrals\n(c) Pastels\n(d) Primary Colours\n",))
if q2 = 'a':
   total = total + 5 
elif q2 ='b':
   total = total + 10 
elif q2 = 'c':
   total = total + 15
else:
   total = total + 20  

q3 = input(str("Choose an extra curricular activity!\n(a) Photography Club\n(b) Student Government\n(c) Cheerleading\n(d) A Sports Team\n"))
if q3 = 'a':
   total = total + 5 
elif q3 ='b':
   total = total + 10 
elif q3 = 'c':
   total = total + 15
else:
   total = total + 20  

q4 = input(str("How would you describe your style?\n(a) Funky\n(b) Formal\n(c) Girly\n(d) Tomboyish\n"))
if q4 = 'a':
   total = total + 5 
elif q4 ='b':
   total = total + 10 
elif q4 = 'c':
   total = total + 15
else:
   total = total + 20  

if 20 <= total < 40: 
   print "You are Aria"
elif 40 <= total < 60:
   print "You are Spencer" 
elif 60 <= total < 80: 
   print "You are Hanna"
else: 
   print "you are Emily" 
   

