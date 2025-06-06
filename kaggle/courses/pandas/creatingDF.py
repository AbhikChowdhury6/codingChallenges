import pandas as pd

#q1
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
fruits = pd.DataFrame({"Apples": [30], "Bananas": [21]})

#q2
fruit_sales = pd.DataFrame({"Apples": [35, 41], "Bananas": [21, 34]},
                index=["2017 Sales", "2018 Sales"])

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])

#q3
ingredients = pd.Series(index=["Flour", "Milk", "Eggs", "Spam"],
                        name="Dinner", 
                        data=["4 cups", "1 cup", "2 large", "1 can"])

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')


#q4
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

#q5
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv("cows_and_goats.csv")




