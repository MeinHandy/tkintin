from tkinter import *
from tkinter import ttk

# Create a variable to store the account balance
savings_balance = 0
phone_balance = 0
holiday_balance = 0
enemy_stats = []
player_inventory = []
player_balance = 0
player_stats = {"Level": 1, "Health": 20, "Damage": 5}
# aaa

def menu():
    clear_bottom_frame()
    action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")
    submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def clear_bottom_frame():
    for widget in bottom_frame.winfo_children():
        widget.grid_forget()


def combat():  # called on button press for combat
    clear_bottom_frame()
    enemy_label.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
    attack_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def fought():  # for after combat
    global player_balance
    clear_bottom_frame()
    player_balance += 2
    combat_over.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    menu_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def sleep():  # called on button press
    clear_bottom_frame()
    rest_label.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    menu_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def shop():  # called on button press
    clear_bottom_frame()
    shop_combobox.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    menu_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    purchase_button.grid(row=6, column=2, columnspan=2, padx=10, pady=10)


def purchase_item():
    global player_balance, player_inventory
    if player_balance >= 10:
        player_balance -= 10
        print("{} bought".format(shop_item.get()))
        player_inventory.append(shop_item)
    else:
        print("Insufficient funds")


# runs function for each choice when chosen
def intersection():
    choice = chosen_action.get()
    if choice == "Fight":
        combat()
    elif choice == "Sleep":
        sleep()
    elif choice == "Shop":
        shop()
    else:
        print("drug deal")


# tkinter init
root = Tk()
root.title("Shit game")
# menu widgets
top_frame = ttk.LabelFrame(root, text="Player")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

player_info = StringVar()
player_info.set(player_stats)

details_label = ttk.Label(top_frame, textvariable=player_info)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

action_label = ttk.Label(bottom_frame, text="Action:")
action_label.grid(row=4, column=0)

action_list = ["Fight", "Sleep", "Shop"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list

# combat var ect
enemy = StringVar()
enemy.set("Boneman")
enemy_label = ttk.Label(bottom_frame, textvariable=enemy)
post_combat = StringVar()
post_combat.set("Battle ended.")
combat_over = ttk.Label(bottom_frame, textvariable=post_combat)

# rest var ect
resting = StringVar()
resting.set("You feel rested.")
rest_label = ttk.Label(bottom_frame, textvariable=resting)

# submit send to intersection function
attack_button = ttk.Button(bottom_frame, text="Attack", command=fought)
submit_button = ttk.Button(bottom_frame, text="Continue", command=intersection)
# general menu button
menu_button = ttk.Button(bottom_frame, text="Return", command=menu)

# shop
wares = ["short sword", "mace", "broadsword"]
shop_item = StringVar()
shop_item.set(wares[0])
shop_combobox = ttk.Combobox(bottom_frame, textvariable=shop_item, state="readonly")
shop_combobox['values'] = wares
purchase_button = ttk.Button(bottom_frame, text="Buy", command=lambda: purchase_item())

# Run the mainloop and starts menu
menu()
root.mainloop()
