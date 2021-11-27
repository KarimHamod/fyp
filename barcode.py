
import cv2
from pyzbar.pyzbar import decode
def BarcodeReader(image) :
    # read the image in numpy array using cv2
    img = cv2.imread(image)

    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes :
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else :

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes :

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to heighlight the barcode
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "" :
                # Print the barcode data
                print(barcode.data)
                return str(barcode.data)

    # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
url = ""
cap = cv2.VideoCapture(url)
while(True):
     camera, frame = cap.read()
     if frame is not None:
        cv2.imshow("Frame", cv2.resize(frame,(600,400)))
     if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing
        cv2.imwrite('potata2.png', frame)
        cv2.destroyAllWindows()
        break

def searchitems(input):
    obj1 = open("items.txt")

    for line in obj1.readlines() :
      line = line.rstrip()
      if input in line:
            print (line)
    obj1.close()
image=('new item.png')

output=BarcodeReader(image)
searchitems(output)
#bar code generator
#print("please enter item name")
#item=input()
#img=qrcode.make(item)
#img.save(item)