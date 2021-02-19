
def displayInventory(inventory):
  item_total = 0
  print(inventory)
  for k, v in inventory.items():
    print(v,k)
    item_total = item_total+v
  print("Total number of items: " + str(item_total))
def addToInventory(inventory, addedItems):
  for items in addedItems:
    inventory.setdefault(items,0)
    inventory[items] = inventory[items]+1
  return inventory
inv = {'gold coin': 42, 'wire ': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin' , 'ruby']
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)
