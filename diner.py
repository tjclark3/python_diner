mainMenu = ['3 Finger', 'Box Combo', 'Caniac Combo'];
sideMenu = ['Fries', 'Texas Toast', 'Cole Slaw'];

subTotal = 0;

user = input('We have 3 options: 3 Finger, Box Combo, and Caniac Combo. WHich would you like to order?');

if user == '3 Finger':
  print ('Not very hungry? Well which sides would you like with that?')
  print (subTotal + 5)
elif user == 'Box Combo':
  print ('This is the most popular combo. Which sides would you like with that?')
  print (subTotal + 7)
elif user == 'Caniac Combo':
  print ('Pretty hungry huh? Well which sides would you like with that?')  
  print (subTotal + 10)
else:
  print ('Sorry these are our only options please choose either 3 Finger, Box Combo, or Caniac Combo.')

user = input ('Please choose your sides now: Fries, Texas Toast, or Cole Slaw.')

if user == 'Fries':
  print ('Fries are great! Which other side would you like?')
  print (subTotal + 2)
elif user == 'Texas Toast':
  print ('Texas Toast is the best! Which other side would you like?')
  print (subTotal + 2)
elif user == 'Cole Slaw':
  print ('I don\'t like cole slaw at all!!! So the more you order the less I have to smell it. What other sides would you like?')  
  print (subTotal + 1)