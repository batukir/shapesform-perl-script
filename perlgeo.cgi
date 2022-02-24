#! /bin/perl -w

# perlgeo.cgi - show a form and do simple calculations

use strict;
use CGI qw(:param);  # only using library to get parameters

my $qs = $ENV{QUERY_STRING};
$qs =~ s/&/&amp;/;
my $pic_src = "./perlgeopic.cgi?" . $qs;

print "Content-type: text/html\n\n";

# stole this from 'template.html'
print '
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <title>
    Perl Geometry Calculator
  </title>
  <meta charset="utf-8" />
  <meta name="Author" content="Darren Provine" />
  <meta name="generator" content="Perl" />
  <style>
    a { text-decoration: none; }
    a:hover { text-decoration: underline; }
    fieldset { width: 400px }
    button {
    white-space: nowrap;
    text-align: center;
  </style>
</head>
';

print '
<p>
         <fieldset>
         <legend>Shapes</legend>
         <form method="get" action="./perlgeopic.cgi">
            <table>
               <tr>
                  <td>
                     <input type="radio" name="shape"
                        id="circle" value="circle"
                        title="circle"/>
                  </td>
                  <td>
                     <label for="circle">Circle</label>
                  </td>
                  <td>
                     <label for="height2d">Height</label>
                  </td>
                  <td>
                     <input type="number" id="height2d"
                        name="height2d" title="height2d" />
                  </td>
               </tr>
               <tr>
                  <td>
                     <input type="radio" name="shape"
                        id="rectangle" value="rectangle"
                        title="rectangle"/>
                  </td>
                  <td>       
                     <label for="rectangle">Rectangle</label>   
                  </td>
                  <td>
                     <label for="width2d">Width</label> 
                  </td>
                  <td>
                     <input type="number" id="width2d"
                        name="width2d" title="width2d" />
                  </td>
               </tr>
               <tr>
                  <td>
                     <input type="radio" name="shape"
                        id="triangle" value="triangle"
                        title="triangle"/>
                  </td>
                  <td>
                     <label for="triangle">Triangle</label>  
                  </td>
                  <td>
                     <label for="radius2d">Radius</label> 
                  </td>
                  <td>
                     <input type="number" id="radius2d"
                        name="radius2d" title="radius2d" />
                  </td>
               </tr>
                <tr>
                  <td>
                     <input type="checkbox" id="rightTriangle" name="rightTriangle"/>
                  </td>
                  <td>
                     <label for="rightTriangle">Right Triangle?</label> 
                  </td>
                  <td></td>
                  <td></td>
                  <td></td>
               </tr>
               <tr>
                  <td>
                     <input type="checkbox" id="area2d" name="area2d"/>
                  </td>
                  <td>
                     <label for="area2d">Area</label> 
                  </td>
                  <td></td>
                  <td></td>
               </tr>
               <tr>
                  <td>
                     <input type="checkbox" id="perimeter" name="perimeter"/>
                  </td>
                  <td>
                     <label for="perimeter">Perimeter</label>   
                  </td>
                  <td></td>
                  <td>
                  <input type="submit" name=".submit" />
                  </td>
               </tr>
            </table>
            </form>
         </fieldset>
</p>

<p>
  <img src="$pic_src"
       style="border: 2px solid black;"
       alt="drawing" />
</p>
', "\n";

# stole this from 'template.html', too
print '
<footer style="border-top: 1px solid blue">
 <a href="http://elvis.rowan.edu/~kilroy/"
    title="Link to my home page">
    D. Provine
 </a>

<span style="float: right;">
<a href="http://validator.w3.org/check/referer">HTML5</a> /
<a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
    CSS3 </a>
</span>
</footer>

</body>
</html>
';

