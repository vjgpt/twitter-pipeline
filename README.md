# Twitter scheduler using Apache Airflow on Docker

Here we will be building out a Twitter Scheduler data pipeline, the idea is to collect hundreds of tweets in a file and all the tweets will be segregated and posted on Twitter profile depending on the time it's scheduled for.

### Key takeaways from this project are:
- Make a Twitter Scheduler Data Pipeline.
- Understand how Airflow works on Docker

### To learn more about it follow my Medium blog [here](https://medium.com/p/twitter-data-pipeline-using-apache-airflow-24e0881c214d?source=email-f17526e917b6--writer.postDistributed&sk=3fdccd5247579187f0d37b083d2f1dda) :point_left: :books:

## Pre-Requisites

**Step - 1**

Install Docker from their official [site](https://docs.docker.com/get-docker/).

Quick links to download:

  - [Docker for macOS](https://docs.docker.com/docker-for-mac/install/)

  - [Docker for Windows 10 Pro or later](https://docs.docker.com/docker-for-windows/install/)

**Step - 2**

Make a Twitter Developer API account. [(Apply for access - Twitter Developers | Twitter Developer)](https://developer.twitter.com/en/apply-for-access)

After you are done with creating a Twitter Developer account, make sure you save the keys and credentials required and put it in topic_tweet.py file

```
consumer_key = ''           # Add your API key here
consumer_secret = ''        # Add your API secret key here
access_token = ''           # Add your Access Token key here
access_token_secret = ''    # Add your Access Token secret key here
```

**Step - 3**

Enable Google Drive v3 to backup all your data. [(Python Quickstart | Google Drive API | Google Developers)](https://developers.google.com/drive/api/v3/quickstart/python)

To setup the Google Drive API, you need to create a python environment in your local machine and follow the above link. After you allow giving permission to your app, you will get two files credentials.json and token.pickle. Copy these two files and put it in the repo twitter-pipeline/dags/daglibs folder path.

```
├── dags
│   ├── daglibs
│   │   ├── credentials.json
│   │   ├── etl_job.py
│   │   ├── token.pickle
│   │   ├── topic_tweet.py
│   │   └── upload.py
│   └── post_tweet.py
├── data
```

## How to run this project?

We will be running Airflow in Local Executor mode, which means the compose file won't build your image, go ahead and just build it yourself locally before moving on.

```
cd twitter-pipeline
docker build -t aflatest .
```

Now you are ready to start those containers and run Apache Airflow, make sure you are in the home path of twitter-pipeline repo.

```
docker-compose -f docker-compose-LocalExecutor.yml up -d
```

`docker-compose up -d` to start your containers in the background (i.e., detached mode)


#### Hit the web UI at [http://localhost:8080](http://localhost:8080)


You should see any DAGs you put in the ./dags directory, although sometimes it can take a minute for them to show up.

Once the DAG shows up, any changes you make to the python file will immediately be effective the next time you trigger the DAG.

### Other helpful commands

You can **tear down the Compose setup** using 
```
docker-compose -f docker-compose-LocalExecutor.yml down 
```

You **check the logs** of services running in background mode using
```
docker-compose -f docker-compose-LocalExecutor.yml logs
```

#### Now, let's test this pipeline.

Add some tweets in the txt files present in `data/tweets` folder, you can add multiple tweets to that file or create a new file and add tweets in that. Then trigger the pipeline and you would find your tweet posted in your Twitter account and all the files getting backed up in Google Drive.


If you need to learn more about how this pipeline works and how to use it effectively, Checkout this [blog](https://medium.com/p/twitter-data-pipeline-using-apache-airflow-24e0881c214d?source=email-f17526e917b6--writer.postDistributed&sk=3fdccd5247579187f0d37b083d2f1dda) where i have explained the process thoroughly. If this is helping you in some way, please support my work by liking my [blog](https://medium.com/p/twitter-data-pipeline-using-apache-airflow-24e0881c214d?source=email-f17526e917b6--writer.postDistributed&sk=3fdccd5247579187f0d37b083d2f1dda) or by giving this repo a star. 

Happy Learning!!

