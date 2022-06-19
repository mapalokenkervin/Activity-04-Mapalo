import cv2
import os

while True:
    file = input(" \nFile name: ")
    fileName = str(file + '.jpg')

    flag = int(input("[1] Colored [2] Grayscale \nEnter Flag Values: "))

    if flag == 1:
        if os.path.exists(fileName):
            image = cv2.imread(fileName,1)
            if file == 'jesse':
                name = 'Jesse'
                cv2.imshow(name, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            
            if file == 'heisenberg':
                name = 'Heisenberg'
                cv2.imshow(name, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

        else:
            print("File not found...")

    elif flag == 2:
        if os.path.exists(fileName):
            image = cv2.imread(fileName,0)
            if file == 'jesse':
                name = 'Jesse'
                cv2.imshow(name, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

            if file == 'heisenberg':
                name = 'Heisenberg'
                cv2.imshow(name, image)
                cv2.waitKey(0)  
                cv2.destroyAllWindows()
                break

        else:
            print("File not found...")

    else:
        print("Error Flag...")

while True:

    print("\nChoose option \n\n[1] Fixed Path \n[2] User Provided Path")
    choice = int(input("Choice: "))
    
    if choice == 1:
        import fixed 
        break

    elif choice == 2:
        import user
        break
    
    else:
        print("Invalid Input...")