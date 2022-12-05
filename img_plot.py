# 본 파일은 테스트img와 출력이 나온 img를 동시에 볼수 있도록 plot 시키는 code 입니다.
# 필요한 모듈 import
import glob
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


def data_save(origin, path0, path1, path2, save_point):
    # 원본사진 경로
    origin_img = origin

    # img1 path
    img1_path = path0

    # img2 path
    img2_path = path1

    # img3 path
    img3_path = path2

    fig = plt.figure()
    file0_name = glob.glob(os.path.join(origin_img, '*jpg'))
    file1_name = glob.glob(os.path.join(img1_path, '*jpg'))
    file2_name = glob.glob(os.path.join(img2_path, '*jpg'))
    file3_name = glob.glob(os.path.join(img3_path, '*jpg'))


    for i, (x, y, z, w) in enumerate(zip(file0_name, file1_name, file2_name,file3_name)):
        img0 = cv2.imread(x, cv2.IMREAD_UNCHANGED)
        img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)

        img1 = cv2.imread(y, cv2.IMREAD_UNCHANGED)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

        img2 = cv2.imread(z, cv2.IMREAD_UNCHANGED)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        img3 = cv2.imread(w, cv2.IMREAD_UNCHANGED)
        img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

        images = [img0, img1, img2, img3]

        titles = ['origin',
                  '1024',
                  '1028',
                  '1280']

        for j in range(4):
            plt.subplot(2, 2, j + 1)
            if j < 2:
                plt.imshow(images[j])
            else:
                plt.imshow(images[j], cmap='gray')
            plt.title(titles[j])
            plt.xticks([]), plt.yticks([])

            plt.tight_layout()
            # plt.show()

            result_dir = save_point
            if not os.path.exists(result_dir):
                os.makedirs(result_dir)
            # print(result_dir, str(i))
            plt.savefig(result_dir + 'results (' + str(i) + ').png')
            # plt.cla()
            # plt.close()

    cv2.waitKey(0)

if __name__ == '__main__':
    origin_path = 'data/ng_1280/test/images/'
    path0 = 'runs/detect/1024_1280/'
    path1 = 'runs/detect/1028_1280/'
    path2 = 'runs/detect/1280_te/'
    save_points = 'runs/detect/results/'
    if not os.path.exists(save_points):
        os.makedirs(save_points)
    # print(save_points)

    data_save(origin_path, path0, path1, path2, save_points)


