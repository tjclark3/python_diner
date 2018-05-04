mainMenu = ['3 Finger', 'Box Combo', 'Caniac Combo'];
sideMenu = ['Fries', 'Texas Toast', 'Cole Slaw'];

total = 0;

user = input('We have 3 options: 3 Finger, Box Combo, and Caniac Combo. WHich would you like to order?');

if user == '3 Finger':
  print('Not very hungry? Well which sides would you like with that?')
  total = total + 5
  print(f'You owe me ${total}')

elif user == 'Box Combo':
  print ('This is the most popular combo. Which sides would you like with that?')
  total = total + 7
  print(f'You owe me ${total}')

elif user == 'Caniac Combo':
  print ('Pretty hungry huh? Well which sides would you like with that?')  
  total = total + 10
  print(f'You owe me ${total}')

else:
  print ('Sorry these are our only options please choose either 3 Finger, Box Combo, or Caniac Combo.')

user = input ('Fries, Texas Toast, or Cole Slaw.')

if user == 'Fries':
  print ('Fries are great! Which other side would you like?')
  total =total + 2
  print(f'You owe me ${total}')

elif user == 'Texas Toast':
  print ('Texas Toast is the best! Which other side would you like?')
  total = total + 2
  print(f'You owe me ${total}')

elif user == 'Cole Slaw':
  print ('I don\'t like cole slaw at all!!! So the more you order the less I have to smell it. What other sides would you like?')  
  total = total + 1
  print(f'You owe me ${total}')


user = input ('What is your final choice in a side.')

if user == 'Fries':
  print ('Great choice. Enjoy your meal.')
  total =total + 2
  print(f'You owe me ${total}')

elif user == 'Texas Toast':
  print ('MMMMMM Texas Toast is the best! Enjoy your meal.')
  total = total + 2
  print(f'You owe me ${total}')

elif user == 'Cole Slaw':
  print ('Well if you really want it... Enjoy your meal.')  
  total = total + 1
  print(f'You owe me ${total}')