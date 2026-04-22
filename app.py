import random
import time
#Golf incremental


types = [
    {'class': 'henry smith', 'multi': 1, 'cooldown': 1, 'accuracy': 1, 'desc': 'Average guy'},
    {'class': 'sharpshooter', 'multi': 1, 'cooldown': 1.2, 'accuracy': 1.1, 'desc': 'Pro: Increased accuracy   Con: Increased cooldown'},
    {'class': 'abuser', 'multi': 1, 'cooldown': 0.8, 'accuracy': 0.8, 'desc:': 'Pro: Decreased cooldown  Con: Decreased accuracy'},
    {'class': 'midas', 'muti': 1.25, 'cooldown': 1.1, 'accuracy': 0.925, 'desc': 'Pro: Increased mutli  Con: Increased cooldown and decreased accuracy'}
]

print("Class list:")
for type in types:
    print(type['class'].capitalize() + type['desc'])
# class_type = input("What class?")

# class type:
#     def __init__