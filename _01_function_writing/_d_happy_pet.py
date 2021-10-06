"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk

global happiness
happiness=10

class interactfish():
        fish={
        'walk':-happiness,
        'feed':30,
        'give drink': 0,
        'play':7,
        'pet': -2,
        'bathe':0,
        'speak to it in it\'s language': -10
        }

        def interactions(self,fish,activity):
            global happiness
            print(activity)
            act=input('which activity?')
            while happiness>0 or happiness==100:
                if act=='walk':
                    happiness+=fish['walk']
                    print('your fish is now dead due to your incompetence')
                    return happiness
                elif act=='feed':
                    happiness+=fish['feed']
                    print('good job! you fed your fish')
                    print(happiness)
                elif act=='give drink':
                    happiness+=fish['give drink']
                    print('wow, you really just gave a water to a creature surrounded by it.')
                    print(happiness)
                elif act=='play':
                    happiness+=fish['play']
                    print('not sure how you played with it but points for trying')
                    print(happiness)
                elif act=='pet':
                    happiness+=fish['pet']
                    print('your fish did not appreciate that')
                    print(happiness)
                elif act=='bathe':
                    happiness+=fish['bathe']
                    print('noice')
                    print(happiness)
                elif act=='speak to it in it\'s language':
                    happiness+=fish['speak to it in it\'s language']
                    print('your fish is disapointed in your pronounciation')
                    print(happiness)
                else:
                    print('you lose, follow the directions dimwit')
            if happiness==0:
                print('you can\'t even keep a fish alive (you lost)')
            else:
                print('good job! your fish has reached maximum happiness (you won)')

class interactcat():
        cat={
        'walk':-1,
        'feed':20,
        'give drink':10,
        'play':30,
        'pet':20,
        'bathe':-20,
        'speak to it in it\'s language': -40
        }

        def interactions(self,cat):
            global happiness
            print(activity)
            act=input('which activity?')
            while happiness>0 or happiness==100:
                if act=='walk':
                    happiness+=cat['walk']
                    print('your cat does not appreciate your incompetence')
                    print(happiness)
                elif act=='feed':
                    happiness+=cat['feed']
                    print('good job! you fed your cat')
                    print(happiness)
                elif act=='give drink':
                    happiness+=cat['give drink']
                    print('noice')
                    print(happiness)
                elif act=='play':
                    happiness+=cat['play']
                    print('yay! your cat loves you more!')
                    print(happiness)
                elif act=='pet':
                    happiness+=cat['pet']
                    print('your act did appreciate that')
                    print(happiness)
                elif act=='bathe':
                    happiness+=cat['bathe']
                    print('your cat is dying, it now hates you')
                    print(happiness)
                elif act=='speak to it in it\'s language':
                    happiness+=cat['speak to it in it\'s language']
                    print('your cat doesn\'t understand a word you said and now despies you for your pronunciation and horribble grammar')
                    print(happiness)
                else:
                    print('you lose, follow the directions dimwit')
            if happiness==0:
                print('you can\'t even keep a cat alive (you lost)')
            else:
                print('good job! your cat has reached maximum happiness (you won)')
    
class interactfrog():
        frog={
        'walk':5,
        'feed':30,
        'give drink':30,
        'play':3,
        'pet':-happiness,
        'bathe':50,
        'speak to it in it\'s language': -15
        }
    
class interactdog():
        dog={
        'walk':40,
        'feed':30,
        'give drink':20,
        'play':50,
        'pet':60,
        'bathe':3,
        'speak to it in it\'s language': 0
        }
        


if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pets=['fish','cat','frog','dog']
    
    goal=100
    activity=['walk','feed','give drink','play','pet','bathe','speak to it in it\'s language']
    
    def which():
        print(pets)
        pet=input('which pet do you want?(out of the options above)')
        print('you now have a',pet)
        return pet

    which()
    if which=='fish':
        print(interactfish.interactions(interactfish,interactfish.fish,activity))



