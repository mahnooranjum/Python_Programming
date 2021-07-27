<?php
// PHP code goes here
$d = $_GET['input1'];
$s = $_GET['input2'];
$p = $_GET['input3'];

echo $d;
echo " ";
echo $s;
echo " ";
echo $p;
echo " ";
echo "Row Entry";


$dataRow = [
    'input1' => $d,
    'input2' => $s,
    'input3' => $p
];

$csvFile = 'C:/xampp/htdocs/myapp/data.csv';
$fp = fopen($csvFile, 'a');
fputcsv($fp, $dataRow);
fclose($fp);

?> 