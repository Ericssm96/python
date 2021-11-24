def vote(x):
    from datetime import date
    age = date.today().year - x
    if 18 <= age < 60:
        return 'MANDATORY.'
    elif age < 16:
        return 'DENIED.'
    elif 16 <= age < 18 or age > 60:
        return 'OPTIONAL.'


n1 = int(input('What year were you born in? '))
r1 = vote(n1)
print(f'Since you were born in {n1}, your voting status is {r1}')
