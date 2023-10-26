<?php

@include 'config.php';

session_start();



if(!isset($_SESSION['admin_name'])){
   header('location:login_form.php');
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>admin page</title>

   <!-- custom css file link  -->
   <link rel="stylesheet" href="css/style.css">

</head>
<body>
   
<div class="container" >

   <div class="content">
   <h1>CMS</h1><h3><span>ADMIN PAGE</span></h3>
      <h3> <?php echo $_SESSION['admin_name'] ?></h3>     
   <p></p>
      <div class="content">
      <a href="" class="btn">Users Setting</a>
      <a href="" class="btn">Setting</a>
      <a href="" class="btn">Discussion Room</a>
      </div>
      <div class="content">
      <img src="img/admin.png" width="300"
     height="450">
      </div>
	    <div class="content">
       <a href="logout.php" class="btn">logout</a>
      </div>
   </div>
   <p></p>

   
</div>

</body>
</html>