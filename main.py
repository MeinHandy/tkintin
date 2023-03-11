from tkinter import *
from tkinter import ttk

# variables to store the account balance
enemy_stats = []
player_inventory = ["old sock"]
player_balance = 0
player_stats = {"Level": 1, "Health": 20, "Damage": 5}
wares = ["short sword", "mace", "broadsword", "the throngler"]
# shop items can be added freely, dictionary for individual prices?


# all the function
def menu():
    clear_bottom_frame()
    action_box.grid(row=4, column=0, padx=10, pady=3, sticky="WE")
    submit_button.grid(row=5, column=0, padx=10, pady=10)
    balance_label.grid(row=3, column=0)  # row, column subject to change
    balance_display.grid(row=3, column=1)
    inventory_box.grid(row=1, column=0)



def clear_bottom_frame():
    for widget in action_frame.winfo_children():
        widget.grid_forget()


def combat():  # called on button press for combat
    global player_balance, balance_total
    clear_bottom_frame()
    enemy_label.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
    attack_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def fought():  # for after combat
    global player_balance, balance_total
    clear_bottom_frame()
    player_stats["Health"] -= 5
    player_info.set(player_stats)  # player loses health, will be actual damage at some point maybe
    if player_stats["Health"] > 0:
        player_balance += 5  # money gained post combat, temporary probably
        balance_total.set(player_balance)  # sets the DoubleVar to balance to update GUI
        combat_over.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        menu_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    else:  # if player low health they die
        death_label.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
        respawn_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)  # shows respawn button


def respawn():  # resets stats after respawn button is pressed
    global player_inventory, player_stats, player_balance
    player_inventory = ["old sock"]  # resets inventory
    player_balance = 0  # resets money
    player_stats = {"Level": 1, "Health": 20, "Damage": 5}  # resets stats
    player_info.set(player_stats)  # displays reset stats
    balance_total.set(player_balance)  # sets the DoubleVar to balance to update GUI
    inventory_box['values'] = player_inventory  # re-displays inventory so its empty
    inventory_display.set(player_inventory[0])  # makes the selected item the first, so it doesn't show old item
    menu()  # sends player to the menu


def sleep():  # called on button press
    clear_bottom_frame()
    rest_label.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    menu_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def shop():  # called on button press
    clear_bottom_frame()
    shop_combobox.grid(row=1, column=0, padx=10, pady=10)
    menu_button.grid(row=2, column=0, padx=10, pady=10)
    purchase_button.grid(row=2, column=1, padx=10, pady=10)


def purchase_item():
    global player_balance, player_inventory, balance_total, inventory_display
    if player_balance >= 10:
        player_balance -= 10
        balance_total.set(player_balance)
        bought_item_string.set(shop_item.get() + " bought")
        bought_item.grid(row=1, column=1)
        get_item()
    else:
        bought_item_string.set("Insufficient funds")
        bought_item.grid(row=1, column=1)


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
        print("the funny secret else statement you cannot achieve.. unless you can. pls report bug")


def get_item():
    global player_inventory
    player_inventory.append(shop_item.get())
    inventory_box['values'] = player_inventory


# tkinter init
root = Tk()
root.title("Shit game")
# menu widgets
player_frame = ttk.LabelFrame(root, text="Player")
player_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
player_info = StringVar()
player_info.set(player_stats)  # lol w/e

details_label = ttk.Label(player_frame, textvariable=player_info)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

action_frame = ttk.LabelFrame(root)
action_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# action_label = ttk.Label(action_frame, text="Action:")
# action_label.grid(row=4, column=0)

action_list = ["Fight", "Sleep", "Shop"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

action_box = ttk.Combobox(action_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list

# combat var ect
enemy = StringVar()
enemy.set("Boneman")
enemy_label = ttk.Label(action_frame, textvariable=enemy)
post_combat = StringVar()
post_combat.set("Battle ended.")
combat_over = ttk.Label(action_frame, textvariable=post_combat)
# death during combat
death_message = StringVar()
death_message.set("You have perished")
death_label = ttk.Label(action_frame, textvariable=death_message)
respawn_button = ttk.Button(action_frame, text="Respawn", command=respawn)

# rest var ect
resting = StringVar()
resting.set("You feel rested.")
rest_label = ttk.Label(action_frame, textvariable=resting)

# submit send to intersection function
attack_button = ttk.Button(action_frame, text="Attack", command=fought)
submit_button = ttk.Button(action_frame, text="Continue", command=intersection)
# general menu button
menu_button = ttk.Button(action_frame, text="Return", command=menu)

# shop
shop_item = StringVar()
shop_item.set(wares[0])
shop_combobox = ttk.Combobox(action_frame, textvariable=shop_item, state="readonly")
shop_combobox['values'] = wares
purchase_button = ttk.Button(action_frame, text="Buy", command=purchase_item)
bought_item_string = StringVar()
bought_item_string.set("placeholder")
bought_item = ttk.Label(action_frame, textvariable=bought_item_string)

# money update real time
balance_label = ttk.Label(player_frame, text="Money: ")
balance_total = DoubleVar()
balance_total.set(0)
balance_display = Label(player_frame, textvariable=balance_total)

# inventory, as combobox for now, may have other tab later, copied shop code, basically
inventory_frame = ttk.LabelFrame(root, text="Inventory")  # frame for the inventory, inventory will be expanded sometime
inventory_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")
inventory_display = StringVar()
inventory_display.set(player_inventory[0])
inventory_box = ttk.Combobox(inventory_frame, textvariable=inventory_display, state="readonly")
inventory_box['values'] = player_inventory


# Run the mainloop and starts menu
menu()
root.mainloop()
