import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city name:")

    # get user input for month (all, january, february, ... , june)
    month = input("Enter the month:")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the week:")


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(f'\nMost Popular Month:{common_month}')

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(f'\nMost Popular Day of the Week:{common_day_of_week}')

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(f'\nMost Popular Hour:{common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_ststation = df['Start Station'].mode()[0]
    print(f'\nMost Popular Start Station:{common_ststation}')

    # display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print(f'\nMost Popular End Station:{common_endstation}')

    # display most frequent combination of start station and end station trip
    common_stend_station = common_ststation + " & " + common_endstation
    print(f'\nMost Popular Start and End Station:{common_stend_station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'\nThe total trip duration is (in mins):{total_travel_time}')

    # display mean travel time
    total_travel_mean = df['Trip Duration'].mean()
    print(f'\nThe mean trip duration is (in mins):{total_travel_mean}')

    print(f"\nThis took %s seconds.{(time.time() - start_time)}")
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'\nThese are the various types of users:{user_types}')

    # Display counts of gender
    gender_types = df['Gender'].value_counts()
    print(f'\nThese are the various types of genders:{gender_types}')

    # Display earliest, most recent, and most common year of birth
    birth_year_min = df['Birth Year'].min()
    print(f'\nThe earliest birth year is:{birth_year_min}')

    birth_year_max = df['Birth Year'].max()
    print(f'\nThe most recent birth year is:{birth_year_max}')

    birth_year_common = df['Birth Year'].mode()[0]
    print(f'\nThe most common birth year is:{birth_year_common}')

    print(f"\nThis took %s seconds.{(time.time() - start_time)}")
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
