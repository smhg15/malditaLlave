import string as s
import secrets as ss
import tkinter as tk

#KEY GENERATOR
#alphabet = string.ascii_letters + string.digits
#password = ''.join(secrets.choice(alphabet) for i in range(16))

#APP 'MALDITA LLAVE'
    
windows=tk.Tk()
windows.config(bg='#000000')


#GLOBAL VARIABLES
#admited characters
alphabet = s.ascii_letters + s.digits
#dictionary where your keys will be safe
keyBook = {'platform':{'user': 'key'}}
title_var= 'Maldita Llave'
platform_entry_var= tk.StringVar()
user_entry_var= tk.StringVar()

#FUNCTIONS
#key generator
def key_generator():
        platform= platform_entry_var.get()
        user= user_entry_var.get()
        random_password =''.join(ss.choice(alphabet) for i in range(16))
        keyBook[platform]= {user: random_password}
        new_password = tk.Label(windows, text='+ Hi ' + user + ', your new secure password for '+ platform + ' is: ' + random_password)
        new_password.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
        new_password.pack()
        print(keyBook)

title = tk.Label(windows, text=title_var)
title.config(bg='#000000', fg='#00ff00', font=('Comic Sans MS',28,'bold'))
title.pack()

platform = tk.Label(windows, text='Platform: ')
platform.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
platform.pack()

platform_entry = tk.Entry(windows, textvariable=platform_entry_var)
platform_entry.config()
platform_entry.pack()

user = tk.Label(windows, text='Username: ')
user.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
user.pack()

user_entry = tk.Entry(windows, textvariable=user_entry_var)
user_entry.config()
user_entry.pack()

key_generator_button = tk.Button(windows, text='Take a Key', command=key_generator)
key_generator_button.config()
key_generator_button.pack()

#LOOP
windows.mainloop()



#TESTING ZONE
# key_generator()
# print(keyBook)
# key_generator()
# print(keyBook)