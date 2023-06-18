import string as s
import secrets as ss
import tkinter as tk

#KEY GENERATOR
#alphabet = string.ascii_letters + string.digits
#password = ''.join(secrets.choice(alphabet) for i in range(16))

#APP 'MALDITA LLAVE'
    
window=tk.Tk()
window.config(bg='#000000')


#GLOBAL VARIABLES
title_var= 'Maldita Llave'
#dictionary: [0]characters, [1]selected characters
characters_dict= {'numbers': [s.digits,tk.IntVar()], 
                'lowercases': [s.ascii_lowercase,tk.IntVar()], 
                'UPPERCASES': [s.ascii_uppercase,tk.IntVar()],
                'symbols': [s.punctuation,tk.IntVar()], 
                'whitespaces': [s.whitespace,tk.IntVar()]}
#dictionary where your keys will be safe
keyBook= {}#'platform':{'user': 'key'}
#here you save the inputs text
platform_entry_var= tk.StringVar()
user_entry_var= tk.StringVar()

#FUNCTIONS
#key generator
def key_generator():
        alphabet=''
        for character in characters_dict:
            if characters_dict[character][1].get() == 1:
                   alphabet +=characters_dict[character][0]
        platform= platform_entry_var.get()
        user= user_entry_var.get()
        random_password =''.join(ss.choice(alphabet) for i in range(16))
        keyBook[platform]= {user: random_password}
        new_password = tk.Label(window, text='+ Hi ' + user + ', your new secure password for '+ platform + ' is: ' + random_password)
        new_password.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
        new_password.pack()
        platform_entry.delete(0,len(platform_entry_var.get()))
        user_entry.delete(0,len(user_entry_var.get()))
        for character in characters_dict:
            characters_dict[character][1].set(0)

title = tk.Label(window, text=title_var)
title.config(bg='#000000', fg='#00ff00', font=('Comic Sans MS',28,'bold'))
title.pack()

platform = tk.Label(window, text='Platform: ')
platform.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
platform.pack()

platform_entry = tk.Entry(window, textvariable=platform_entry_var)
platform_entry.config()
platform_entry.pack()

user = tk.Label(window, text='Username: ')
user.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
user.pack()

user_entry = tk.Entry(window, textvariable=user_entry_var)
user_entry.config()
user_entry.pack()
for character in characters_dict:
        checkbox= tk.Checkbutton(window,text=character, variable=characters_dict[character][1])
        checkbox.config()
        checkbox.pack()

key_generator_button = tk.Button(window, text='Take a Key', command=key_generator)
key_generator_button.config()
key_generator_button.pack()

#LOOP
window.mainloop()


#TESTING ZONE
# print(keyBook)