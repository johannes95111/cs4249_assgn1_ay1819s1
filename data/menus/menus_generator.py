import pandas as pd
from random import shuffle
from random import seed


###### Menu Breadth 8 ######
level1 = ['Animal', 'Fruit', 'Clothing', 'Electronic',
          'Transportation', 'Furniture', 'Stationery', 'Instrument']
animal = ['Bird', 'Frog', 'Fish', 'Butterfly',
          'Cat', 'Spider', 'Snake', 'Dog']
fruit = ['Banana', 'Apple', 'Pear', 'Plum',
         'Papaya', 'Grape', 'Berry', 'Melon']
clothing = ['Socks', 'Jacket', 'Blouse', 'Jeans',
            'Belt', 'Hat', 'Gloves', 'Shirt']
electronic = ['Printer', 'Monitor', 'Phone', 'Speaker',
              'Tablet', 'Laptop', 'Camera', 'Headphones']
transportation = ['Train', 'Bus', 'Helicopter', 'Boat',
                  'Airplane', 'Van', 'Truck', 'Motorcycle']
furniture = ['Sofa', 'Bed', 'Chair', 'Shelf',
             'Bookcase', 'Table', 'Mattress', 'Stool']
stationery = ['Eraser', 'Pencil', 'Ruler', 'Highlighter',
              'Pen', 'Stapler', 'Envelope', 'Marker']
instrument = ['Piano', 'Accordion', 'Violin', 'Drum',
              'Flute', 'Saxophone', 'Trumpet', 'Guitar']
colour = ['Red', 'Yellow', 'Pink', 'Blue', 'Purple', 'Black', 'Green', 'White']

seed(11)
### Menu Breadth 8 Depth 3 ###
res = {'Id':[],
       'Parent':[],
       'Label':[]}
count_id = 1
count_parent = 0
# create level 1
for e in level1:
    res['Id'].append(count_id)
    count_id += 1
    res['Parent'].append(count_parent)
    res['Label'].append(e)
count_parent += 1

# create level 2
def create_level2(collection):
    global count_id, count_parent
    for e in collection:
        res['Id'].append(count_id)
        count_id += 1
        res['Parent'].append(count_parent)
        res['Label'].append(e)
    count_parent += 1
create_level2(animal)
create_level2(fruit)
create_level2(clothing)
create_level2(electronic)
create_level2(transportation)
create_level2(furniture)
create_level2(stationery)
create_level2(instrument)

# create level 3
def create_level3(collection, prefix):
    global count_id, count_parent
    for e in collection:
        temp = list()
        for c in prefix:
            res['Id'].append(count_id)
            count_id += 1
            res['Parent'].append(count_parent)
            temp.append(c + ' ' + e)
            shuffle(temp)
        count_parent += 1
        res['Label'].extend(temp)
create_level3(animal, colour)
create_level3(fruit, colour)
create_level3(clothing, colour)
create_level3(electronic, colour)
create_level3(transportation, colour)
create_level3(furniture, colour)
create_level3(stationery, colour)
create_level3(instrument, colour)

output = pd.DataFrame(res)
output = output[['Id', 'Parent', 'Label']]
output.to_csv('menu_depth_3_breadth_8.csv', encoding='utf-8', index=False)

###### Menu Breadth 4 ######
level1 = ['Animal', 'Fruit', 'Clothing', 'Transportation']
animal = ['Bird', 'Frog', 'Fish', 'Butterfly']
fruit = ['Banana', 'Apple', 'Pear', 'Plum']
clothing = ['Socks', 'Jacket', 'Blouse', 'Jeans']
transportation = ['Train', 'Bus', 'Van', 'Boat']
colour = ['Red', 'Yellow', 'Purple', 'Blue']

seed(11)
### Menu Breadth 4 Depth 3 ###
res = {'Id':[],
       'Parent':[],
       'Label':[]}
count_id = 1
count_parent = 0
# create level 1
for e in level1:
    res['Id'].append(count_id)
    count_id += 1
    res['Parent'].append(count_parent)
    res['Label'].append(e)
count_parent += 1

# create level 2
def create_level2(collection):
    global count_id, count_parent
    for e in collection:
        res['Id'].append(count_id)
        count_id += 1
        res['Parent'].append(count_parent)
        res['Label'].append(e)
    count_parent += 1
create_level2(animal)
create_level2(fruit)
create_level2(clothing)
create_level2(transportation)

# create level 3
def create_level3(collection, prefix):
    global count_id, count_parent
    for e in collection:
        temp = list()
        for c in prefix:
            res['Id'].append(count_id)
            count_id += 1
            res['Parent'].append(count_parent)
            temp.append(c + ' ' + e)
            shuffle(temp)
        count_parent += 1
        res['Label'].extend(temp)
create_level3(animal, colour)
create_level3(fruit, colour)
create_level3(clothing, colour)
create_level3(transportation, colour)

output = pd.DataFrame(res)
output = output[['Id', 'Parent', 'Label']]
output.to_csv('menu_depth_3_breadth_4.csv', encoding='utf-8', index=False)

