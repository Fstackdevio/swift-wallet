<?php

require './../vendor/autoload.php';

$app = new Slim\App();

//db connect
require __DIR__ . '/functions.php';

$app->get('/', function ($request, $response, $args) {
    $response->write("Welcome to Slim!");
    return $response;
});

//student transaction controller
require_once __DIR__ . '/student/transaction.php';


$app->run();
