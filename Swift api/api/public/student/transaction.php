<?php 

$app->group('/v1', function () use ($app) {
    $app->group('/clients', function () use ($app){
        $app->post('/login', function ($request, $response, $args) {
            $swift =  new Auth();
            $data = $request->getParsedBody();

            $response = $swift->login($data['username'],$data['password']);
            return json_encode($response);
        });

        $app->post('/add_transac',function ($request,$response, $args){
            $swift =  new CRUD();
            $data = $request->getParsedBody();

            $response = $swift->makeDeposit($data);
            return json_encode($response);
        });

        $app->post('/transfer',function ($request,$response, $args){
            $swift =  new CRUD();
            $data = $request->getParsedBody();

            $response = $swift->makeTransfer($data);
            return json_encode($response);
        });

        $app->post('/get_transfer',function ($request,$response, $args){
            $swift =  new CRUD();
            $data = $request->getParsedBody();

            $response = $swift->getAllTransfers($data);
            return json_encode($response);
        }); 
    });
});


?>