<?php

class StackTest extends PHPUnit\Framework\TestCase
{
    protected $client;

    protected function setUp() : void{
        parent::setUp();
        $this->client = new GuzzleHttp\Client(["base_uri" => "http://localhost:80"]); //port # will very likely be different!!
    }

    public function testGet_SongList() {
        $response = $this->client->request('GET', 'comp-333-hw3/index.php/song/enumerate');
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testPost_CreateUser() {
        $response = $this->client->request('POST', 'comp-333-hw3/index.php/user/create',[
            'username' => 'ThisUserDefinitelyDoesntExist123454321',
            'password' => 'qwjehrpidsjgfoahsdgf'
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testPost_LoginUser() {
        $response = $this->client->request('POST', 'comp-333-hw3/index.php/user/read',[
            'username' => 'Simon',
            'password' => 'strongpassword' //this account must be created within the local database.
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testPost_FailedLogin() { //intentional fail
        $response = $this->client->request('POST', 'comp-333-hw3/index.php/user/read',[
            'username' => 'Simon',
            'password' => 'wrongpassword'
        ]);
        $this->assertEquals(200, $response->getStatusCode()); // should return a fail.
    }

    public function testPost_NewSong() {
        $response = $this->client->request('POST', 'comp-333-hw3/index.php/song/create',[
            'username' => 'Simon',
            'artist' => 'Ride',
            'song' => 'Vapour Trails',
            'rating' => '5'
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testPost_UpdateSong() {
        $response = $this->client->request('POST', 'comp-333-hw3/index.php/song/update',[

            'id' => '3', // add two songs before adding this one
            'artist' => 'Remi Wolf',
            'song' => 'Photo ID',
            'rating' => '5' // rating is different in database
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testPost_DeleteSong(){
        $response = $this->client->request('POST', 'comp-333-hw3/index.php/song/delete',[
            'id' => 4
        ]);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function tearDown() : void{
        parent::tearDown();
        $this->client = null;
    }
}

?>