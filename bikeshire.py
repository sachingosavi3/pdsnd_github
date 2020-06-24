import time 
import pandas as pd 
import numpy as np 
from datetime import datetime 
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
    #print('Hello! Let\'s explore some US bikeshare data!') 
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nName of the city (chicago, new york city, washington) to analyze:').lower() 
    exists = city in CITY_DATA 
    if not exists : 
      print('Enter Valid City Name.\n') 
      city, month, day = get_filters() 
      return city, month, day 
    
    # TO DO: get user input for month (all, january, february, ... , june) 
    month = input('\nName of the month to see stats(january, february, ... , june) to filter by, or "all" to apply no month filter:').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
    day = input('\nName of the day of week(monday, tuesday, ... sunday) to filter by, or "all" to apply no day filter:').lower()

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
    df['End Time'] = pd.to_datetime(df['End Time']) 
    df['month'] =df['Start Time'].dt.month 
    df['day'] =df['Start Time'].dt.weekday_name 
    df['hour'] =df['Start Time'].dt.hour 
    
    if month != 'all': 
        # use the index of the months list to get the corresponding int 
        months = ['january', 'february', 'march', 'april', 'may', 'june'] 
        month = months.index(month.lower()) + 1 
        # filter by month to create the new dataframe 
        df = df[df['month'] == month] 
        # filter by day of week if applicable 
    if day != 'all': 
        # filter by day of week to create the new dataframe 
        df = df[df['day'] == day.title()] 
    return df 

def time_stats(df): 
    """Displays statistics on the most frequent times of travel.""" 
    print('\nCalculating The Most Frequent Times of Travel...\n') 
    start_time = time.time() 
    
    # TO DO: display the most common month 
    popular_month =df['month'].mode()[0] 
    print('Most Frequent Start Month:', popular_month) 

    # TO DO: display the most common day of week 
    popular_day_of_week =df['day'].mode()[0] 
    print('Most Frequent Start day_of_week:', popular_day_of_week) 

    # TO DO: display the most common start hour 
    popular_hour =df['hour'].mode()[0] 
    print('Most Frequent Start Hour:', popular_hour) 

    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 
    
    
def station_stats(df): 
    """Displays statistics on the most popular stations and trip.""" 
    print('\nCalculating The Most Popular Stations and Trip...\n') 
    start_time = time.time() 
    # TO DO: display most commonly used start station 
    popular_start_station =df['Start Station'].mode()[0] 
    print('Most commonly used start station:', popular_start_station) 
    
    # TO DO: display most commonly used end station 
    popular_end_station =df['End Station'].mode()[0] 
    print('Most commonly used end station:', popular_end_station) 

    # TO DO: display most frequent combination of start station and end station trip 
    df['Both Station'] =df['Start Station'] + " to " +df['End Station'] 
    popular_combi =df['Both Station'].mode()[0] 
    print('Most commonly used start and end station combination:', popular_combi) 

    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

def trip_duration_stats(df): 
    """Displays statistics on the total and average trip duration.""" 
    print('\nCalculating Trip Duration...\n') 
    start_time = time.time() 
    # TO DO: display total travel time 
    df['travel_time'] = df['End Time'] - df['Start Time'] 
    #print(df.dtypes) 
    
    tot_time =df['travel_time'].sum() 
    print('total travel time:', tot_time) 
    # TO DO: display mean travel time 
    mean_time =df['travel_time'].mean() 
    print('mean travel time:', mean_time) 

    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

def user_stats(city,df): 
    """Displays statistics on bikeshare users.""" 
    print('\nCalculating User Stats...\n') 
    start_time = time.time() 
    # TO DO: Display counts of user types 
    df2=df.groupby('User Type').count() 
    print('counts of user types:', df2.iloc[:,[0]]) 
    
    if city != 'washington': 
        # TO DO: Display counts of gender 
        df2=df.groupby('Gender').count() 
        print('counts of gender:', df2.iloc[:,[0]]) 

        # TO DO: Display earliest, most recent, and most common year of birth 
        by_earliest=df['Birth Year'].min() 
        print('Earliest year of birth:', by_earliest) 
        by_most_recent=df['Birth Year'].max() 
        print('Most recent year of birth:', by_most_recent) 
        by_most_common=df['Birth Year'].mode()[0] 
        print('Most common year of birth:', by_most_common) 
    
    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

def main(): 
    while True: 
        print('Hello! Let\'s explore some US bikeshare data!') 
        city, month, day = get_filters() 
        df = load_data(city, month, day) 
        df_copy = df.copy() 
        time_stats(df)       
        station_stats(df) 
        trip_duration_stats(df) 
        user_stats(city,df) 
        df_copy.drop(columns=['month', 'day', 'hour']) 
        raw_data = input('\nDo you want to see the first 5 rows of data? Enter yes or no.\n') 
        if raw_data.lower() == 'yes' : 
            i=0 
            print(df_copy.iloc[5*i:5*(i+1)]) 
            while raw_data.lower() == 'yes' : 
                raw_data = input('\nDo you want to see the next 5 rows of data? Enter yes or no.\n') 
                if raw_data.lower() == 'yes' : 
                    i = i + 1 
                    print(df_copy.iloc[5*i:5*(i+1)]) 
        restart = input('\nWould you like to restart? Enter yes or no.\n') 
        if restart.lower() != 'yes': 
            break 

if __name__ == "__main__": 
        main() 

