import csv
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.
import copy

def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for k,v in inventory.items():
        print(f'{k}: {v}') 

def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    unique_list = []
    
    for items in added_items:
        if items not in unique_list:
            unique_list.append(items)  
    for items in unique_list:
        if items not in inventory.keys():
            inventory[items] = 0
        inventory[items] += added_items.count(items)     
    return inventory

def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    unique_list = []
    
    for items in removed_items:
        if items not in unique_list:
            unique_list.append(items)
    for items in unique_list:
        inventory[items] -= removed_items.count(items)
        if inventory[items] == 0:
            inventory.pop(items)    
    return inventory

def print_table(inventory, order=None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    print('-----------------')
    print(f"{'item name | count' : >10}")
    print('-----------------')
    if order == None:
        for k,v in inventory.items():
            print(f"{k: >9} | {v : >5}")
    else:
        values = []
        keys = []
        for v in inventory.values():
            values.append(v)
        values.sort()

        for i in range(len(values)):
            keys.append(list(inventory.keys())[list(inventory.values()).index(values[i])])
            
        if 'asc' in order:
            for i in range(len(values)):
                print(f"{keys[0]: >9} | {values[0] : >5}")
                values.pop(0)
                keys.pop(0)

        elif 'desc' in order:
            for i in range(len(values)):
                print(f"{keys[-1]: >9} | {values[-1] : >5}")
                values.pop(-1)
                keys.pop(-1)
    print('-----------------')

def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    try:
        with open(filename,'r',newline='') as f:
            csvreader = csv.reader(f, delimiter=',')
            for line in csvreader:
                add_to_inventory(inventory,line)
            return inventory
        
    except FileNotFoundError:
        print("File 'no_such_file.csv' not found!")

def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""
    try:
        with open(filename,'r+', newline='') as f:
            csvwriter = csv.writer(f, delimiter=',')
            add_to_file_list = []
            for k,v in inventory.items():
                if inventory.get(k) > 1:
                    for i in range(inventory.get(k)-1):
                        add_to_file_list.append(k)
                add_to_file_list.append(k)
            print(add_to_file_list)
            csvwriter.writerow(add_to_file_list)
    except FileNotFoundError:
        print("You don't have permission creating file '/nopermission.csv'!")
        

inventory = {'rope': 1, 'torch': 6}

print_table(inventory)


