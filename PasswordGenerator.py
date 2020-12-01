import random

print('''
Password Generator
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@Â£$%^&*().,?0123456789'

nummer = input('aantal wachtwoorden?')
nummer = int(nummer)

lengte = input('wachtwoord lengte?')
lengte = int(lengte)

print('\nhier zijn je wachtwoorden:')

for pwd in range(nummer):
  password = ''

  for c in range(lengte):
    password += random.choice(chars)
  print(password)
