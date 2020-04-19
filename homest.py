
#!/usr/bin/env python

import cv2
import numpy as np

if __name__ == '__main__' :

    # Read source image.
    im_src    = cv2.imread('267.jpg')
    im_circle = cv2.imread('267_output_circle.jpg')

    # Four corners of source image
    pts_src = np.array([[315,30], [578, 32], [847, 468],[1, 436]])
    # Four corners with a sort of rectangular bird view
    pts_dst = np.array([[0,65], [828, 65], [828, 478],[0, 478]])

    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
    
    # Apply homography
    im_out = cv2.warpPerspective(im_src, h, (im_src.shape[1],im_src.shape[0]))

    # Apply inverse homography to check effect on circle
    im_circle_out = cv2.warpPerspective(im_circle, np.linalg.inv(h), (im_src.shape[1],im_src.shape[0]))
    #transformed = cv2.perspectiveTransform(points, homography)

    # Display images
    cv2.imshow("Orinal Image", im_src)
    cv2.imshow("Forward homography Image", im_out)
    cv2.imshow("Circle", im_circle)
    cv2.imshow("Inverse homography Image", im_circle_out)

    cv2.imwrite('267_output.jpg',im_out)

    cv2.waitKey(0)
