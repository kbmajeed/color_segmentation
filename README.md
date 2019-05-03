# Color Segmentation for Body Tones

## Introduction
<p style="text-align: justify">
An image is converted to the HSV color space for color based segmentation. The body tones can be used for tracking and AR applications. </p>

## Description
This simple color segmentation approach is as follows:
```
ImageHSV <- ImageRGB
Segment ImageHSV using H-S-V ranges
Return output
```
![](mitt_hsv51.png)


## Results
The GIF below shows the application of the algorithm on a video:
![](Mitt_hand_hsv_gif.gif)
