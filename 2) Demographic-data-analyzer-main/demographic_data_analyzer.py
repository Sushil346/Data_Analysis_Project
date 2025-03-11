import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'] .mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round( ( (df['education'] == 'Bachelors').sum() / df['education'].count() ) * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    adv_people_count = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    adv_people_morethan50k = len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')])
    percentage = round( (adv_people_morethan50k / adv_people_count) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    nonadv_people = ( ~ df['education'].isin(['Bachelors','Masters','Doctorate']) )
    nonadv_people_count = nonadv_people.sum() # // it workd because nonadv..count is a boolean list (df)
    print(nonadv_people_count)
    nonadv_people_morethan50k = (nonadv_people & (df['salary']=='>50K') ).sum()
    print(nonadv_people_morethan50k)

    percentage1 = round(nonadv_people_morethan50k / nonadv_people_count * 100, 1)
    print(percentage1)


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = adv_people_count
    lower_education = nonadv_people_count

    # percentage with salary >50K
    higher_education_rich = percentage
    lower_education_rich = percentage1

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    min_work_people = ( df['hours-per-week'] ==  min_work_hours).sum()
    min_work_morethan50k = ( df['hours-per-week'] == min_work_hours & ( df['salary'] == '>50K' ) ).sum()
    percentage2 = min_work_morethan50k /min_work_people * 100
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = min_work_morethan50k

    rich_percentage = percentage2

    # What country has the highest percentage of people that earn >50K?

    country_percentage = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
    country_with_highest = country_percentage.idxmax() #return country name
    highest_percentage = country_percentage.max() #return countriy percentage
     

    highest_earning_country = country_with_highest
    highest_earning_country_percentage = round(highest_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.

    occupation__percentage = df[ (df['native-country'] == 'India') & (df['salary'] == '>50K') ].groupby('occupation').size()
    occupation_most_preffered = occupation__percentage.idxmax()
    occupation_most_preffered_value = occupation__percentage.max()
    print(f"Occupation: {occupation_most_preffered} is the most preffered by the people in India who is earning more than 50k whose percentage is {occupation_most_preffered_value} ")


    top_IN_occupation = occupation_most_preffered

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
