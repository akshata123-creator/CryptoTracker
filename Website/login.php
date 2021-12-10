<?php
$email=$_POST['em'];
$pass=$_POST['pa'];
    
$con = new mysqli("localhost","root","","project");
if($con->connect_error)
{
    die("Failed to Connect : ".$con->connect_error);
}
else
{
    $stmt = $con->prepare("select * from details where email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt_result = $stmt->get_result();
    if($stmt_result->num_rows > 0)
    {
        $data = $stmt_result->fetch_assoc();
        if($data['pass'] === $pass)
        {
            header("Location: Aboutcrpy.php");
        
        }
        else
        {
            header("Location:index.html");
        }
    }
    else
    {
        header("Location:index.html");
    }
}
?>
