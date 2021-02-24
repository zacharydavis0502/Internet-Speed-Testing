<!DOCTYPE html>

<html>
<head>
	<title>Internet Speedtest Table</title>
	<style type = "text/css">
		body {
			background-color: #2c2f33;
		
		}
		
		table {
			border-collapse: collapse;
			width: 100%;
			text-align: center;
		}
		
		table th {
			
			background-color: #7289da;
			border: 1px solid #7289da;
			color: #FFF;
			padding: 8px 4px 8px 4px;
		}
		
		table td {
			border: 1px solid #e3e3e3;
			padding: 4px 8px;
			background-color: #99aab5;
		}
		
		table tr:nth-child(odd) td {
			background-color: #ffffff;
		}
		
	</style>
</head>
<body>
<table>
	<tr>
		<th>Timestamp</th>
		<th>Ping (ms)</th>
		<th>Download Speed (Mbps)</th>
		<th>Upload Speed (Mbps)</th>
		<th>Host</th>
	</tr>
	<?php
	$conn = mysqli_connect("####", "####", "####", "####");
	if ($conn-> connect_error) {
		die("Connection failed:". $conn-> connect_error);
	}
	
	$sql = "SELECT TIME, PING, DOWN, UP, HOST from dataTable";
	$result = $conn -> query($sql);
	
	if($result-> num_rows > 0) {
		$inc = 0;
		while ($row = $result-> fetch_assoc()) {
			echo "<tr id = 'row_{$inc}'><td>". $row["TIME"] ."</td><td id = 'ping_{$inc}'>". $row["PING"] ."</td><td id = 'down_{$inc}'>". $row["DOWN"] ."</td><td id = 'up_{$inc}'>". $row["UP"] ."</td><td>". $row["HOST"] ."</td></tr>";
			$inc++;
		}
	}
	else {
		echo "Database Contains No Data";
	}
	
	$conn-> close();
	?>
</table>
</body>
</html>
	
