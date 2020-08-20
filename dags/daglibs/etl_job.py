import pandas as pd
from os import listdir
from os.path import isfile, join
from daglibs.topic_tweet import post_tweets
import sys
import os

sys.path.append(os.path.dirname(__file__))

homepath = '/usr/local/airflow/'

def stage_tweets():
    """
    We need to make a file where we will be adding our tweets.
    Also the above file will be in csv, add a new column where 
    you flag if its updated in the master file or not.
    All the parsed tweet needs to go to a csv file.
    """
    homepath = '/usr/local/airflow/tweets/'
    stage_file = join(homepath, 'data/tweets/tweets.csv')
    filenames = [f for f in listdir(homepath) if isfile(join(homepath, f))]
    df = pd.DataFrame(columns=['tweets','staged'])
    final_file = []
    for file in filenames:
        file1 = open(join(homepath, f"{file}"),"r+")
        for index,tweet in enumerate(file1.readlines()):
            print (index, tweet)
            tmp_df = [tweet,'False']
            df.loc[len(df)] = tmp_df
        file1.truncate(0)
        file1.close()
    df.to_csv('/usr/local/airflow/data/tweets/tweets.csv',mode='a',header=False,index=False)

def commit_tweets():
    """
    Here all the tweets from stage path will go 
    into final csv files
    """
    stage_file = join(homepath, 'data/tweets/tweets.csv')
    final_file = join(homepath, 'data/finaltest.csv')
    try:
        stage_data = pd.read_csv(stage_file)
        stage_data.columns = ['tweets','staged']
    except:
        stage_data = pd.DataFrame(columns=['tweets','staged'])

    try:
        final_data = pd.read_csv(final_file)
        final_data.columns = ['tweets','status']
    except:
        final_data = pd.DataFrame(columns=['tweets','status'])

    for stwee in stage_data.index:
        flag = False
        if stage_data['staged'][stwee] == False:
            for ftwee in final_data.index:
                if stage_data['tweets'][stwee] == final_data['tweets'][ftwee]:
                    flag = True
                    print("Inside true flag")
            print(flag)
            print(stage_data['tweets'][stwee])
            if flag == False:
                final_data.loc[len(final_data)] = [stage_data['tweets'][stwee],'false']
            stage_data['staged'][stwee] = True
    stage_data.to_csv(stage_file,index=False)
    final_data.to_csv(final_file, header=False,index=False)
    return True

# Read from CSV, select tweet and post it and then change the status
def post_tweet():
    data = pd.read_csv("/usr/local/airflow/final.csv")
    for t in data.index:
        if data['status'][t] == False:
            #Post the tweet
            print ("posting")
            print (post_tweets(data['tweets'][t]))

            #Change the status
            data['status'][t] = True
            data.to_csv('/usr/local/airflow/final.csv', index_label="Index", index=False)
            
            return True
        else:
            pass
    return False

