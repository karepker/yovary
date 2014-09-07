
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Take Yo' Birth Control</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/cover.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/bootstrap-clockpicker.min.css">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="js/ie-emulation-modes-warning.js"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <!--here there be dragons-->
    <script type="text/javascript" src="js/bootstrap-timepicker.min.js"></script>


    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="site-wrapper">

      <!---<div class="site-wrapper-inner">-->

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              <div id="yo-button"></div>
              <ul class="nav masthead-nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#">Contact</a></li>
              </ul>
            </div>
          </div>
          <img src="pix\YovaryWhite.png" style="max-width:100%;">
          <div class="inner cover">
            <h1 class="cover-heading">Never fret.<i> Period</i>.</h1>
            <form role="form">
			  <div class="form-group">
			    <!--<label for="exampleInputEmail1">Yo Handle</label> -->
			    <input type="text" class="form-control" placeholder="Yo Handle">
			  </div>
			  <div class="input-group clockpicker">
			      <!--<input type="text" class="form-control" value="09:00">-->
            <input type="text" class="form-control" value="Notification Time">
			      <span class="input-group-addon">
			          <span class="glyphicon glyphicon-time"></span>
			      </span>
			  </div>
			    <script type="text/javascript" src="js/bootstrap-clockpicker.min.js"></script>
				<script type="text/javascript">
				    $('.clockpicker').clockpicker();
				</script>

			  <div class="checkbox">
			  </div>
			  <button type="submit" class="btn btn-default">Submit</button>
			</form>
      <!--</div>-->




        </div>

      </div>

    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/docs.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="js/ie10-viewport-bug-workaround.js"></script>
    <script type="text/javascript">
      var _yoData = {
        "username": "YOVARY",
        "trigger": "When they need tot ake birth control"
      };
      var s = document.createElement("script");
      s.type = "text/javascript";
      s.src = "//yoapp.s3.amazonaws.com/js/yo-button.js";
      (document.head || document.getElementsByTagName("head")[0]).appendChild(s);
    </script>
  </body>
</html>
