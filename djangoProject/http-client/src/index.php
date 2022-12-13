<html>
<head>
    <title>App page</title>
</head>
<body>
    <h2>Function-replace</h2>
    <h3>Замена выражения с й на и</h3>
    <?php
    if (isset($_POST['my_word'])){
        $myCurl = curl_init();
    curl_setopt_array($myCurl, array(
        CURLOPT_URL => 'http://nginxserver/api/'.$_POST['my_word'],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
    ));
    $response = curl_exec($myCurl);
    $return= curl_exec($myCurl);
    curl_close($myCurl);

    echo "Ответ на Ваш запрос: ".$response;
    }
    ?>
    <form action="index.php" method="post">
    <label for="text">Вводимое слово </label>
    <input type="text" name="my_word" id="my_word" required>
    <input type="submit" value="RUN!">
</body>
</html>