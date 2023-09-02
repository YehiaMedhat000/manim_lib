# Challenges

> Here are some of the problems in my manim code implementation in the following scenes.

## Important note

> **On each header you'll find a video link**

## [S_int_l scene](/challenges/S_int_l.mp4)

> Explains the integers numberline, the challenges in this scenes are:

1. I couldn't add the back tip to the line smoothly, it's created before the front tip, so, I was advised to make the line grow from center.

2. I couldn't make the last `<` sign disappear, **actually I can do it now.**

## [S_rat_l scene](/challenges/S_rat_l.mp4)

> Explains the rationals numberline, the challenges in this scene are:

1. I had the same tip's problem as in **S_int_l**.

2. I tried to zoom in onto a portion of the line to show how the numbers between each two numbers are infinite, but instead, I made several copies of the line to show on them some zoom-like effect.

3. I wanted the numbers to show up as fractions not decimals, **This is applicable by the `label_constructor` param,** but, I saw some people trying with it hard without the needed results

## [SR_Numline scene](/challenges/SR_Numline.mp4)

> Explains the Sign rule of with arrows on the numberline using some arrow.

1. I wanted to make the `DecimalNumber` above the arrow to shift a little bit to let in the `\times` sign and the multiplier, so they fit on the arrow.

2. I wanted to squish or `ReplacementTransform` the whole expression above it with only the result, and redo this process of putting an expression, changing the length and/ or direction of the arrow with replacing the expression with only one final digit.

3. What I tried is to try to `self.remove()`, `self.play(FadeOut())`, but not giving the described wanted result above.

## [CubeVolume scene](/challenges/CubeVolume.mp4)

> Explains the conversion from length to area to volume, or from 1D to 2D to 3D shapes

1. I wanted to text after rotating the frame (camera) to show go to the `DL` and then pull the other 4 on the `Arrow3D` mobject to get multiplied together.

2. I would like a more straight forward way to show the brace with the label more precisely in 3D.

## [SpheresCuboid scene](/challenges/SpheresCuboid.mp4)

### Uncomplete scene

> Explains a specific problem in a textbook about the ration between 3 spheres and the box that contains them.

1. I wanted to get the braces to completely be replaced with the bigger one, but, as it seems in the video that one of the braces wasn't replaced.
