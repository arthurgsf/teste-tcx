import cv2 as cv
import numpy as np

def preprocessing(img:np.ndarray) -> np.ndarray:
    """
    Recebe como entrada uma imagem e etorna uma nova imagem após:
    converter para escala de cinza, aplicar filtro de média 3x3 e aplicar thresholding.

    Parameters:
    img (np.ndarray): Imagem de entrada.

    Returns:
    np.ndarray: Imagem pré-processada.
    """
    new_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    new_img = cv.medianBlur(new_img, ksize=3)
    _, thresh = cv.threshold(new_img, 90, 255, cv.THRESH_BINARY)
    
    return thresh

if __name__ == "__main__":
    img = cv.imread("images/test.jpg", cv.IMREAD_UNCHANGED)
    new_img = preprocessing(img)

    cv.imshow("original", img)
    cv.imshow("preprocessada", new_img)
    cv.waitKey(0)
    cv.destroyAllWindows()