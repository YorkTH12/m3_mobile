<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "db_library";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Error". $conn->connect_error);
    }
?>