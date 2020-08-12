import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list = ['chicago', 'new york city', 'washington']
month_list = ['all', 'janurary', 'february', 'march', 'april', 'may', 'june']
day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def askuser (options, prompt_message):
    answer = ""
    while len(answer) == 0:
        answer = input(prompt_message)
        answer = answer.strip().lower()

        if answer in options:
            return answer
        else:
            answer = ""
            print("Please enter one of the options \n")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = askuser(
        city_list,
        "please enter two cities: chicago, new york city or washington > ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = askuser(
        month_list,
        "please enter month: janurary, february, march, april, may, june or all > ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = askuser(
        day_list,
        "Please enter: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all > ")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #uploading file and creating new columns
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    Start_Time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print(month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name
    common_day = df['day_of_week'].mode()[0]
    print(common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - Start_Time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    Start_Time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + 'to' + df['End Station']
    frequent_combination = df['combination'].mode()[0]
    print(frequent_combination)

    print("\nThis took %s seconds." % (time.time() - Start_Time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    Start_Time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - Start_Time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    Start_Time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print(user_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        Gender = df['Gender'].value_counts()
        print(Gender)
    else:
        print("No gender information in this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print(earliest_birth_year)
        recent_birth_year = df['Birth Year'].max()
        print(recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print(common_birth_year)
    else:
        print("No birth year information in this city")

    print("\nThis took %s seconds." % (time.time() - Start_Time))
    print('-'*40)

def raw_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data:
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display.lower() != 'yes':
            break
        print(df[start:end])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
