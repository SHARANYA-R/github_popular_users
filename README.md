# github_popular_users
To get the most popular users from the GitHub API using Python

### Setup and Bring server up
chmod +x setup.sh
./setup.sh
# This should start running the application

### Run views module to start the flask application if the requirements are already installed
# Also for subsequent runs
source env/bin/activate
python views.py

Open a browser and go to [http://127.0.0.1:5000/](localhost) where the application is running. Enter technology of your choice and the app will display the popular users in that technology from Github.
