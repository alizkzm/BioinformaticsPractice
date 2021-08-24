import pandas as pd
from sklearn import linear_model

SEX =          {'Ass':       [55,50,70,80,60,65,75,70,55,60,80],
                'Thigh':     [60,60,70,80,70,75,70,70,60,60,70],
                'Boob':      [80,45,75,75,70,70,75,65,75,55,75],
                'Horniness': [70,55,50,60,70,80,65,75,70,25,80],
                'Prettines': [55,65,65,80,75,70,55,70,65,65,55],
                'Color':     [45,55,50,75,80,70,35,55,85,75,75],
                'SexAge':    [55,45,70,90,85,85,60,75,70,70,65]
                }

df = pd.DataFrame(SEX,columns=['Ass','Thigh','Boob','Horniness','Prettines','Color','SexAge'])
x = df[['Ass','Thigh','Boob','Horniness','Prettines','Color']]
Y = df['SexAge']
regr = linear_model.LinearRegression()
regr.fit(x, Y)
predictions = regr.predict(x)

sample ={'Ass':      [65,60],
        'Thigh':     [70,80],
        'Boob':      [90,70],
        'Horniness': [80,85],
        'Prettines': [65,60],
        'Color':     [75,55],
        }
sampleDF = pd.DataFrame(sample,columns=['Ass','Thigh','Boob','Horniness','Prettines','Color'])
sampleSexAge = regr.predict(sampleDF)
print(sampleSexAge)


print(regr.score(x,Y))
print(predictions)