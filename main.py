#lets make a code to ask questions and diplay your personality based on the results.
print(''' 
This is a personality quiz!
~~~~~~~~~~~~~~~~~~~~~~
Answer these questions to get your MBTI!
      ''')
yourPersonality = ''
print('''
Question1
Do you find yourself drawing away from others or getting close to others?
Answer \'I\' for drawing away from others and \'E\' for getting closer to others.
      ''')
q1 = input().upper()
if q1 == 'I':
    yourPersonality += q1
    print('Oh! You are an introvert!')
elif q1 == 'E':
    yourPersonality += q1
    print('Wow! You\'re an extrovert!')
else:
    print('Enter either I or E')
print('''
Question2
Do you prefer to look at the big picture, with all the possibilities, innovations and creative ideas or would you prefer to go by facts and reasoning, basing yourself on realistic ideals?
Answer \'N\' if you look towards the big picture, or \'S\' if you are a realistic person.
      ''')
q2 = input().upper()
if q2 == 'N':
    yourPersonality += q2
    print('That must mean you are intuitive! Nice!')
elif q2 == 'S':
    yourPersonality += q2
    print('You would be a Sensing kind of person. That\'s pretty cool!')
else:
    ('Enter either N or S please.')
print('''
Question3
Do you tend to make decisions based on logical analysis, based off of fairness, pros and cons, etc, or are you more likely to make decisions emotionally or with sentiment, based on your own personal values, thoughts and opinions?
Answer \'T\' if you make decisions logically or \'F\' if you make decisions sentimentally.
      ''')
q3 = input().upper()
if q3 == 'T':
    yourPersonality += q3
    print('Your\'e a Thinker. That\'s amazing!')
elif q3 == 'F':
    yourPersonality += q3
    print('Being a Feel')
else:
    ('Enter either T or F please.')
print('''
Question4
Okay final question here! Do you feel more comfortable abiding to the rules, sticking to plans, and tend to be more organized or do you prefer to have your options open, act spontaneously, and be flexible with your plans?
Answer \'J\' if you are the rule abider or \'P\' if you like to be flexible with your options.
      ''')
q4 = input().upper()
if q4 == 'J':
    yourPersonality += q4
    print('So you\'re a judger! Super!')
elif q4 == 'P':
    yourPersonality += q4
    print('Perceivers are sooo wonderful though.')
else:
    ('Enter either J or P please.')
print('You\'ve completed the test! That\'s cool! So your personality is ' + yourPersonality)
