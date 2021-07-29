from requests.sessions import Session
import streamlit as st
from PIL import Image
import random

from streamlit.proto.Checkbox_pb2 import Checkbox
from streamlit.proto.Progress_pb2 import Progress
import time



st.header('THE SITE WITH MANY OPTION')
st.error('Select An Option')

#ROCK PAPER SCISSORS ------------------------------------------------------------------------------
# ... rules ...

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
# ... rules ....
# add many option to the game
RockPaperScissors,BmiCalculator,encryptWord = st.beta_columns(3)
PasswordGen,TipCal = st.beta_columns([1,2])
Weather,LoveCal,quizApp= st.beta_columns(3)

# quiz app

if quizApp.checkbox('Quiz Me'):
    st.cache()
    def main():


        from data import data
    
        
        
        

        if 'point' not in st.session_state:
            st.session_state.point = 0
            st.session_state.my_score = 0

        
        question_1 = random.choice(data)
        # que 2
        question_2 = random.choice(data)

        # compared things
        st.info('Who Has More Searches')
        st.subheader(f"A: { question_1['name']}, a {question_1['description']} in {question_1['country']}")
        st.header('vs')
        st.subheader(f"B: { question_2['name']}, a {question_2['description']} in {question_2['country']}")
        


         # assign values for comparison
        a = question_1['follower_count']
        b = question_2['follower_count']
    

       

        entry = st.text_input('type A or B and check answer').lower()

        st.cache()
        def increment(entry):


            if entry == 'a':
                if a > b:
                    st.session_state.point +=1
                else:
                    st.session_state.my_score +=1
                    
            
            if entry == 'b':
                if b > a:
                    st.session_state.point +=1
                else:
                    st.session_state.my_score +=1
               


                        







            
        check = st.button('Check Answer', on_click=increment,
            args=(entry, ))
        st.write('my point = ', st.session_state.point)
        st.write('computer = ', st.session_state.my_score)
    if __name__=='__main__':
        main()



  


# encrypt word
if encryptWord.checkbox('Word Encrypted'):
    st.info('Encrypt Your MESSAGE')
    st.cache()
    def main():
        from data import alphabet

        word = st.text_area('Enter the words')
        direction = st.slider('Encode or Decode Number')

       

        action= st.radio("Choose an action",("Encode","Decode"))
        

        send = st.button('Submit')
        new_word = ''
        words = {}

        if word and action and send and direction:
            if action == 'Encode':

                for i in word:
                    if i in alphabet:
                        position = alphabet.index(i)+direction
                        new_pos = alphabet[position]
                        new_word += new_pos
                st.write(f'{new_word}')
                
                
               
            else:

                for i in word:
                    if i in alphabet:
                        position = alphabet.index(i)-direction
                        new_pos = alphabet[position]
                        new_word += new_pos
                st.write(f'{new_word}')
                

            





    if __name__ == '__main__':
            main()
        


#     # ------


    
















if RockPaperScissors.checkbox('RockPaperScissor'):

    st.title('ROCK PAPER SCISSORS')

    

    

    # load up the images
    rock,paper,scissors = st.beta_columns([1,2,3])
    rock = Image.open('rock.png')
    paper = Image.open('paper.png')
    scissors = Image.open('scissors.png')

    # store the list for computer
    opt = ['scissors','paper', 'rock']



    # your selection
    your_select = ['none','scissors','paper', 'rock']

    # random choice from pc
    computer_choice = random.choice(opt)
    

    # getting your selection
    my_guess = st.radio('Select to play', your_select)

    # now we play the game logic

    if my_guess == 'none': #to display nothing
        pass

        st.warning('You have to select option to start play')
      


    elif my_guess == computer_choice:
        st.warning(f"🤡🤡🤡 Damn its a DRAW!!! 🤡")
        
       
        
        if (computer_choice == 'rock') and ( my_guess=='rock'):
            st.image([rock,rock],width=200, caption=['Computer', 'Your Guess'])
          
        elif computer_choice == 'paper' and ( my_guess=='paper'):
            st.image([paper,paper],width=200, caption=['Computer', 'Your Guess'])
            
        elif computer_choice == 'scissors' and ( my_guess=='scissors'):
            st.image([scissors,scissors],width=200, caption=['Computer', 'Your Guess'])
           

    elif my_guess == 'rock' and computer_choice == 'scissors':
        st.success(f"Congrats!  WON the game! 🎈 🏆🏆🏆Winner🏆🏆🏆")
        st.image([scissors,rock],width=200, caption=['Computer', 'Your Guess'])
        st.balloons()
        

    elif my_guess == 'scissors' and computer_choice == 'paper':
        st.success(f"Congrats!  WON the game! 🎈 🏆🏆🏆Winner🏆🏆🏆")
        st.image([paper,scissors],width=200, caption=['Computer', 'Your Guess'])
        st.balloons()
     

    elif my_guess == 'paper' and computer_choice == 'rock':
        st.success(f"Congrats!  WON the game! 🎈 🏆🏆🏆Winner🏆🏆🏆")
        st.image([rock, paper],width=200, caption=['Computer', 'Your Guess'])
        st.balloons()
    


