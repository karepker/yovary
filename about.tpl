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

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="js/ie-emulation-modes-warning.js"></script>
    <script type="text/javascript" src="js/bootstrap-timepicker.min.js"></script>


    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="site-wrapper">
      <div class="cover-container">
        <div class="masthead clearfix">
          <div class="inner">
            <ul class="nav masthead-nav">
              <li><a href="/">Home</a></li>
              <li class="active"><a href="#">About</a></li>
            </ul>
          </div>
        </div>
        <img src="pix/YovaryWhite.png" style="max-width:100%;">
	    <p>Combining the ease of one-time sign up with Yo's simple push notifications, Yovary has your back when it comes to taking the pill. Registered Yo users can now receive friendly reminders, avoiding the hassle of alarms or calendar events.</p>
        <p>Have any questions? Feel free to reach out to us with feedback at <a href="mailto:contact@yovary.me">contact@yovary.me</a></p>
      </div>
    </div>
    <div id="yo-button"></div>

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
        "trigger": "When they need to take birth control"
      };
      var s = document.createElement("script");
      s.type = "text/javascript";
      s.src = "//yoapp.s3.amazonaws.com/js/yo-button.js";
      (document.head || document.getElementsByTagName("head")[0]).appendChild(s);
    </script>
  </body>
</html>
