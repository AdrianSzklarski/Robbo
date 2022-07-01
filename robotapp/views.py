import math
import os
from random import randint

import numpy as np
from django.shortcuts import render, redirect
from robotapp.calculate import Calc
from robotapp.forms import Robo


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

    elif request.GET.get('Automatic'):
        ans1 = ([x for x in range(0, 20, 1)])  # X
        ans2 = ([(randint(1, 2) * y) for y in range(0, 20, 1)])  # Y
        ans3 = np.concatenate([ans1, ans2])
        ans = f'X: {ans3[ans1]} Y: {ans3[ans2]}'

    elif request.GET.get('Error'):
        ans = f'The robot has broken down, you need to get it serviced!'

    elif request.GET.get('Idle'):
        ans = f'The robot is waiting for a task'

    return render(request, 'calculate/calc.html', {"answer": ans})



    # WZÓR na SAVE
    # template_name = 'Files/note.html'
    #
    # def get(self, request, *arg, **kwargs):
    #     textN = NoteAddForm()
    #     return render(request, self.template_name, {'textN': textN})
    #
    # def post(self, request, *arg, **kwargs):
    #     form = NoteAddForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    #     else:
    #         print(form.errors)
    #     return render(request, self.template_name, {'textN': form})


    # DZIAŁAJĄCY BLOK
    # num1 = int(request.GET.get('value1'))
    # num2 = int(request.GET.get('value2'))
    # print(num1)
    # print(num2)
    # ans = []
    #
    # if request.GET.get('Manual'):
    #     c = round(math.sqrt(math.pow(num1, 2) + math.pow(num2, 2)), 1)
    #     ans.append(c)
    #
    # elif request.GET.get('Automatic'):
    #     ans1 = ([x for x in range(0, 20, 1)])  # X
    #     ans2 = ([(randint(1, 2) * y) for y in range(0, 20, 1)])  # Y
    #     ans3 = np.concatenate([ans1, ans2])
    #     ans = f'X: {ans3[ans1]} Y: {ans3[ans2]}'
    #
    # elif request.GET.get('Error'):
    #     ans = f'The robot has broken down, you need to get it serviced!'
    #
    # elif request.GET.get('Idle'):
    #     ans = f'The robot is waiting for a task'
    #
    # return render(request, 'calculate/calc.html', {"answer": ans})



# Save?
# def calculate(request):
#
#     def get(self, request, *arg, **kwargs):
#         robbo = Robo()
#         return render(request, 'calculate/calc.html', {'robot': robbo})
#
#     def post(self, request, *arg, **kwargs):
#         form = Robo(request.POST)
#         if form.is_valid():
#             form.save()
#             num1 = int(request.POST.get('value1'))
#             num2 = int(request.POST.get('value2'))
#             print(num1)
#             print(num2)
#             ans = []
#
#             if request.POST.get('Manual'):
#                 c = round(math.sqrt(math.pow(num1, 2) + math.pow(num2, 2)), 1)
#                 ans.append(c)
#
#             elif request.POST.get('Automatic'):
#                 ans1 = ([x for x in range(0, 20, 1)])  # X
#                 ans2 = ([(randint(1, 2) * y) for y in range(0, 20, 1)])  # Y
#                 ans3 = np.concatenate([ans1, ans2])
#                 ans = f'X: {ans3[ans1]} Y: {ans3[ans2]}'
#
#             elif request.POST.get('Error'):
#                 ans = f'The robot has broken down, you need to get it serviced!'
#
#             elif request.POST.get('Idle'):
#                 ans = f'The robot is waiting for a task'
#             return redirect('/')
#         else:
#             print(form.errors)
#         return render(request, 'calculate/calc.html', {"answer": ans})
