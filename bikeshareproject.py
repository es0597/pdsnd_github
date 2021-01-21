import time
import pandas as pd
import numpy as np
import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("\nWould you like to see data for Chicago, New York City or Washington?\n").lower()
        if city not in cities:
            print('Sorry,{} is not a valid choice. Please try again by entering either Chicago, New York City or Washington'.format(city))
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("\nWhat month would you like to see? Please select from the following: [All, January, February, March, April, May, June]:\n").lower()
        if month not in months:
            print('Sorry,{} is not a valid choice. Please try again by entering either All, January, February, March, April, May or June'.format(month))
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("\nWhat day would you like to see? Please select from the following: [All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday]:\n")
        if day not in day_of_week:
            print('Sorry,{} is not a valid choice. Please try again by entering either All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday'.format(day))
            continue
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:Pandas
        df - PandasFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day) + 1
        df = df[df['day'] == day]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = months[df['month'].mode()[0] - 1]
    print('The most common month is {}'.format(common_month))

    # TO DO: display the most common day of week
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    common_day = df['day'].mode()[0]
    print('The most common day is {}'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    common_hour_count = hour.value_counts().max()
    print('The most common hour is {} and count is {}'.format(common_hour,common_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(
    df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print("The most common end station is: {} ".format(
    df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['station_from_to'] = df['Start Station'] + " " + df['End Station']
    print("The most common start and end station combo is: {} ".format(
    df['station_from_to'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['duration'] = df['End Time'] - df['Start Time']
    print("The total travel time is: {} ".format(
    df['duration'].sum()))

    # TO DO: display mean travel time
    print("The mean travel time is: {} ".format(
    df['duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Here are the counts of various user types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nHere are the counts of gender:')
        print(df['Gender'].value_counts())
    else:
        print("\nGender statistics are not available in Washington.")

        # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent_birthyear = df['Birth Year'].max()
        print('\nMost recent birth year:', int(most_recent_birthyear))
        earliest_birthyear = df['Birth Year'].min()
        print('Earliest birth year:', int(earliest_birthyear))
        most_common_birthyear = df['Birth Year'].mode()[0]
        print('Most common birth year:', int(most_common_birthyear))
    else:
        print("\nBirth statistics are not available in Washington.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    """ Display 5 lines raw data as requested by the user."""

    i = 0

    raw_data = input("Would you like to see the first 5 rows of raw data? yes or no:\n").lower()

    pd.set_option('display.max_columns',200)

    while True:
    display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    if display_data.lower() != 'yes':
        break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
            	main()
