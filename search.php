<!DOCTYPE html>
<html>
    
<body>

<p><a href="http://lyricsentiment.web.engr.illinois.edu/">Back to the Home Page</a></p>


<?php

	$link = mysql_connect('localhost', 'lyricsentiment_cs410', 'cs410');
	if (!$link) {
		die('Could not connect: ' . mysql_error());
	}
	mysql_select_db('lyricsentiment_song');


	$singer=$_POST["singer_name"];
	$song=$_POST["song_name"];
	
	if (!empty($song)&&!empty($singer)){
		$sql = "SELECT * FROM Songs WHERE Song_NAME = '$song' AND Singer_NAME = '$singer'"; 
		$case = 1;	
	}else if(!empty($singer)){
		$sql = "SELECT * FROM Songs WHERE Singer_NAME = '$singer'";
		$case = 2;	
	}else if(!empty($song)){
		$sql = "SELECT * FROM Songs WHERE Song_NAME = '$song'";
		$case = 3;
	}else{
		$sql = "";
	}
	
	$res = mysql_query($sql);

	print("<table width=\"100%\" border=\"1\" cellpadding=\"10\"> 
		<tr>
			<td  align=\"center\">
			<h1>Setiment Analysis Results</h1>
			
			
			</td>
		</tr> ");
		
	
	print("<tr>
			<td align=\"center\"> ");
			
            
			if (mysql_num_rows($res)>0)
			{
				
				print("<h2> 
			        <span style=\"color:red;\"> red is positive </span>             
			        <span style=\"color:green;\"> green is negative </span>
                </h2>");
                
				if($case == 1 || $case == 3){
				    while($data=mysql_fetch_assoc($res))
				    {
				        print("<br>");
				        
					    print("<b><p>Song:</b> {$data['Song_NAME']}</p>");
					    if($data['Song_Score'] > 0){
					        print("<p><b>Song Score:</b> <span style=\"color:red;\">{$data['Song_Score']}</span></p>");
					    }else{
					        print("<p><b>Song Score:</b> <span style=\"color:green;\">{$data['Song_Score']}</span></p>");
					    }
		
					    print("<b><p>Lyrics:</b> {$data['Lyrics']}</p><br/>");

                        print("<p><b>Singer:</b> {$data['Singer_NAME']}</p>");
                        if($data['Singer_Score'] > 0){
					        print("<p><b>Singer Score: </b> <span style=\"color:red;\">{$data['Singer_Score']}</span></p><br/>");
					    }else{
					        print("<p><b>Song Score: </b> <span style=\"color:green;\">{$data['Song_Score']}</span></p><br/>");
					    }
					   
                        print("<br>");
				    }
				}else if($case == 2){
				    print("<br>");
				    
				    $data=mysql_fetch_assoc($res);
				     print("<p><b>Singer:</b> {$data['Singer_NAME']}</p>");
                        if($data['Singer_Score'] > 0){
					        print("<p><b>Singer Score: </b> <span style=\"color:red;\">{$data['Singer_Score']}</span></p><br/>");
					    }else{
					        print("<p><b>Singer Score: </b> <span style=\"color:green;\">{$data['Singer_Score']}</span></p><br/>");
					    }
					
					print("<p style=\"color:blue;\">There are " . mysql_num_rows($res) . " song(s) available</p>");
					
					while($data=mysql_fetch_assoc($res))
				    {
				        
					    print("<b><p>Song:</b> {$data['Song_NAME']}</p>");
					    if($data['Song_Score'] > 0){
					        print("<p><b>Song Score:</b> <span style=\"color:red;\">{$data['Song_Score']}</span></p>");
					    }else{
					        print("<p><b>Song Score:</b> <span style=\"color:green;\">{$data['Song_Score']}</span></p>");
					    }
					    print("<b><p>Lyrics:</b> {$data['Lyrics']}</p><br/>");
					    
					    print("<br>");
				
				    }
				}
				
			    print("<br>");
	
			}
			else
			{
				print("There is no singer/song found with your current search criterion.");
			}
			
		
			print("</td>
		</tr>
		
	</table> ");

?>

</body>
</html>
