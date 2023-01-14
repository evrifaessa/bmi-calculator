print('''The body mass index, abbreviated as BMI, is a measure of a person's weight relative to height that correlates fairly well with body fat. The BMI is accepted as the most useful indicator of obesity in adults when only weight and height data are available.

BMI is calculated by dividing body weight (in kilograms) by height (in metres) squared.

The following subdivisions are used to categorise the BMI into five categories:

    < 18.5: underweight;
    >= 18.5 and < 25: normal weight;
    >= 25 and < 30: pre-obese;
    >= 25: overweight;
    >= 30: obese.

Note that the BMI is not calculated for children.
-----
The definition above was quoted from the "Statistics Explained" website made by the European Union.
Read more: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Body_mass_index_(BMI)
-----''')

def bmi():
    mass = input("To calculate your BMI, please input your body weight (in kilograms): ")
    height = input("Please input your body height (in metres): ")

    mass = float(mass.replace(',', '.'))
    height = float(height.replace(',', '.'))

    if mass <= 0:
        raise ValueError("Your weight must be a positive number of kilograms.")
    
    if height <= 0:
        raise ValueError("Your height must be a positive number of meters.")

    if height > 2.75: # Slightly higher than the tallest human recorded in the history
        # If the inputted height is more than this, it likely was inputted in centimeters.
        height = height / 100 # Converted that to meters
    
    calculated = mass / (height ** 2)
    calculated = float(f'{calculated:.2f}') # ab.cdefgh... -> ab.cd

    print ("-----")

    if calculated < 18.5:
        print("Based on your BMI ({}), you seem to be underweight.".format(calculated))
    elif calculated < 25:
        print("Based on your BMI ({}), you seem to be in your normal range of weight.".format(calculated))
    elif calculated < 30:
        print("Based on your BMI ({}), you seem to be overweight (pre-obese).".format(calculated))
    else:
        print("Based on your BMI ({}), you seem to be overweight (obese).".format(calculated))
    
    print("These ranges of BMI values are valid only as statistical categories. Definitions vary by country, ethnic group, age and gender.")
    print("You also might be interested in the 'Obesity and overweight' fact sheet by the World Health Organization: https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight")

    print("-----")
    print("https://github.com/evrifaessa")

bmi()
