import cv2



img = cv2.imread(r"D:\vision01\images\photo.png")


if img is None:
    print("读取失败：图片路径不对，或者文件不存在")
else:

    print("图片尺寸：", img.shape)


    cv2.imshow("photo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    out_path=r"D:\vision01\images\photo.png"
    cv2.imwrite(out_path, img)
