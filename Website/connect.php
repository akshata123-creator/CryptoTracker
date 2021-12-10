<?php
/*
$name=$_POST['name'];
$uname=$_POST['uname'];
$email=$_POST['email'];
$num=$_POST['num'];
$pass=$_POST['pass'];

$con = new mysqli('localhost','root','','project');
if($con->connect_error)
{
    die('connection failed : '.$con->connect_error);
}
else
{
    $stmt = $con->prepare("insert into details(name, uname, email, num, pass)values(?,?,?,?,?)");
    $stmt->bind_param("sssis",$name, $uname, $email, $num, $pass);
    $stmt->execute();
    header("Location: Aboutcrpy.html");
    $stmt->close();
    $con->close();
}
*/

$name=$_POST['name'];
$uname=$_POST['uname'];
$email=$_POST['email1'];
$num=$_POST['num'];
$pass=$_POST['pass1'];



$con = new mysqli('localhost','root','','project');
if($con->connect_error)
{
die('connection failed : '.$con->connect_error);
}
else
{
$query="select * from details where uname='$uname'";
$run=mysqli_query($con,$query);
if(mysqli_num_rows($run)>0)
{
echo"<script>alert('username already exists,please try another')</script>";
}

else
{
$stmt = $con->prepare("insert into details(name, uname, email, num, pass)values(?,?,?,?,?)");
$stmt->bind_param("sssis",$name, $uname, $email, $num, $pass);
$stmt->execute();
header("Location: Aboutcrpy.html");

$stmt->close();
$con->close();
}
}

?>