#! /usr/bin/perl -w

# perlgeopic.cgi - draw a shape and label the sides

use strict;
use CGI;
use GD;
use CGI qw(:standard);
use Math::Trig;

my $query = new CGI;
my $shape = param("shape");
my $width = param("width2d");
my $height = param("height2d");
my $radius = param("radius2d");

my $areaChecked = param("area2d");
my $perimeterChecked = param("perimeter");
my $rightTriangleChecked = param("rightTriangle");
my $areaR = $width*$height;
my $perimeterR = 2*($height+$width);

my $areaC = ($radius**2)*pi();
my $perimeterC = 2*pi()*$radius;

my $areaT = ($height*$width)/2;
my $hypotenuse = sqrt(($height**2) + ($width**2));
my $perimeterT = $width+$height+$hypotenuse;
# Put out the content-type
print $query->header("image/png");

# Make a rectangular image
my $image = new GD::Image(400, 200);

# Set up some colors (RGB)
#
# NOTE: first color allocated becomes background color!

my $white = $image->colorAllocate(255, 255, 255);
my $black = $image->colorAllocate(  0,   0,   0);
my $red   = $image->colorAllocate(255,   0,   0);
my $green = $image->colorAllocate(  0, 255,   0);
my $blue  = $image->colorAllocate(  0,   0, 255);

# add some text
# shape is rectangle
if($shape eq "rectangle"){
  # scaling stuff
  if( ($width > 360 && $height > 150) && ($width == $height)){
    $image->filledRectangle(20, 40, 150, 150, $blue); #(x1, y1, x2, y2)
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Height: $height" ,       # string
              $black);   # color
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 20,    # start position
              "Width: $width" ,       # string
              $black);   # color
  }
    elsif(($width > 360 && $height > 150) && ($width > $height)){
    $image->filledRectangle(20, 40, 360+20, 150+40, $blue); #(x1, y1, x2, y2)
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Height: $height" ,       # string
              $black);   # color
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 20,    # start position
              "Width: $width" ,       # string
              $black);   # color
  }
  elsif(($width > 360 && $height > 150) && ($width < $height)){
    $image->filledRectangle(20, 40, 100, 180, $blue); #(x1, y1, x2, y2)
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Height: $height" ,       # string
              $black);   # color
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 20,    # start position
              "Width: $width" ,       # string
              $black);   # color
  }
  elsif($width > 360){
    $image->filledRectangle(20, 40, 360+20, $height+40, $blue); #(x1, y1, x2, y2)
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Width: $width" ,       # string
              $black);   # color
  }
  elsif($height > 150){
    $image->filledRectangle(20, 40, $width+20, 150+40, $blue); #(x1, y1, x2, y2)
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
          250, 10,    # start position
          "Height: $height" ,       # string
          $black);   # color
  }
  else {
    $image->filledRectangle(20, 40, $width+20, $height+40, $blue); #(x1, y1, x2, y2)
  }
  if($areaChecked){
  $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
               10, 10,    # start position
               "Area: $areaR" ,       # string
               $black);   # color
  }
  if($perimeterChecked){
  $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
               10, 20,    # start position
               "Perimeter: $perimeterR" ,       # string
               $black);   # color
  }
}

# shape is circle
if($shape eq "circle"){
  # scaling stuff
  if($radius > 170){
    $image->arc(180, 110, # center X, center Y,
              170, 170, # width, height,
              0, 360, # start/end angle (in degrees; 0 is to the right)
              $green);
    $image->fill(180,110,$green);

    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Radius: $radius" ,       # string
              $black);   # color  # color
  }
  else {
    $image->arc(180, 110, # center X, center Y,
              $radius, $radius, # width, height,
              0, 360, # start/end angle (in degrees; 0 is to the right)
              $green);
    $image->fill(180,110,$green);
  }

  
  if($areaChecked){
  $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
               10, 10,    # start position
               "Area: $areaC" ,       # string
               $black);   # color
  }
  if($perimeterChecked){
  $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
               10, 20,    # start position
               "Circumference: $perimeterC" ,       # string
               $black);   # color
  }
}

# shape is triangle 
if($shape eq "triangle"){
  if($rightTriangleChecked){
    if($perimeterChecked){
    $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
               10, 20,    # start position
               "Perimeter: $perimeterT" ,       # string
               $black);   # color
    }
    my $poly = new GD::Polygon;
    # scaling stuff
    if($width > 300 && $height > 150){
      $poly->addPt(90, 40); #A
      $poly->addPt(90 ,150+40); #B
      $poly->addPt(300+90, 150+40); #C
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Height: $height" ,       # string
              $black);   # color
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 20,    # start position
              "Width: $width" ,       # string
              $black);   # color
    }
    elsif($width > 300){
      $poly->addPt(90, 40); #A
      $poly->addPt(90 ,$height+40); #B
      $poly->addPt(300+90, $height+40); #C
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Width: $width" ,       # string
              $black);   # color
    }
    elsif($height > 150){
      $poly->addPt(90, 40); #A
      $poly->addPt(90 ,150+40); #B
      $poly->addPt($width+90, 150+40); #C
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
            250, 10,    # start position
            "Height: $height" ,       # string
            $black);   # color
    }
    else {
    $poly->addPt(90, 40); #A
    $poly->addPt(90 ,$height+40); #B
    $poly->addPt($width+90, $height+40); #C
    # draw the polygon, filling it with a color
    }
    $image->filledPolygon($poly,$black);
  }
  else {
    my $poly = new GD::Polygon;
    if($width > 300 && $height > 150){
      $poly->addPt(100, 40); #A
      $poly->addPt(90 ,150+40); #B
      $poly->addPt(300+90, 150+40); #C
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 10,    # start position
              "Height: $height" ,       # string
              $black);   # color
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
              250, 20,    # start position
              "Width: $width" ,       # string
              $black);   # color
    }
    elsif($width > 300){
      $poly->addPt(100, 40); #A
      $poly->addPt(90 ,$height+40); #B
      $poly->addPt(300+90, $height+40); #C
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
        250, 10,    # start position
        "Width: $width" ,       # string
        $black);   # color
    }
    elsif($height > 150){
      $poly->addPt(100, 40); #A
      $poly->addPt(90 ,150+40); #B
      $poly->addPt($width+90, 150+40); #C
      $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
            250, 10,    # start position
            "Height: $height" ,       # string
            $black);   # color
    }
    else {
      $poly->addPt(100, 40);
      # shift 90 to the right
      # shift 40 to the down
      $poly->addPt(90 ,$height+40);
      $poly->addPt($width+90, $height+40);
    }
    # draw the polygon, filling it with a color
    $image->filledPolygon($poly,$black);
  }
  if($areaChecked){
  $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
               10, 10,    # start position
               "Area: $areaT" ,       # string
               $black);   # color
  }
  if($perimeterChecked && !$rightTriangleChecked){
  $image->string(gdSmallFont, # or: gdLargeFont, gdMediumBoldFont, gdTinyFont
               10, 20,    # start position
               "Perimeter: Cannot be computed" ,       # string
               $black);   # color
  }
}

# Output the image to the browser
print $image->png;

