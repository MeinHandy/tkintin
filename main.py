from tkinter import *
from tkinter import ttk
import random as ran
import time

# variables to store the account balance
enemy_stats = []
player_inventory = ["old sock"]
player_balance = 0
player_stats = {"Level": 1, "Health": 20, "Damage": 5}
wares = {"short sword": 20, "mace": 20, "broadsword": 30, "the throngler": 45, "Health potion": 10}
consumable_items = ["Health potion", "old sock", "moist old sock", "soggy old sock", "damp old sock", "wet old sock"]

# list of what can be consumed shop items can be added freely, dictionary allows for unique prices


# all the function
def menu():
    clear_bottom_frame()
    clear_combat_frame()
    consumed_label.grid_forget()
    balance_label.grid(row=3, column=0)  # row, column subject to change
    balance_display.grid(row=3, column=1)
    inventory_box.grid(row=1, column=0)
    start_combat.grid()



def clear_bottom_frame():
    for widget in action_frame.winfo_children():
        widget.grid_forget()


def clear_combat_frame():
    for widget in combat_frame.winfo_children():
        widget.grid_forget()


def init_combat():  # called on button press for combat
    global player_balance, balance_total
    clear_combat_frame()
    enemy_label.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
    attack_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def fought():  # for after combat
    global player_balance, balance_total
    clear_bottom_frame()
    player_stats["Health"] -= 5
    update_stats()  # player loses health, will be accurate damage at some point maybe
    if player_stats["Health"] > 0:
        player_balance += 5  # money gained post combat, temporary probably
        balance_total.set(player_balance)  # sets the DoubleVar to balance to update GUI
        combat_over.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        menu_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    else:  # if player low health they die
        clear_combat_frame()
        death_label.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
        respawn_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)  # shows respawn button


def respawn():  # resets stats after respawn button is pressed
    global player_inventory, player_stats, player_balance
    player_inventory = ["old sock"]  # resets inventory
    player_balance = 0  # resets money
    player_stats = {"Level": 1, "Health": 20, "Damage": 5}  # resets stats
    update_stats()  # updates reset stats
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
    if player_balance >= wares[shop_item.get()]:
        player_balance -= wares[shop_item.get()]
        balance_total.set(player_balance)
        bought_item_string.set(shop_item.get() + " bought")
        bought_item.grid(row=1, column=1)
        get_item()
    else:
        bought_item_string.set("Insufficient funds")
        bought_item.grid(row=1, column=1)


def get_item():
    global player_inventory
    player_inventory.append(shop_item.get())
    inventory_box['values'] = player_inventory


def use_item():  # consume item logic
    global player_inventory, consumable_items, player_stats
    if inventory_box.get() in consumable_items:  # checks if item is consumable
        if inventory_box.get() == "Health potion":  # checks if item is Health potion is true does health potion things
            player_stats["Health"] += 15
            update_stats()
        elif inventory_box.get() == "old sock":
            player_inventory.append("moist old sock")
            inventory_box['values'] = player_inventory
        elif inventory_box.get() == "moist old sock":
            player_inventory.append("damp old sock")
            inventory_box['values'] = player_inventory
        elif inventory_box.get() == "damp old sock":
            player_inventory.append("soggy old sock")
            inventory_box['values'] = player_inventory
        elif inventory_box.get() == "soggy old sock":
            player_inventory.append("wet old sock")
            inventory_box['values'] = player_inventory
        elif inventory_box.get() == "wet old sock":
            player_inventory.append("drenched old sock")
            inventory_box['values'] = player_inventory

        consumed_text.set(inventory_box.get() + " consumed.")
        consumed_label.grid()
        if inventory_box.get() != "drenched old sock":
            player_inventory.remove(inventory_box.get())  # removes it from the inventory
        inventory_box['values'] = player_inventory  # updates the inventory combobox
        inventory_display.set(player_inventory[0])  # changes back to item 0, so it no longer displays the item
    else:
        consumed_text.set(inventory_box.get() + " is not consumable.")
        consumed_label.grid()


def quit_game():
    quit("quit button")


def update_stats():
    global player_stats
    player_info.set("{} {} \n{} {} \n{} {}".format(list(player_stats)[0], player_stats['Level'],
                                                   list(player_stats)[1], player_stats['Health'],
                                                   list(player_stats)[2], player_stats['Damage']))


# tkinter init
root = Tk()
root.title("Sock Simulator 2023")
# menu widgets
player_frame = ttk.LabelFrame(root, text="Player")
player_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
player_info = StringVar()
update_stats()
details_label = ttk.Label(player_frame, textvariable=player_info)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

action_frame = ttk.LabelFrame(root)
action_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# action_label = ttk.Label(action_frame, text="Action:")
# action_label.grid(row=4, column=0)

action_list = ["Fight", "Sleep", "Shop"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# combat var ect
combat_frame = ttk.LabelFrame(root)
combat_frame.grid(row=1, column=1, sticky="NSEW", padx=10, pady=10)
start_combat = ttk.Button(combat_frame, text="Fight", command=init_combat)
start_combat.grid()
enemy = StringVar()
enemy.set("Boneman")
enemy_label = ttk.Label(combat_frame, textvariable=enemy)
post_combat = StringVar()
post_combat.set("Battle ended.")
combat_over = ttk.Label(combat_frame, textvariable=post_combat)
# death during combat
death_label = ttk.Label(combat_frame, text="You have perished.")
respawn_button = ttk.Button(combat_frame, text="Respawn", command=respawn)
# combat button
attack_enemy = ttk.Button(root, text="Attack Enemy!")

# rest var ect
resting = StringVar()
resting.set("You feel rested.")
rest_label = ttk.Label(action_frame, textvariable=resting)

# submit send to intersection function
attack_button = ttk.Button(combat_frame, text="Attack", command=fought)
# general menu button
menu_button = ttk.Button(combat_frame, text="Return", command=menu)

# shop
shop_item = StringVar()
shop_item.set("Health potion")
shop_combobox = ttk.Combobox(action_frame, textvariable=shop_item, state="readonly")
shop_combobox['values'] = list(wares)
purchase_button = ttk.Button(action_frame, text="Buy", command=purchase_item)
bought_item_string = StringVar()
bought_item_string.set("funny secret message")
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
# use item button
use_button = ttk.Button(inventory_frame, text="Use", command=use_item)
use_button.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")
consumed_text = StringVar()
consumed_text.set("placeholder consumable")
consumed_label = ttk.Label(inventory_frame, textvariable=consumed_text)

quit_button = ttk.Button(root, text="Quit game", command=quit_game)
quit_button.grid(row=3, column=2)

# Run the mainloop and starts menu
menu()
root.mainloop()
