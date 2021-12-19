"""
This file holds some old code I used to print out location info.
Also it will color a small red bot at every location.
"""

print(q1['loc'])
print(sum(img[q1['loc']]))
img[q1['loc']] = [0,0,255]

print(q2['loc'])
print(sum(img[q2['loc']]))
img[q2['loc']] = [0,0,255]

print(q3['loc'])
print(sum(img[q3['loc']]))
img[q3['loc']] = [0,0,255]

print(q4['loc'])
print(sum(img[q4['loc']]))
img[q4['loc']] = [0,0,255]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()