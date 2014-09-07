<!DOCTYPE html>
<html lang="en">
  <head>
	<meta charset="utf-8">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Yovary</title>
  </head>
  <body>
    % if success:
    <p>Successfully added yo for user {{username}} which will be sent {{duration}}
    minutes from now</p>
    % else:
    <p>Could not add yo for username {{username}}</p>
    % end
  </body>
</html>
