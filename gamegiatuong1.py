stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
  item_total = 0
  print("Inventory:")
  for k, v in inventory.items():
    print(v,k)
    item_total = item_total+v

  print("Total number of items: " + str(item_total))
displayInventory(stuff)