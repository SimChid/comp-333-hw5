# comp-333-hw5
Unit testing repo for the Startunes site and app.

## Work distribution:
Problems 1,2,3: Simon Chidley
Problems 4,5,6: Aaron Foote

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

Once setup, return to the music_db tab. In the SQL tab, run the following command:
```sql
INSERT INTO users (username,password) VALUES ('Simon', 'strongpassword');
INSERT INTO ratings (username,artist,song,rating) VALUES ('user','artist1','song1',1);
INSERT INTO ratings (username,artist,song,rating) VALUES ('user','Blur','Song 2',5);
INSERT INTO ratings (username,artist,song,rating) VALUES ('Simon','Remi Wolf','Photo ID',4);
INSERT INTO ratings (username,artist,song,rating) VALUES ('user','artist4','song4',1);
```
Going back to the 'Manage Servers' tab in manager-osx. Click on Apache Web Server, then click on 'Configure'. Read the port number listed, and if necessary, go to line 9 of StackTest.php, which should read:
```php
$this->client = new GuzzleHttp\Client(["base_uri" => "http://localhost:80"]);
```
At the end of the line where it says '80', replace it with the port number listed in the configure window.
