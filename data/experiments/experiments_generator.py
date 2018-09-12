import pandas as pd
from sklearn.utils import shuffle

menu_type = ['Marking', 'Radial']
menu_depth = [1, 2, 3]
menu_breadth = [4, 8]
input_device = ['Mouse', 'Touchpad']

def shuffle_trials(df, n_trial):
    res = list()
    n_row = df.shape[0]
    for i in range(0, n_row, n_trial):
        temp = shuffle(df[i:i+n_trial])
        res.append(temp)
    return pd.concat(res)


columns = ['Menu Type','Menu Depth','Menu Breadth',
           'Input Device','Target Item']
df = pd.DataFrame(columns=columns)

cond1 = pd.DataFrame([['Marking',1,4,'Mouse','xxx'],
                      ['Marking',2,4,'Mouse','xxx'],
                      ['Marking',3,4,'Mouse','xxx']], columns=columns)

cond2 = pd.DataFrame([['Marking',1,8,'Mouse','xxx'],
                      ['Marking',2,8,'Mouse','xxx'],
                      ['Marking',3,8,'Mouse','xxx']], columns=columns)

cond3 = pd.DataFrame([['Marking',1,4,'Touchpad','xxx'],
                      ['Marking',2,4,'Touchpad','xxx'],
                      ['Marking',3,4,'Touchpad','xxx']], columns=columns)

cond4 = pd.DataFrame([['Marking',1,8,'Touchpad','xxx'],
                      ['Marking',2,8,'Touchpad','xxx'],
                      ['Marking',3,8,'Touchpad','xxx']], columns=columns)

cond5 = pd.DataFrame([['Radial',1,4,'Mouse','xxx'],
                      ['Radial',2,4,'Mouse','xxx'],
                      ['Radial',3,4,'Mouse','xxx']], columns=columns)

cond6 = pd.DataFrame([['Radial',1,8,'Mouse','xxx'],
                      ['Radial',2,8,'Mouse','xxx'],
                      ['Radial',3,8,'Mouse','xxx']], columns=columns)

cond7 = pd.DataFrame([['Radial',1,4,'Touchpad','xxx'],
                      ['Radial',2,4,'Touchpad','xxx'],
                      ['Radial',3,4,'Touchpad','xxx']], columns=columns)

cond8 = pd.DataFrame([['Radial',1,8,'Touchpad','xxx'],
                      ['Radial',2,8,'Touchpad','xxx'],
                      ['Radial',3,8,'Touchpad','xxx']], columns=columns)

df1 = [cond1, cond2, cond3, cond4, cond5, cond6, cond7, cond8]
p1 = pd.concat(df1, ignore_index=True)
p1.to_csv('set1.csv', index=False)

df2 = [cond2, cond1, cond4, cond3, cond6, cond5, cond8, cond7]
p2 = pd.concat(df2, ignore_index=True)
p2.to_csv('set2.csv', index=False)

df3 = [cond3, cond4, cond1, cond2, cond7, cond8, cond5, cond6]
p3 = pd.concat(df3, ignore_index=True)
p3.to_csv('set3.csv', index=False)

df4 = [cond4, cond3, cond2, cond1, cond8, cond7, cond6, cond5]
p4 = pd.concat(df4, ignore_index=True)
p4.to_csv('set4.csv', index=False)

df5 = [cond5, cond6, cond7, cond8, cond1, cond2, cond3, cond4]
p5 = pd.concat(df5, ignore_index=True)
p5.to_csv('set5.csv', index=False)

df6 = [cond6, cond5, cond8, cond7, cond2, cond1, cond4, cond3]
p6 = pd.concat(df6, ignore_index=True)
p6.to_csv('set6.csv', index=False)

df7 = [cond7, cond8, cond5, cond6, cond3, cond4, cond1, cond2]
p7 = pd.concat(df7, ignore_index=True)
p7.to_csv('set7.csv', index=False)

df8 = [cond8, cond7, cond6, cond5, cond4, cond3, cond2, cond1]
p8 = pd.concat(df8, ignore_index=True)
p8.to_csv('set8.csv', index=False)
