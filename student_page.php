<?php

@include 'config.php';

session_start();

if(!isset($_SESSION['student_name'])){
   header('location:login_form.php');
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Student page</title>

   <!-- custom css file link  -->
   <link rel="stylesheet" href="css/style.css">

</head>
<body>
   

<div class="container" >

   <div class="content">
   <h1>CMS</h1><h3><span>STUDENT PAGE</span></h3>
      <h3> <?php echo $_SESSION['student_name'] ?></h3>     
   <p></p>
      <div class="content">
      <a href="" class="btn">Courses Page</a>
      <a href="" class="btn">Setting</a>
	  <a href="" class="btn">Discussion Room</a>
	  <a href="" class="btn">Badges</a>
	  </div>
      <div class="content">
      <img src="img/student.png" width="300"
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