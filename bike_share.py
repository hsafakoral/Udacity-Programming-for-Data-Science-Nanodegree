#! /usr/bin/python
from datetime import timedelta
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city_n = ''

    while city_n.lower() not in CITY_DATA:
        city_n= input("\nWhich city do you like to see? Washington, New York City, Chicago?\n")
        if city_n.lower() in CITY_DATA:
            city = CITY_DATA[city_n.lower()]
        else:
            print("Sorry, Could You Please Try Again.\n")
            
            month_n = '' 
    while month_n.lower() not in MONTH_DATA:
        month_n = input("\nWhich month do you like to see? January, February, March, April, May, June or type 'all' if you want to see all?\n")
        if month_n.lower() in MONTH_DATA:
            month = month_n.lower()
        else:
            print("Sorry, Could You Please Try Again.\n")


    day_n = '' 
    while day_n.lower() not in DAY_DATA:
        day_n = input("\nWhich day do you like to see?? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you want to see all.\n")
        if day_n.lower() in DAY_DATA:
            day = day_n.lower()
        else:
            print("Sorry, Could You Please Try Again.\n")
            
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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use index of month list to get corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create new dataframe
        df = df.loc[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# look_up dictionary 
    look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    # display the most common month
    popular_month = df['Month'].mode()[0]
    month_in_string = look_up[str(popular_month)]
    print("1. The most common month was: ", month_in_string)

    # display the most common day of week
    popular_day = df['Day_of_Week'].mode()[0]
    print("2. The most common day of the week was: {}".format(popular_day))

    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('3. The most common start hour was:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print("Most Commonly used start station : " + Start_Station)

    #display most commonly used end station
    End_Station = df['End Station'].mode()[0]
    print("Most Commonly used end station : " + End_Station)

    #display most frequent combination of start station and end station trip
    Combination_Station = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("Most Commonly used combination of start station and end station trip : " + str( Combination_Station.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print("Total travel time : " + str(Total_Travel_Time))

    #display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print("Mean travel time : " + str(Mean_Travel_Time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types : \n" + str(user_types))

    #Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("Gender Types : \n" + str(gender))

        #Display earliest, most recent, and most common year of birth
        Earliest_Year = df['Birth Year'].min()
        Most_Recent_Year = df['Birth Year'].max()
        Most_Common_Year = df['Birth Year'].mode()[0]
        print('Earliest Year : {}\n'.format(Earliest_Year))
        print('Most Recent Year : {}\n'.format(Most_Recent_Year))
        print('Most Common Year : {}\n'.format(Most_Common_Year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """Displays raw data on user request."""
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nDo you want to view next 5 row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

        #MAIN FUNCTION
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