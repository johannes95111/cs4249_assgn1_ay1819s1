import pandas as pd
from sklearn.utils import shuffle

menu_type = ['Marking', 'Radial']
menu_depth = [1, 2, 3]
menu_breadth = [4, 8]
input_device = ['Mouse', 'Touchpad']

columns = ['Menu Type','Menu Depth','Menu Breadth',
           'Input Device','Target Item']
df = pd.DataFrame(columns=columns)

cond1 = pd.DataFrame([['Marking',1,4,'Mouse','Animal'],
                      ['Marking',1,4,'Mouse','Fruit'],
                      ['Marking',1,4,'Mouse','Transportation'],
                      ['Marking',2,4,'Mouse','Bird'],
                      ['Marking',2,4,'Mouse','Socks'],
                      ['Marking',2,4,'Mouse','Butterfly'],
                      ['Marking',3,4,'Mouse','Yellow Pear'],
                      ['Marking',3,4,'Mouse','Blue Jeans'],
                      ['Marking',3,4,'Mouse','Yellow Jacket']], columns=columns)

cond2 = pd.DataFrame([['Marking',1,8,'Mouse','Instrument'],
                      ['Marking',1,8,'Mouse','Furniture'],
                      ['Marking',1,8,'Mouse','Animal'],
                      ['Marking',2,8,'Mouse','Spider'],
                      ['Marking',2,8,'Mouse','Tablet'],
                      ['Marking',2,8,'Mouse','Papaya'],
                      ['Marking',3,8,'Mouse','White Cat'],
                      ['Marking',3,8,'Mouse','Pink Boat'],
                      ['Marking',3,8,'Mouse','Green Ruler']], columns=columns)

cond3 = pd.DataFrame([['Marking',1,4,'Touchpad','Clothing'],
                      ['Marking',1,4,'Touchpad','Transportation'],
                      ['Marking',1,4,'Touchpad','Fruit'],
                      ['Marking',2,4,'Touchpad','Plum'],
                      ['Marking',2,4,'Touchpad','Frog'],
                      ['Marking',2,4,'Touchpad','Train'],
                      ['Marking',3,4,'Touchpad','Purple Van'],
                      ['Marking',3,4,'Touchpad','Purple Fish'],
                      ['Marking',3,4,'Touchpad','Red Bird']], columns=columns)

cond4 = pd.DataFrame([['Marking',1,8,'Touchpad','Stationery'],
                      ['Marking',1,8,'Touchpad','Electronic'],
                      ['Marking',1,8,'Touchpad','Furniture'],
                      ['Marking',2,8,'Touchpad','Shirt'],
                      ['Marking',2,8,'Touchpad','Berry'],
                      ['Marking',2,8,'Touchpad','Highlighter'],
                      ['Marking',3,8,'Touchpad','Red Gloves'],
                      ['Marking',3,8,'Touchpad','Black Stool'],
                      ['Marking',3,8,'Touchpad','Blue Bookcase']], columns=columns)

cond5 = pd.DataFrame([['Radial',1,4,'Mouse','Clothing'],
                      ['Radial',1,4,'Mouse','Animal'],
                      ['Radial',1,4,'Mouse','Fruit'],
                      ['Radial',2,4,'Mouse','Boat'],
                      ['Radial',2,4,'Mouse','Banana'],
                      ['Radial',2,4,'Mouse','Fish'],
                      ['Radial',3,4,'Mouse','Red Banana'],
                      ['Radial',3,4,'Mouse','Yellow Train'],
                      ['Radial',3,4,'Mouse','Blue Frog']], columns=columns)

cond6 = pd.DataFrame([['Radial',1,8,'Mouse','Fruit'],
                      ['Radial',1,8,'Mouse','Instrument'],
                      ['Radial',1,8,'Mouse','Furniture'],
                      ['Radial',2,8,'Mouse','Printer'],
                      ['Radial',2,8,'Mouse','Sofa'],
                      ['Radial',2,8,'Mouse','Guitar'],
                      ['Radial',3,8,'Mouse','Yellow Bed'],
                      ['Radial',3,8,'Mouse','Purple Envelope'],
                      ['Radial',3,8,'Mouse','Black Violin']], columns=columns)

cond7 = pd.DataFrame([['Radial',1,4,'Touchpad','Clothing'],
                      ['Radial',1,4,'Touchpad','Animal'],
                      ['Radial',1,4,'Touchpad','Fruit'],
                      ['Radial',2,4,'Touchpad','Jacket'],
                      ['Radial',2,4,'Touchpad','Blouse'],
                      ['Radial',2,4,'Touchpad','Bus'],
                      ['Radial',3,4,'Touchpad','Red Bus'],
                      ['Radial',3,4,'Touchpad','Purple Plum'],
                      ['Radial',3,4,'Touchpad','Purple Van']], columns=columns)

cond8 = pd.DataFrame([['Radial',1,8,'Touchpad','Clothing'],
                      ['Radial',1,8,'Touchpad','Animal'],
                      ['Radial',1,8,'Touchpad','Transportation'],
                      ['Radial',2,8,'Touchpad','Accordion'],
                      ['Radial',2,8,'Touchpad','Airplane'],
                      ['Radial',2,8,'Touchpad','Mattress'],
                      ['Radial',3,8,'Touchpad','White Snake'],
                      ['Radial',3,8,'Touchpad','Pink Camera'],
                      ['Radial',3,8,'Touchpad','Blue Trumpet']], columns=columns)

def shuffle_trials(df, n_trial):
    res = list()
    n_row = df.shape[0]
    for i in range(0, n_row, n_trial):
        temp = shuffle(df[i:i+n_trial])
        res.append(temp)
    return pd.concat(res)

df1 = [cond1, cond2, cond3, cond4, cond5, cond6, cond7, cond8]
p1 = pd.concat(df1, ignore_index=True)
p1 = shuffle_trials(p1, 3)
p1.to_csv('set1.csv', index=False)

df2 = [cond2, cond1, cond4, cond3, cond6, cond5, cond8, cond7]
p2 = pd.concat(df2, ignore_index=True)
p1 = shuffle_trials(p2, 3)
p2.to_csv('set2.csv', index=False)

df3 = [cond3, cond4, cond1, cond2, cond7, cond8, cond5, cond6]
p3 = pd.concat(df3, ignore_index=True)
p1 = shuffle_trials(p3, 3)
p3.to_csv('set3.csv', index=False)

df4 = [cond4, cond3, cond2, cond1, cond8, cond7, cond6, cond5]
p4 = pd.concat(df4, ignore_index=True)
p1 = shuffle_trials(p4, 3)
p4.to_csv('set4.csv', index=False)

df5 = [cond5, cond6, cond7, cond8, cond1, cond2, cond3, cond4]
p5 = pd.concat(df5, ignore_index=True)
p1 = shuffle_trials(p5, 3)
p5.to_csv('set5.csv', index=False)

df6 = [cond6, cond5, cond8, cond7, cond2, cond1, cond4, cond3]
p6 = pd.concat(df6, ignore_index=True)
p1 = shuffle_trials(p6, 3)
p6.to_csv('set6.csv', index=False)

df7 = [cond7, cond8, cond5, cond6, cond3, cond4, cond1, cond2]
p7 = pd.concat(df7, ignore_index=True)
p1 = shuffle_trials(p7, 3)
p7.to_csv('set7.csv', index=False)

df8 = [cond8, cond7, cond6, cond5, cond4, cond3, cond2, cond1]
p8 = pd.concat(df8, ignore_index=True)
p1 = shuffle_trials(p8, 3)
p8.to_csv('set8.csv', index=False)
