import math
from random import randint
from .models import CleanRobot
from django.shortcuts import render


# Home page
def home(request):
    return render(request, 'calculate/home.html')


def calculate(request):

    num1 = int(request.GET.get('a'))
    num2 = int(request.GET.get('b'))
    print(num1)
    print(num2)
    ans = []

    if request.GET.get('Manual'):
        c = round(math.sqrt(math.pow(num1, 2) + math.pow(num2, 2)), 1)
        ans.append(c)
        cleanRobot = CleanRobot.objects.create(name=1, positionX=num1, positionY=num2)
        cleanRobot.save()

    elif request.GET.get('Automatic'):
        ans1 = [x for x in range(1, 20, 1)]  # Calcuation of X
        ans2 = [(randint(1, 2) * y) for y in range(0, len(ans1), 1)]  # Calcuation of Y
        vel = [round(math.sqrt((math.pow(ans1[i], 2) + math.pow(ans1[i], 2)))/1, 2) for i in range(0, len(ans1), 1)]  # Calcuation of Velocity
        ang = [round((ans1[j] / ans2[j]) * (180/math.pi), 2) for j in range(1, len(ans1), 1)]  # Calcuation of Angle

        polaczenie = list(zip(ans1, ans2, vel, ang))
        for posX, posY, v, a in polaczenie:
            cleanRobot = CleanRobot.objects.create(name=2, positionX=posX, positionY=posY, velocity=v, angleTHETA=a)
            cleanRobot.save()

        ans = polaczenie

    elif request.GET.get('Error'):
        ans = f'The robot has broken down, you need to get it serviced!'

    elif request.GET.get('Idle'):
        ans = f'The robot is waiting for a task'

    return render(request, 'calculate/calc.html', {"answer": ans})

