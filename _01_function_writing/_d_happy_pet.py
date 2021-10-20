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
            while happiness>0 and happiness<100:
                print(activity)
                act=input('which activity?')
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
            while happiness>0 and happiness<100:
                print(activity)
                act=input('which activity?')
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
                    print('your cat did appreciate that')
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
        def interactions(self,frog):
            global happiness
            while happiness>0 and happiness<100:
                print(activity)
                act=input('which activity?')
                if act=='walk':
                    happiness+=frog['walk']
                    print('your frog does not appreciate your incompetence')
                    print(happiness)
                elif act=='feed':
                    happiness+=frog['feed']
                    print('good job! you fed your frog')
                    print(happiness)
                elif act=='give drink':
                    happiness+=frog['give drink']
                    print('noice')
                    print(happiness)
                elif act=='play':
                    happiness+=frog['play']
                    print('yay! your frog loves you more!')
                    print(happiness)
                elif act=='pet':
                    happiness+=frog['pet']
                    print('your frog is now dead from the oils on your skin')
                    print(happiness)
                    break
                elif act=='bathe':
                    happiness+=frog['bathe']
                    print('your frog loves you so much!')
                    print(happiness)
                elif act=='speak to it in it\'s language':
                    happiness+=frog['speak to it in it\'s language']
                    print('your frog doesn\'t understand a word you said and now despies you for your pronunciation and horribble grammar (it loves you anyway)')
                    print(happiness)
                else:
                    print('you lose, follow the directions dimwit')
            if happiness<0:
                print('you can\'t even keep a frog alive (you lost)')
            else:
                print('good job! your frog has reached maximum happiness (you won)')
    
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
        def interactions(self,dog):
            global happiness
            while happiness>0 and happiness<100:
                print(activity)
                act=input('which activity?')
                if act=='walk':
                    happiness+=dog['walk']
                    print('uwu')
                    print(happiness)
                elif act=='feed':
                    happiness+=dog['feed']
                    print('good job! you fed your dog')
                    print(happiness)
                elif act=='give drink':
                    happiness+=dog['give drink']
                    print('noice')
                    print(happiness)
                elif act=='play':
                    happiness+=dog['play']
                    print('yay! your dog loves you more!')
                    print(happiness)
                elif act=='pet':
                    happiness+=dog['pet']
                    print('uwu')
                    print(happiness)
                    break
                elif act=='bathe':
                    happiness+=dog['bathe']
                    print('your dog loves you so much!')
                    print(happiness)
                elif act=='speak to it in it\'s language':
                    happiness+=dog['speak to it in it\'s language']
                    print('your dog doesn\'t understand a word you said and now despies you for your pronunciation and horribble grammar (it loves you anyway)')
                    print(happiness)
                else:
                    print('you lose, follow the directions dimwit')
            if happiness<0:
                print('you can\'t even keep a dog alive (you lost)')
            else:
                print('good job! your gog has reached maximum happiness (you won)')


if __name__ == '__main__':
    pets=['fish','cat','frog','dog']
    goal=100
    activity=['walk','feed','give drink','play','pet','bathe','speak to it in it\'s language']
    
    def which():
        print(pets)
        pet=input('which pet do you want?(out of the options above)')
        print('you now have a',pet)
        return pet
    pet=which()
    if pet=='fish':
        print(interactfish.interactions(interactfish,interactfish.fish,activity))
    elif pet=='cat':
        print(interactcat.interactions(interactcat,interactcat.cat))
    elif pet=='frog':
        print(interactfrog.interactions(interactfrog,interactfrog.frog))
    elif pet=='dog':
        print(interactdog.interactions(interactdog,interactdog.dog))
    
    



