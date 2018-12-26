<?php 
    class Utility
    {
        protected $conn;
        public function __construct(){
            require_once __DIR__ . '/DB/dbconfig.php';
            $db = new DB();
            $this->conn = $db->connect();
        }

        public function check_ref_no($refrence_no){
            try{
                $stmt = $this->conn->prepare("SELECT * FROM `transactions` WHERE refrence_no = :refrence_no");
                $stmt->execute([':refrence_no' => $refrence_no]);
                $res = $stmt->fetchAll(PDO::FETCH_ASSOC);
                if($stmt->rowCount() > 0){
                     return true;
                }else{
                    return false;
                }
            } catch(PDOException $ex){
                return NULL;
            }
        }

        public function clean($in){
            $res = stripslashes($in);
            $res = trim($res);
            return $res;
        }

        public function isExistEmail($email) {
            try {
                $stmt = $this->conn->prepare("SELECT * FROM transactions WHERE email = :email");
                $stmt->execute(array(':email' => $email));
                $res = $stmt->fetch(PDO::FETCH_ASSOC);
                if($stmt->rowCount() > 0){
                     return true;
                }else{
                    return false;
                }
            } catch(PDOException $ex) {
                return NULL;
            }
        }

        public function isExistUser($regno) {
            try {
                $stmt = $this->conn->prepare("SELECT * FROM `users` WHERE reg_no = :regno LIMIT 1");
                $stmt->execute(array(':regno' => $regno));
                $res = $stmt->fetch(PDO::FETCH_ASSOC);
                if($stmt->rowCount() > 0){
                     return true;
                }else{
                    return false;
                }
            } catch(PDOException $ex) {
                return NULL;
            }
        }

        public function redirect($location) {
            header("Location:$location");
        }
    }
    class Auth extends Utility{
        function __construct(){
            parent::__construct();
        }

        public function hashpass($pass){
            return password_hash($pass, PASSWORD_BCRYPT);
        }

        public function verifypass($pass,$hash){
            if(password_verify($pass,$hash)){
                return TRUE;
            }else{
                return FALSE;
            }
        }

        public function login($username,$password){
            $response = array();
            try{
                $stmt = $this->conn->prepare("SELECT * FROM `users` WHERE username = :username LIMIT 1");
                $stmt->execute([':username' => $this->clean($username)]);
                $res = $stmt->fetch(PDO::FETCH_ASSOC);
                if($stmt->rowCount() == 1){
                    if($this->verifypass($this->clean($password),$res['password'])){
                        session_start();
                        $response['status'] = 200;
                        $response['message'] = 'Login Successful';
                        $response['data'] = $res;
                        return $response;
                    }else{
                        $response['message'] = 'Invalid Password';
                        $response['status'] = 400;
                        $response['data'] = "";
                        return $response;
                    }
                }else{
                    $response['message'] = 'Invalid Username';
                    $response['status'] = 400;
                        $response['data'] = "";
                    return $response;
                }
            } catch(PDOException $e){
                return NUll;
            }
        }

        public function logout(){
            session_unset();
            session_destroy();
            // $this->redirect('index.php');
        }
    }

    class CRUD extends Utility {
        function __construct(){
            parent::__construct();
        }

        // public function makeDeposit($req){
        //     $response = array();

        //     $amount = $this->clean($response['amount']);
        //     $recipient_id = $this->clean($response['recipient_id']);

        //     $stmt = $this->conn->prepare("INSERT INTO `transactions` (amount, recipient_id) VALUES (:amount, :recipient_id)");
            
        //     if($this->isExistUser($recipient_id)){
        //         if($stmt->execute([':amount' => $amount, ':recipient_id' => $recipient_id])){
        //             $response['status'] = 200;
        //             // $response['data'] = $res;
        //             $response['message'] = "Deposit Successful";
        //         }else{
        //             $response['status'] = 400;
        //             // $response['data'] = $res;
        //             $response['message'] = "Deposit Not Successful";
        //         }
        //     }else{
        //         $response['status'] = 400;
        //             // $response['data'] = $res;
        //         $response['message'] = "Invalid User";
        //     }
        // }

        public function getAllTransfers($req){
            $response = array();

            $regno = $this->clean($req['regno']);

            $stmt = $this->conn->prepare("SELECT * FROM `transfers` WHERE senders_regno = :regno ORDER BY date_created DESC");
            $stmt->execute([":regno" => $regno]);

            $res = $stmt->fetchAll(PDO::FETCH_ASSOC);

            if($stmt->rowCount() > 0){
                $response['status'] = 200;
                $response['data'] = $res;
                return $response;
            }else{
                $response['message'] = 'No Record';
                $response['status'] = 200;
                $response['data'] = "";
                return $response;
            }
        }
        
        // public function getAllDeposit($req){
        //     $response = array();

        //     $regno = $this->clean($req['regno']);

        //     $stmt = $this->conn->prepare("SELECT * FROM `tran` WHERE senders_regno = :regno ORDER BY date_created DESC");
        //     $stmt->execute([":regno" => $regno]);

        //     $res = $stmt->fetchAll(PDO::FETCH_ASSOC);

        //     if($stmt->rowCount() > 0){
        //         $response['status'] = 200;
        //         $response['data'] = $res;
        //         return $response;
        //     }else{
        //         $response['message'] = 'No Record';
        //         $response['status'] = 200;
        //         $response['data'] = "";
        //         return $response;
        //     }
        // }

        public function makeTransfer($req){
            $response = array();

            $amount = $this->clean($req['amount']);
            $recipient_regno = $this->clean($req['recipient_regno']);
            $senders_regno = $this->clean($req['senders_regno']);
            
            if(!$this->isExistUser($recipient_regno)){
                $response['status'] = 400;
                $response['message'] = "Invalid Recipient";
                return $response;
            }
            if(!$this->isExistUser($senders_regno)){
                $response['status'] = 400;
                $response['message'] = "Invalid Senders Regno";
                return $response;
            }

            $stmt = $this->conn->prepare("SELECT `balance` from `users` WHERE reg_no = :regno");
            $stmt->execute([":regno" => $senders_regno]);

            $res = $stmt->fetch(PDO::FETCH_ASSOC);

            if($stmt->rowCount() == 1){
                if($res['balance'] >= $amount){
                    $status = 0;
                    //0 means none...not added to recipient and not removed from sender
                    //1 means money removed from sender but hasnt been added to recipient balance,
                    //2 means money removed from sender and also added to recipient balance,
                    //3 means when it was either a 0,1 then it would be rolled back...

                    $stmt = $this->conn->prepare("UPDATE `users` SET `balance` = users.balance - :amount WHERE reg_no = :regno");
                    if($stmt->execute([":amount" => $amount,":regno" => $senders_regno])){
                        $status = 1;
                        $stmt = $this->conn->prepare("UPDATE `users` set balance = users.balance + :amount where reg_no = :regno");
                        if($stmt->execute([":amount" => $amount,":regno" => $recipient_regno])){
                            $status = 2;
                        }else{
                            $response['status'] = 400;
                            $response['message'] = "pending";
                            return $response;
                        }
                    }else{
                        $response['status'] = 400;
                        $response['message'] = "Pending";
                        return $response;
                    }

                    $stmt = $this->conn->prepare("INSERT INTO `transfers` (amount, status, senders_regno, recipient_regno) VALUES (:amount, :status, :senders_regno,:recipient_regno)");
                    if($stmt->execute([":amount" => $amount, ":status" => $status,":senders_regno" => $senders_regno,":recipient_regno" => $recipient_regno])){
                        $response['status'] = 200;
                        $response['message'] = "Transfer successful";
                        return $response;
                    }else{
                        $response['status'] = 400;
                        $response['message'] = "Error in making transfer";
                        return $response;
                    }
                }else{
                    $response['status'] = 400;
                    $response['message'] = "Insufficient Balance";
                    return $response;
                }
            }

        }

        
    }
    
    

?>