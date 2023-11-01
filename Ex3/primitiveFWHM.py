def fwhm(image, xStart, yStart):
    max = np.max(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == max:
                centre = [i,j]
   
    xPosBottomHalf = centre[0]
    xPosTopHalf = centre[0]
    yPosBottomHalf = centre[1]
    yPosTopHalf = centre[1]
    
    for i in range(len(image)):
        if np.abs(max*0.5 - image[centre[0]][i]) < max*0.5 - image[centre[0]][xPosBottomHalf]:
            if xPosBottomHalf <= centre[0]:
                xPosBottomHalf = i
    for i in range(len(image)):
        if image[centre[0]][i] - max*0.5 < image[centre[0]][xPosTopHalf]- max*0.5:
            if xPosTopHalf >= centre[0]:
                xPosTopHalf = i
    xHalfBottom = [centre[0], xPosBottomHalf]
    xHalfTop = [centre[0], xPosTopHalf]
    
    for i in range(len(image[0])):
        if np.abs(max*0.5 - image[i][centre[1]]) < np.abs(max*0.5 - image[yPosBottomHalf][centre[1]]):
            if yPosBottomHalf <= centre[1]:
                yPosBottomHalf = i
    for i in range(len(image[0])):
        if np.abs(max*0.5 - image[i][centre[1]]) < np.abs(max*0.5 - image[yPosTopHalf][centre[1]]):
            if yPosTopHalf >= centre[1]:
                yPosTopHalf = i
    print('centre : ',centre)
    print('xHalfBottom : ',xHalfBottom)
    print('xHalfTop : ',xHalfTop)
    # print('yPosHalfBottom : ',yPosHalfBottom)
    # print('yPosHalfTop : ',yPosHalfTop)
    centreTranslate = [centre[0] + xStart, centre[1] + yStart]