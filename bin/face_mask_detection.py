import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import mysql.connector


gpus = tf.config.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only use the first GPU
  try:
    tf.config.set_visible_devices(gpus[0], 'GPU')
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
  except RuntimeError as e:
    # Visible devices must be set before GPUs have been initialized
    print(e)

    gpus = tf.config.list_physical_devices('GPU')
    
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)

cap = cv2.VideoCapture(1) # Video source capturing
cap.set(3, 640) # Width of the video window
cap.set(4, 480) # Height of the video window

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Face detector
maskClassifier = load_model('maskclassifier.model') # Mask classifier

while True:
   
    _, frame = cap.read() # Reading frame from video source

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Converting RGB to Grayscale
    
    faces = faceCascade.detectMultiScale( # Detecting faces
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        )
    
    for (x, y, h, w) in faces: 
      faceROI = frame[y : y + h, x : x + w, :] # Cropping face region of interest

      faceROI = cv2.resize(faceROI, (160, 160)) # Resizing faceROI to 160x160
                                                # Because, Our VGG16 model accepts 160x160 as input 
      faceROI = img_to_array(faceROI)
      faceROI = faceROI.reshape(1, 160, 160, 3) # Changing dimensions to 1x160x160x3, Because our VGG16 
                                                # take input as 4D matrix(BATCH_SIZE, 160, 160, #Channels)
     

      conn = mysql.connector.connect(
          host="localhost", user="root", password="", database="spycrop")
      my_cursor = conn.cursor()

      my_cursor.execute(
          "SELECT fname, lname FROM `user_table` WHERE id="+str(id))
      n = my_cursor.fetchone()
      n = " ".join(n)

      my_cursor.execute(
          "SELECT rollNo FROM `user_table` WHERE id="+str(id))
      r = my_cursor.fetchone()
      r = "+".join(r)

      my_cursor.execute(
          "SELECT dept FROM `user_table` WHERE id="+str(id))
      d = my_cursor.fetchone()
      d = "+".join(d)

      my_cursor.execute(
          "SELECT email FROM `user_table` WHERE id="+str(id))
      e = my_cursor.fetchone()
      e = "+".join(e)

      

      prediction = maskClassifier(faceROI) # Making predictions
      (withoutmask, withmask) = prediction[0].numpy()
      
      # Drawing bounding boxes using OpenCV
      if withmask > withoutmask:
          (label, color, prob) = ('Mask', (0, 255, 0), withmask*100.0)
      else:
          (label, color, prob) = ('No mask', (0, 0, 255), withoutmask*100.0)


    # (label, color, prob) = ('Mask', (0, 255, 0), withmask*100.0) if withmask > withoutmask else ('No mask', (0, 0, 255), withoutmask*100.0)

      cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

      cv2.rectangle(frame, (x + 15, y + 2), (x + w - 15, y + 20), (0, 0, 0), -1) #lower
      cv2.rectangle(frame, (x + 15, y - 2), (x + w - 15, y - 20), (0, 0, 0), -1) #upper

      cv2.putText(frame, str(prob)+' %', (x + 20, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
      cv2.putText(frame, label, (x + 20, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)

        
    cv2.imshow('Video', frame) # Displaying the video
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release() # Releasing the capture
cv2.destroyAllWindows()
