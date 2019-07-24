import random

def Goodbye():
    samples = ['Goodbye :)',
               'Have a nice day!',
               'Have a wonderful day!',
               'Adios!',
               'Talk to you later!',
               'Take it easy! :)',
               'Until tomorrow! :)']
    i = random.randint(0, len(samples) - 1)
    return samples[i]