# display what comput generated
    else:
        st.error(f' ☠️ ☠️ you lose, computer choice was ☠️ ☠️ ☠️')
        
       
        
        # to show failed option
        if computer_choice == 'paper' and my_guess == 'scissors':
            st.image([paper,scissors],width=200, caption=['Computer', 'Your Guess'])
        elif computer_choice == 'paper' and my_guess == 'rock':
            st.image([paper,rock],width=200, caption=['Computer', 'Your Guess'])
        elif computer_choice == 'paper' and my_guess == 'paper':
            st.image([paper,paper],width=200, caption=['Computer', 'Your Guess'])

        # option 2

        elif computer_choice == 'rock' and my_guess == 'scissors':
            st.image([rock,scissors],width=200, caption=['Computer', 'Your Guess'])
        elif computer_choice == 'rock' and my_guess == 'rock':
            st.image([rock,rock],width=200, caption=['Computer', 'Your Guess'])
        elif computer_choice == 'rock' and my_guess == 'paper':
            st.image([rock,paper],width=200, caption=['Computer', 'Your Guess'])


        # option 3
        elif computer_choice == 'scissors' and my_guess == 'scissors':
            st.image([scissors,scissors],width=200, caption=['Computer', 'Your Guess'])
        elif computer_choice == 'scissors' and my_guess == 'rock':
            st.image([scissors,rock],width=200, caption=['Computer', 'Your Guess'])
        elif computer_choice == 'scissors' and my_guess == 'paper':
            st.image([scissors,paper],width=200, caption=['Computer', 'Your Guess'])


        


    #BMI Calculator ------------------------------------------------------------------------------
if BmiCalculator.checkbox('BMI Calculator'):
    st.cache()
    def main():

        
        st.header('Amoeba BMI Calculator')

        
      

        
       
       
        # math
        weight = st.slider('enter your weight in KG', max_value=300)
        height,inches = st.beta_columns(2)
        feet = height.number_input('height in ft', min_value=0)
        inches = inches.number_input('inches', min_value=0)
        st.write('Your Details')
        st.write(f'{feet} ft - {inches} inch - {weight} KG')
       
        

        # feet to meters
        if feet == 0 and inches == 0:
            st.warning('enter your details to check your BMI')
        else:

            newHeight = feet * 0.3049
            newInches = inches * 0.0254

            newHeightMeters = newHeight + newInches
            bmi = weight / newHeightMeters**2

            


            if bmi < 18.5:
                st.subheader(f'Your bmi is {"{:.2f}".format(bmi)}')
                st.warning('YOUR BMI IS UNDER WEIGHT CLASS')
            elif (bmi > 18.5) and (bmi < 25):
                st.subheader(f'Your bmi is {"{:.2f}".format(bmi)}')
                st.success('YOUR BMI IS NORMAL WEIGHT CLASS')
            elif (bmi > 25) and (bmi < 30):
                st.subheader(f'Your bmi is {"{:.2f}".format(bmi)}')
                st.warning('YOUR BMI IS OVER WEIGHT CLASS')
            elif (bmi > 30) and (bmi < 35):
                st.subheader(f'Your bmi is {"{:.2f}".format(bmi)}')
                st.error('YOUR BMI IS OBESE WEIGHT CLASS')
            else:
                st.subheader(f'Your bmi is {"{:.2f}".format(bmi)}')
                st.error('YOUR BMI IS CLINICALLY OBESE WEIGHT CLASS')

        
    if __name__ == '__main__':

        main()

    


    #Password Generator------------------------------------------------------------------------------
if TipCal.checkbox('TipCalculator'):
    st.cache()
    def main():
        st.header('Tip Calculator')
        st.info('Read The Instructions')
        import random

        # initialize the variables
        bill = st.number_input('Bill Price')
        tip = st.number_input('Tip Percentage (%)', min_value=0)
        people = st.number_input('How many people to split the bill', min_value=1)

        if st.checkbox('Select To Choose Who Pays The Bill?'):
            names = st.text_input('Enter the names of your friends')
            play = names.split(',')
            who = random.choice(play)
            st.subheader(f'The computer chose 🤗{who}🤗 to pay the bill')





        # Maths
        if bill == 0 and tip == 0 and people == 0:
            st.warning('Fill the info')
            pass
        else:

            tip_as_percent = tip / 100
            total_tip_amount = bill * tip_as_percent
            total_bill = bill + total_tip_amount
            bill_per_person = total_bill / people
            finale = "Bill Per Person: {:.2f}".format(bill_per_person)
            st.header(finale)
    if __name__ == '__main__':
        main() 


