
#!/usr/bin/env python

import cv2
import numpy as np

if __name__ == '__main__' :

    # Read source image.
    im_src = cv2.imread('267.jpg')
    # Four corners of source image
    pts_src = np.array([[289,65], [620, 51], [853, 478],[1, 476]])

    # Four corners with a sort of rectangular bird view
    pts_dst = np.array([[0,65], [828, 65], [853, 478],[1, 476]])

    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
    
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_src.shape[1],im_src.shape[0]))
    
    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Warped Source Image", im_out)

    cv2.waitKey(0)
