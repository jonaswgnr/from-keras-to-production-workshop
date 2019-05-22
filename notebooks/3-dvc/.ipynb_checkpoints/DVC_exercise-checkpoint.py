import fire
import cv2
import json

def preprocess(inputPicture, outputPicture):
    img = cv2.imread(inputPicture, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (100,100))
    cv2.imwrite(outputPicture, img)
    print("Finished")
    
def classify(picture, result):
    img = cv2.imread(picture, cv2.IMREAD_GRAYSCALE)
    circles = cv2.HoughCircles(img, 
                               cv2.HOUGH_GRADIENT,
                               dp=2, 
                               minDist=15, 
                               param1=100, 
                               param2=70)
    
    if circles is None:
        fruit="banana"
    else:
        fruit="lemon"
        
    with open(result,"w") as out:
            json.dump({"class": fruit}, out)

if __name__ == '__main__':
    fire.Fire()