#love calculator------------------------------------------------------------------------------
if LoveCal.checkbox('LoveCalculator'):
    st.cache()
    def main():

        love = Image.open('lovecal.png')
        couple = Image.open('couples.png')
        st.image(love, width=300)
        st.header('LOVE CALCULATOR')
        st.markdown('The Love Calculator provides a score from 0% to 100% that is meant to be an indication of a match in terms of love, based on the names of two people. The higher the percentage, the better the match.')
        st.info('🤗🤗 MIND YOU, IT IS JUST FOR FUN 🤗🤗')
        name_1,name_2 = st.beta_columns(2)
        name_1 = name_1.text_input('Enter your name')
        name_2 = name_2.text_input("Enter your lover's name")

        # the logic
        
        both = (name_1 + name_2)

        for i in 'truelove':
            here = both.count(i)
            print(here)
            
        t = both.count('t')
        r = both.count('r')
        u = both.count('u')
        e = both.count('e')

        true = (t+r+u+e)
        # 
        l = both.count('l')
        o = both.count('o')
        v = both.count('v')
        e = both.count('e')
        love = (l+o+v+e)

        love_score = str(love) + str(love)
        original = int(love_score)

        if original < 10 or original > 90:
            st.subheader(f"Your love score is {love_score}, you go together like coke and mentos.")
            if original < 10:
                pass
            else:
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.5)
                    progress.progress(i+1)
                st.image(couple, width=300)
        elif original >= 40 and original <= 50:
            progress = st.progress(0)
            for i in range(50):
                time.sleep(0.5)
                progress.progress(i+1)
            st.subheader(f"Your love score is {love_score}, you are alright together.")
        else:
            
            st.subheader(f"Your love score is {love_score}, 😋😋😋")

       


    if __name__ == '__main__':
        main()
    

#Password Generator------------------------------------------------------------------------------ 
if PasswordGen.checkbox('PasswordGenerator'):
    st.cache()
    def main():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        import random

        st.header('Random Password Generator')
        st.write('Strong Password Generator to generate secure passwords from characters, numbers special symbols, and more. Random password generator to create passwords for any kind of login or other uses.')


        #get the values
        nr_letters,nr_symbols,nr_numbers = st.beta_columns(3)
        nr_letters= nr_letters.number_input('How many alphabets',min_value=0)
        nr_symbols = nr_symbols.number_input('How many symbols', min_value=0)
        nr_numbers = nr_numbers.number_input('How many numbers', min_value=0)
         
        
        # to get letters
        password = ''
        for py in range(1,nr_letters+1):
            randpy = random.choice(letters)
            password = randpy + password
    

        # to get numbers
        numb =''
        for nu in range(1,nr_numbers+1):
            li = random.choice(numbers)
            numb = numb + li

        # to get characters
        xter =''
        for nu in range(1,nr_symbols+1):
            lx = random.choice(symbols)
            xter = xter + lx
       
    #    add all the generated values
        yourpas = xter+numb+password
        

    #    to randomize the password
        str_var = list(yourpas)
        random.shuffle(str_var)

    # SHOW THE PASSWORD
        paz = ''.join(str_var)
        st.header('Your Generated Password')
        st.warning(paz)

        
    if __name__ == '__main__':
        main()
    

    # weather application
if Weather.checkbox('WeatherSearch'):
    def main():
        st.warning('The Weather Application')

        import requests, json

# API base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

        # City Name
        CITY = st.text_input('What is the name of the city')
        if CITY == '':
            pass

        else:


            # Your API key
            API_KEY = "494e02d29c6be05ea895dd671982ef04"

            # updating the URL
            URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

            # Sending HTTP request
            response = requests.get(URL)

            if response.status_code != '404':
                
            # retrieving data in the json format
                data = response.json()
                
                # take the main dict block
                main = data['main']
                
                # getting temperature
                temperature = main['temp']
                # getting feel like
                temp_feel_like = main['feels_like']  
                # getting the humidity
                humidity = main['humidity']
                # getting the pressure
                pressure = main['pressure']
                
                # weather report
                weather_report = data['weather']
                # wind report
                wind_report = data['wind']
                
                st.info(f"{CITY:-^35}")
                st.write(f"City ID: {data['id']}")   
                st.write(f"Temperature: {temperature}")
                st.write(f"Feel Like: {temp_feel_like}")    
                st.write(f"Humidity: {humidity}")
                st.write(f"Pressure: {pressure}")
                st.write(f"Weather Report: {weather_report[0]['description']}")
                st.write(f"Wind Speed: {wind_report['speed']}")
                st.write(f"Time Zone: {data['timezone']}")
            else:
            # showing the error message
                st.error("City Not Found")


               

    if __name__ == '__main__':
        main()


    




