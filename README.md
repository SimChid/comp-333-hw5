# comp-333-hw5
Unit testing repo for the Startunes site and app.

## Work distribution:
- Problems 1,2,3: Simon Chidley
- Problems 4,5,6: Aaron Foote

## pytest setup
To start, assuming python3 is already installed, type the following command into your temrinal:
```bash
pip3 install pytest
```
In the terminal, change to the directory that contains unit_testing_py_test.py and simply type 'pytest' into the terminal. It should return 7 passes, and 4 fails.

To get more in-depth with the assertions, run the following command:
```bash
pytest -v
```

## PHP unit testing setup
Please note the following:
- There is no command in the API to get the uesr list for testGet_UserList, so in its place we have testGet_SongList.
- For all functions except testGet_SongList, the assignment asks to assert that the server responds with a 201 response code. All funcitons came back with a 200 code, so that's how it is tested in StackTest.php.

Download the backend code from [here](https://github.com/SimChid/comp-333-hw3), and follow the instructions under that backend section in the readme to setup.

Once setup, return to the music_db tab. In the SQL tab, run the following commands:
```sql
INSERT INTO users (username,password) VALUES ('Simon', 'strongpassword');
INSERT INTO ratings (username,artist,song,rating) VALUES ('user','artist1','song1',1);
INSERT INTO ratings (username,artist,song,rating) VALUES ('user','Blur','Song 2',5);
INSERT INTO ratings (username,artist,song,rating) VALUES ('Simon','Remi Wolf','Photo ID',4);
INSERT INTO ratings (username,artist,song,rating) VALUES ('user','artist4','song4',1);
```
In your terminal, assuming brew is already installed, run the following commands:
```bash
brew install phpunit
```
```bash
brew install composer
```
If php is not installed, run
```bash
brew install php
```
In the file where the backend is stored, create a new folder called test-project, and switch to that directory in the terminal. Then run the following command and use the images below see what you should input as the instructions come up.
```bash
composer init
```

![image](https://github.com/SimChid/comp-333-hw5/assets/144281352/bf3fc890-2e24-4bda-84a3-03f4a5071e5f)
![image](https://github.com/SimChid/comp-333-hw5/assets/144281352/5060c335-7cf6-45ca-9def-f9a00138ead2)

Once done, install Guzzle with the following command:
```bash
composer require guzzlehttp/guzzle
```
Create a folder in test-project called 'tests', Which is where you will place StackTests.php.

Going back to the 'Manage Servers' tab in manager-osx. Click on Apache Web Server, then click on 'Configure'. Read the port number listed, and if necessary, go to line 9 of StackTest.php, which should read:
```php
$this->client = new GuzzleHttp\Client(["base_uri" => "http://localhost:80"]);
```
At the end of the line where it says '80', replace it with the port number listed in the configure window.

Once everything is set up, run the tests within test-project in the terminal using the following command. You should see 7 passes and 0 fails.
```bash
php vendor/bin/phpunit tests
```
## Problem 4

To get the app/tests up and running on your own device, first clone the repository. Next, navigate into the `my-jest-test` directory. Run the command `npm install` to get all of the dependencies, and then run `npm start` to run the app or `npm test` to run the tests. Just as a side note, I did not  do question 2d. I went to TA hours on Monday, SCIC hours on Tuesday, Professor Zimmeck's office hours on Wednesday, and more SCIC hours on Wednesday, but ultimately nobody was able to figure out why some `fireEvent.click()` commands work and others don't within the same test. I do parts 2a,2b, and 2c though.
## Problem 5
As instructed, the automated tests are in the `.github/workflows` directory (node.js, not the demo file). Shoutout Gavin for helping me get those working.

## Problem 6

I asked ChatGPT to help write a test that simulates user input using Jest. Initially it wasn't very helpful, but I was able to refine my question to get it to answer the question using `user-event`. It wasn't correct but it got me moving in the right direction. Nothing I couldn't have just done with a regular search engine though. To see the conversation, check out this [this link](https://chat.openai.com/share/5725218a-8fed-4475-b00e-7ad949e9de50). This should show the exact questions I asked and the code ChatGPT provided.
