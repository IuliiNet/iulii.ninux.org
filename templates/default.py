# Author:      Luca Postregna <luca.postregna@gmail.com>
# License:     MIT, see LICENSE for details

import os
import time, datetime

site_name = "iulii.net"
desc = "rete mesh libera e decentralizzata in friuli"
author = "lucapost"
src_dir = "src"
dst_dir = ""
prefix = "/"
home = "home"
path_separator = "/"
src_ext = {"markdown": "md", "textile": "tt", "plain": "txt"}
dst_ext = "html"
hidden = set(["404.md", "500.md", "search.md"])

current_time = datetime.datetime.now()
menu_code = ''

def menu(node):
	global menu_code

	menu_code = '\n'
	root = node
	while root.parent:
		root = root.parent
	menu_(root, node)
	return menu_code

def menu_(node, cur_node, node_prefix = prefix, indent = ''):
	global menu_code

	menu_code += indent + '<ul>\n'
	for child in sorted(node.children, key=lambda n: n.src_pathname):
		if child.dst_file.startswith("index.") or child.src_file in hidden:
			continue
		menu_code += indent + '<li class="level-' + str(child.level) + '"><a '
		if(child == cur_node
		or (cur_node.dst_file.startswith("index.") and child == cur_node.parent)):
			menu_code += 'class="current" '
		menu_code += 'href="' + node_prefix + child.dst_file
		if child.children:
			menu_code += "/index." + dst_ext + '">'	+ child.name + '</a>\n'
			menu_(child, cur_node, node_prefix + child.dst_file + '/', indent + '\t')
			menu_code += indent + '</li>\n'
		else:
			menu_code += '">'   + child.name + '</a></li>\n'
	menu_code += indent + '</ul>\n'

def header(node):
	"""Builds the header and returns it to a string."""
	
	return '''<!doctype html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
  		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>''' + site_name + ' | ' + node.name + '''</title>
  		<meta name="description" content="rete libera e decentralizzata in friuli">
  		<meta name="author" content="''' + author + '''" />
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="'''+ prefix +'''css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ prefix +'''css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ prefix +'''css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ prefix +'''css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ prefix +'''css/style.css" />
  		<script src="'''+ prefix +'''js/vendor/modernizr-2.5.3.min.js"></script>
		<link rel="icon" type="image/png" href="'''+ prefix +'''img/iuliinetlogo.png">
	</head>
	<body id="top">
		<div class="social">	
			<div class="tt-share">
				<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://iulii.net" data-text="rete mesh libera e decentralizzata in friuli #iuliinet #ninux" data-via="iuliinet" data-count="vertical">Tweet</a>
			</div>
			<div class="g-plusone" data-size="tall" data-href="http://iulii.net">
			</div><br/>
			<div class="fb-like" data-href="http://iulii.net" data-send="false" data-layout="box_count" data-width="60" data-show-faces="false" data-font="arial">
			</div>
		</div>
		<header class="container_12 clearfix">
			<div class="grid_8">
				<hgroup>
					<h1><a href="''' + prefix + '''">''' + site_name + '''</a></h1>
					<h2>''' + desc + '''</a></h2>
				</hgroup>
			</div>
			<div class="grid_4">
				<a href="''' + prefix + '''">
					<img class="iuliinetlogo" title="iuliinet logo" alt="iuliinet logo" src="'''+ prefix +'''img/iuliinetlogo.png">
				</a>
			</div>
			<div class="clear"></div>
		</header>
		<section class="container_12 clearfix">
			<article class="grid_8">
'''

def footer(node):
	"""Builds the footer and returns it to a string."""

	return '''
			</article>
			<div class="grid_4 column">
				<div class="path">
					<b>path</b>: %%%PATH%%%
				</div>
				<nav>
					''' + menu(node) + '''
				</nav>
				<a href="http://wiki.ninux.org" title="wiki ninux">
					<img src="''' + prefix + '''img/ninuxlogo.png" alt="logo ninux" title="logo ninux" class="banner"/>
				</a>
				<div class="tt-widget">
					<script charset="utf-8" src="http://widgets.twimg.com/j/2/widget.js"></script>
					<script>
					new TWTR.Widget({
					  version: 2,
					  type: 'profile',
					  rpp: 5,
					  interval: 30000,
					  width: 'auto',
					  height: 300,
					  theme: {
					    shell: {
					      background: '#55a2d5',
					      color: '#ffffff'
					    },
					    tweets: {
					      background: '#ffffff',
					      color: '#000000',
					      links: '#55a2d5'
					    }
					  },
					  features: {
					    scrollbar: false,
					    loop: false,
					    live: false,
					    behavior: 'all'
					  }
					}).render().setUser('iuliinet').start();
					</script>
				</div>
			</div>
			<div class="clear"></div>
		</section>
		<footer class="container_12 clearfix">
			<div class="grid_12">
				<a href="#top" title="back to top" class="backtotop">back to top<a>
				<div class="foot">
					<p>&copy; ''' + str(current_time.year) + ''' <a href="http://iulii.net" title="iulii.net website">iulii.net</a> | <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license CC by-nc</a> | edit: ''' + time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(node.src_pathname))) + '''</p>
				</div>
			</div>
			<div class="clear"></div>
		</footer>
	  	<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
	  	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
  		<script>window.jQuery || document.write('<script src="'''+ prefix +'''js/vendor/jquery-1.7.2.min.js"><\/script>')</script>
  		<script src="'''+ prefix +'''js/plugins.js"></script>
  		<script src="'''+ prefix +'''js/main.js"></script>
  		<script src="'''+ prefix +'''js/hashgrid.js"></script>
		<div id="fb-root"></div>
		<script>(function(d, s, id) {
		  var js, fjs = d.getElementsByTagName(s)[0];
		  if (d.getElementById(id)) return;
		  js = d.createElement(s); js.id = id;
		  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
		  fjs.parentNode.insertBefore(js, fjs);
		  }(document, 'script', 'facebook-jssdk'));
		</script>
		<script>
			!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");
		</script>
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
  		<script>
    			var _gaq=[['_setAccount','UA-6164762-12'],['_trackPageview']];
    			(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    			g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
    			s.parentNode.insertBefore(g,s)}(document,'script'));
  		</script>
</body>
</html>'''