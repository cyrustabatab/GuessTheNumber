import tkinter,random

def generate_random_number(start=1,high=100):

    return random.randint(start,high)

def play_game_again():
    global number_to_guess,guesses_left,is_game_over
    number_to_guess = generate_random_number()
    guesses_left = 7
    guesses_left_label['text']= f"{guesses_left} guesses left"
    info_label['text'] = ''
    info_label_2['text'] = ''
    play_again.pack_forget()
    is_game_over = False




def check_guess():
    global incorrect_input,guesses_left,is_game_over
    if is_game_over:
        return
    try:
        guess = int(entry.get())
    except:
        info_label['foreground'] = 'black'
        info_label['text'] = "Please enter a number"
        info_label_2['text'] = ''
    else:
        if guess ==  number_to_guess:
            info_label['text'] = 'CORRECT'
            guesses_left_label['text'] = ''
            info_label['foreground'] = 'green'
            info_label_2['text'] = ''
            is_game_over = True
            play_again.pack()
        else:
            info_label['text'] = 'INCORRECT'
            guesses_left -= 1
            if guesses_left == 0:
                is_game_over = True
                info_label['text'] = 'Out of Guesses'
                info_label_2['text'] = f'The number was {number_to_guess}'
                guesses_left_label['text'] = ''
                play_again.pack()
            else:
                guesses_left_label['text'] = f"{guesses_left} guesses left"
                if guess < number_to_guess:
                    info_label_2['text'] = 'TOO LOW'
                else:
                    info_label_2['text'] = 'TOO HIGH'

    finally:
        entry.delete(0,tkinter.END)
        




      



font=("Arial",24,"bold")
window = tkinter.Tk()
window.title("Guess The Number")
window.minsize(width=700,height=500)

number_to_guess = generate_random_number()
guesses_left = 7
is_game_over = False

label = tkinter.Label(text="GUESS THE NUMBER!",font=font)
label.pack(pady=20)



entry = tkinter.Entry(width=30,justify='center',font=font)
entry.focus_set()
entry.pack(pady=20,ipady=10)


button = tkinter.Button(text="Guess",font=font,command=check_guess)
button.pack()


guesses_left_label = tkinter.Label(text="7 Guesses Left",foreground='blue',font=font)
guesses_left_label.pack(pady=10)


info_label= tkinter.Label(text='',font=font,foreground='red')
info_label.pack(pady=10)

info_label_2 = tkinter.Label(text='',font=font,foreground='red')
info_label_2.pack(pady=10)

play_again = tkinter.Button(text="Play Again",font=font,command=play_game_again)
play_again.pack(pady=10)
play_again.pack_forget()








window.mainloop()


