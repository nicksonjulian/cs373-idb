document.write('\
	<!-- Start of Navbar-->\
	<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\
		<div class="container">\
\
		<!-- Navbar Title -->\
		<div class="navbar-header">\
			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\
            <span class="sr-only">Toggle navigation</span>\
            <span class="icon-bar"></span>\
            <span class="icon-bar"></span>\
            <span class="icon-bar"></span>\
          </button>\
			<a class="navbar-brand" href="http://ajhooper.pythonanywhere.com">Sochi 2014</a>\
		</div>\
\
		<!-- Navbar Links -->\
		<div class="collapse navbar-collapse">\
			<ul class="nav navbar-nav">\
\
				<!-- Navbar Link #1 -->\
				<li>\
					<a href="http://ajhooper.pythonanywhere.com/athlete/">Athletes</a>\
				</li>\
				<li>\
					<a href="http://ajhooper.pythonanywhere.com/country/">Countries</a>\
				</li>\
				<li>\
					<a href="http://ajhooper.pythonanywhere.com/event/">Events</a>\
				</li>\
				<li>\
					<a href="http://ajhooper.pythonanywhere.com/about/">About</a>\
				</li>\
				<li>\
					<a href="http://ajhooper.pythonanywhere.com/sponsor/">Sponsor</a>\
				</li>\
\
			<!-- Search bar -->\
			<form action="/search" method="get" class="navbar-form navbar-left">\
			<div class="form-group">\
                <input type="text" name="q">\
            </div>\
                <button type="submit" class="btn btn-default">Search</button>\
            </form>\
\
			<!-- End of Search bar -->\
\
		  </ul>\
		</div> <!-- Close Collapse -->\
	  </div> <!-- Close Container -->\
	</nav> <!-- End of Navbar -->\
');