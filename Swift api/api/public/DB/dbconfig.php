<?php 
require_once __DIR__ .'/DB.php';
class DB {
    private $conn;

    function _construct(){
    }

    function connect(){
        
        $db_name = DB_NAME;
        $user = USER;
        $pass = PASS;
        $host = HOST;
        
        try{
            $this->conn = new PDO("mysql:host=$host;dbname=$db_name",$user,$pass);
            // $this->conn->setAttribue(PDO::SET_DEFAULT_FETCH_ATTR,)
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        }catch(PDOExecption $e){
            echo "Connection failed " . $e->getMessage();
        }

        return $this->conn;
    }
}

?>