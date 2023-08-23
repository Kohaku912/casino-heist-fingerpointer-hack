import cv2,keyboard
while True:
    if keyboard.is_pressed("Space"):
        def Judge_Matching(num):
            if 0.90 < num:
                return True
            else:
                return False
            
        camera = cv2.VideoCapture(1)
        re,img = camera.read()
        num = 1
        while num <= 4:
            fingerpoint = cv2.imread(f"tmp/fingerpoint{num}.png")
            result = cv2.matchTemplate(img, fingerpoint, cv2.TM_CCORR_NORMED)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
            Judg = Judge_Matching(maxVal)
            if Judg:
                i = 1
                while(i <= 4):
                    piece = cv2.imread(f"tmp/{num}-{i}.png")
                    result = cv2.matchTemplate(img, piece, cv2.TM_CCORR_NORMED)
                    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                    template_width = piece.shape[1]
                    template_height = piece.shape[0]
                    cv2.rectangle(img, maxLoc, (maxLoc[0] + template_width, maxLoc[1] + template_height), (0, 255, 0), -1)
                    i = i + 1
                break
            num = num + 1
        poslist = [[150,175],[150,220],[220,175],[220,220],[275,180],[275,215],[340,175],[340,225]]
        num = 1
        checked = 0
        while num <= 8:
            if checked >= 4:
                keyboard.press_and_release("Tab")
                print("完了！")
                break
            B,G,R = img[poslist[num-1][0],poslist[num-1][1],:]
            bgrstr = str(B) + str(G) + str(R)
            if bgrstr == "02550":
                keyboard.press_and_release("Return")
                print("選択！")
                if checked >= 3:
                    keyboard.press_and_release("Tab")
                    print("完了！")
                    break
                checked = checked + 1
            keyboard.press_and_release("Right")
            print("右！")
            num = num + 1