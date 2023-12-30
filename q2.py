import cv2 as cv
import numpy as np

def quantization(img:np.ndarray) -> np.ndarray:
    """
    Aplica clusterização k-means para agrupar os pixels de cores similares.
    O resultado é uma imagem com 2 cores diferentes.

    Parameters:
    img (np.ndarray): Imagem de entrada.

    Returns:
    np.ndarray: Imagem quantizada.
    """
    Z = img.reshape((-1,3)).astype(np.float32)
    K = 2 # no. de clusters

    crit = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, label, center = cv.kmeans(Z, K, None, crit, 10, cv.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape((img.shape))
    
    return result

if __name__ == "__main__":
    img = cv.imread("images/pcb.png", cv.IMREAD_UNCHANGED)
    copy = img.copy() # copia utilizada para desenhar os retangulos

    """
    borra a imagem com filtro de média para uniformizá-la e reduzir o ruído.
    em seguida aplica a quantização.
    """
    blurred = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=3, sigmaY=3)
    quantized = quantization(blurred)
    quantized = cv.cvtColor(quantized, cv.COLOR_BGR2GRAY)

    """
    O detector de bordas irá contornar as regiões de contraste entre as duas cores da quantização.
    """
    edges = cv.Canny(quantized, 100, 200)
    
    """
    Encontra os contornos que estão interconectados, e desenha bounding-boxes ao redor.
    """
    contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        cv.rectangle(copy, (x, y), (x+w, y+h), (255, 0, 0), 1)

    cv.imshow("resultado", copy)
    cv.waitKey(0)
    cv.destroyAllWindows()