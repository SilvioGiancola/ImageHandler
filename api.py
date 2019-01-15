import cv2
import numpy as np


def detectSeeds(image):
    ret, maskR = cv2.threshold(
        image[:, :, 0], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    ret, maskG = cv2.threshold(
        image[:, :, 1], 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    ret, maskB = cv2.threshold(
        image[:, :, 2], 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    mask = cv2.bitwise_and(maskR, maskB)

    # Find Contours
    im2, contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter Contours based on geometrical features
    good_cnt = []
    for cnt in contours:
        if cv2.contourArea(cnt) < 1000:
            continue
        if cv2.contourArea(cnt) > 100000:
            continue
        if cv2.arcLength(cnt, False) > 2000.0:
            continue
        if (cv2.arcLength(cnt, False) / cv2.contourArea(cnt)) > 0.2:
            continue
        good_cnt.append(cnt)

    # Overlap the image and the mask
    redImg = np.zeros(image.shape, image.dtype)
    redImg[:, :] = (255, 0, 0)
    redMask = cv2.bitwise_and(redImg, redImg, mask=mask)
    cv2.addWeighted(redMask, 1, image, 1, 0, image)
    # Draw contours on image
    cv2.drawContours(image, good_cnt, -1, (0, 255, 0), 3)
    # Plot results
    print(f"{len(good_cnt)} seeds found")

    return image, good_cnt


def classifySeeds(image):
    _, good_cnt = detectSeeds(image)

    cv2.drawContours(image, good_cnt, -1, (0, 255, 0), 3)

    bbs = [cv2.boundingRect(cnt) for cnt in good_cnt]
    areas = [bb[2] * bb[3] for bb in bbs]
    min_area = np.min(areas) * 3
    geminated = 0
    for cnt in good_cnt:
        x, y, w, h = cv2.boundingRect(cnt)
        if (w * h > min_area):
            geminated = geminated + 1
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 4)
        else:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 4)

    print(f"{len(good_cnt)} seeds found")
    print(f"  -> {geminated} geminated (red)")
    print(f"  -> {len(good_cnt) - geminated} non-geminated (blue)")
    return image
