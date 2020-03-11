
# In[1]:


get_ipython().magic('matplotlib inline')

# Import modules
import cv2
import matplotlib.pyplot as plt
from dataPath import DATA_PATH


# In[2]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)


# In[3]:


# Image Path
imgPath = DATA_PATH+"images/IDCard-Satya.png"

# Read image

img = cv2.imread(imgPath,cv2.IMREAD_COLOR)
plt.imshow(img[:,:,::-1])


# In[4]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# # <font style = "color:rgb(50,120,229)"> Step 2: Detect QR Code in the Image </font>

# In[5]:


# Create a QRCodeDetector Object
# Variable name should be qrDecoder

qrDecoder = cv2.QRCodeDetector()

# Detect QR Code in the Image
# Output should be stored in
# opencvData, bbox, rectifiedImage
# in the same order

opencvData, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)

# Check if a QR Code has been detected
if opencvData != None:
    print("QR Code Detected")
else:
    print("QR Code NOT Detected")


# In[6]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[7]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# # <font style = "color:rgb(50,120,229)"> Step 3: Draw bounding box around the detected QR Code </font>

# In[8]:


n = len(bbox)

top_left_corner = (bbox[0][0][0],bbox[0][0][1])
bottom_right_corner = (bbox[2][0][0],bbox[2][0][1])
# Draw the bounding box
new_img = cv2.rectangle(img,top_left_corner,bottom_right_corner,(255,0,0),2)

plt.imshow(new_img[:,:,::-1]) #check if correct box was made


# # <font style = "color:rgb(50,120,229)"> Step 4: Print the Decoded Text </font>

# In[9]:


# Since we have already detected and decoded the QR Code
# using qrDecoder.detectAndDecode, we will directly
# use the decoded text we obtained at that step (opencvdata)

print("QR Code Detected!")
print(opencvData)


# In[10]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# # <font style = "color:rgb(50,120,229)"> Step 5: Save and display the result image </font>

# In[11]:


# Write the result image
resultImagePath = "QRCode-Output.png"
cv2.imwrite(resultImagePath,new_img)


# In[12]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[13]:


# Display the result image
plt.imshow(img)

# Notice anything wrong?


# In[14]:


# OpenCV uses BGR whereas Matplotlib uses RGB format
# So convert the BGR image to RGB image
# And display the correct image

plt.imshow(img[:,:,::-1])

