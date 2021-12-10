<?php
$con = mysqli_connect("localhost","root","","project");
$response = array();
if($con){
    $sql = "select * from details";
    $result = mysqli_query($con,$sql);
    if($result){
        header("Content-Type: JSON");
        $i=0;
        while($row = mysqli_fetch_assoc($result)){
            $response[$i]['id'] = $row ['id'];
            $response[$i]['name'] = $row ['name'];
            $response[$i]['uname'] = $row ['uname'];
            $response[$i]['email'] = $row ['email'];
            $response[$i]['num'] = $row ['num'];
            $i++;
        }
        echo json_encode($response,JSON_PRETTY_PRINT);
    }
}
else{
    echo"Database connection failed";
}
?>