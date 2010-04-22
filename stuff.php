<?php

if(!isset($argv[1])) die("Use event as parameter!");
$event = $argv[1];
// now try to make sense of it.
$event = (int) preg_replace('/[^0-9]+/', '', $event);

if(!isset($argv[2])) die("User data.csv as second parameter!");
$data = $argv[2];

echo '<html>
<head>
<title>WWP Stats, '.sprintf("%04d", $event).' Equipment HTML</title>
<script src="http://beta.timhatch.com/mint/?js" type="text/javascript"></script>
</head>
<body>
';

$f = fopen($data, "rb") or die("Can't open csv");
fgets($f, 4096); //junk the header line
$cameras = array();
$lenses = array();
$panohead = array();
$tripod = array();
$software = array();

while($row = fgetcsv($f, 4096)) {
    if(count($row) > 5 && $row[2] != "") {
        if(!isset($cameras[$row[1]])) $cameras[$row[1]] = array();
        $cameras[$row[1]][] = $row[0];
        if(!isset($cameras[$row[1]])) $lenses[$row[2]] = array();
        $lenses[$row[2]][] = $row[0];
        if(!isset($cameras[$row[1]])) $panohead[$row[3]] = array();
        $panohead[$row[3]][] = $row[0];
        if(!isset($cameras[$row[1]])) $tripod[$row[4]] = array();
        $tripod[$row[4]][] = $row[0];
        if(!isset($cameras[$row[1]])) $software[$row[5]] = array();
        $software[$row[5]][] = $row[0];
    }
}
arsort($cameras);
arsort($lenses);
arsort($panohead);
arsort($tripod);
arsort($software);

doit("Cameras", $cameras);
doit("Lenses", $lenses);
doit("Panoheads", $panohead);
doit("Tripods", $tripod);
doit("Software", $software);

function doit($a, $b) {
    global $event;
    echo "<h3 id=\"{$a}\"><a href=\"#{$a}\">{$a}</a></h3>\n";
    echo "<table border>\n";
    foreach($b as $k=>$v) {
        //if($v==1) break;
        $s = count($v);
        $links = array();
        foreach($v as $i) {
            $links[] = "<a href=\"http://worldwidepanorama.org/worldwidepanorama/wwp{$event}/html/{$i}.html\">{$i}</a>";
        }
        $links = implode(", ", $links);
        echo "  <tr><td>{$k}</td><td>{$s}</td><td>{$links}</td></tr>\n";
    }
    echo "</table>\n\n";
}

echo '</body></html>';
