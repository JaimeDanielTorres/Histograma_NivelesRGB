#------ Torres - DDN MOox - API clasificacion --- Colores en imagen ---- 27/12/22 ---
#------------------------------------------------------------------------------------
#----------------------- Histograma de colores en imagen ----------------------------
#------------------------------------------------------------------------------------


from skimage import io
import matplotlib.pyplot as plt
image = io.imread('./Micrografias/S65.png')

_ = plt.hist(image.ravel(), bins = 256, color = 'orange', )
_ = plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
_ = plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
_ = plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
_ = plt.xlabel('Intensity Value')
_ = plt.ylabel('Count')
_ = plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
plt.show()

#cv2.waitKey(0)

