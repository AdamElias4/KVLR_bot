#!/usr/bin/env python
# coding: utf-8

# In[36]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import os
import time
import random

def original_bot(url, start, end, state_abbrev):

    PATH = "/Users/eric/Downloads/chromedriver" # change 'mitchellpolozov' to the user associated with your computer!
    driver = webdriver.Chrome(PATH)

    driver.get(url)
    time.sleep(5)

    user = driver.find_element_by_name("name")
    user.send_keys("PACREG2076036")

    pin = driver.find_element_by_name("user_pin")
    pin.send_keys("1718")
    pin.send_keys(Keys.RETURN)

    time.sleep(15)

    pages = end - start

    for i in range(pages):
        captchaPresent = len(driver.find_elements_by_name('ResultViews.Attempt')) > 0

        if captchaPresent:
            add_box = driver.find_element_by_name('ResultViews.Attempt')
            add_box.send_keys("7")
            continu = driver.find_element_by_xpath("//span[text() = 'Continue']")
            continu.click()

        selector = driver.find_element_by_id('checkboxCol')
        selector.click()
        page = driver.find_element_by_xpath('//*[@class = "next button mousedown-enterkey"]')
        page.click()
        time.sleep(random.randint(5, 10))

    download = driver.find_element_by_xpath('//*[@class = "action download action-download"]')
    download.click()

    time.sleep(15)
    custom = driver.find_element_by_id('detailCustom')
    custom.click()

    Record_type_unselect = driver.find_element_by_xpath('//*[contains(text(), "Record Type")]').click()
    Fax_num = driver.find_element_by_xpath('//*[contains(text(), "Fax Number Combined")]').click()
    Phone_num = driver.find_element_by_xpath('//*[contains(text(), "Phone Number Combined")]').click()
    website = driver.find_element_by_xpath('//*[contains(text(), "Website")]').click()
    Location_sales = driver.find_element_by_xpath('//*[contains(text(), "Location Sales Volume Actual")]').click()
    EIN_1 = driver.find_element_by_xpath('//*[contains(text(), "EIN 1")]').click()
    EIN_2 = driver.find_element_by_xpath('//*[contains(text(), "EIN 2")]').click()
    EIN_3 = driver.find_element_by_xpath('//*[contains(text(), "EIN 3")]').click()
    Linked_in = driver.find_element_by_xpath('//*[contains(text(), "Linked-In")]').click()

    download_records = driver.find_element_by_xpath(
        '//*[@class= "originButton ui-priority-primary view-on-exportlimit view-on-randomsample action-download"]').click()

    time.sleep(10)

    folder = glob.glob('/Users/eric/Downloads/*.csv') # change 'mitchellpolozov' to the user associated with your computer!
    newest_file = max(folder, key=os.path.getctime)

    end = end - 1

    # Deals with the last scrape of the state where the page number
    # is not divisible by 20

    while end % 20 != 0:
        end += 1

    os.rename(newest_file, str(end) + state_abbrev + 'RefUSA.csv')

    # prints to console to confirm the file was created
    print(str(end) + state_abbrev + 'RefUSA.csv file successfully created')

    driver.quit()


# In[39]:


original_bot("http://www.referenceusa.com.chipublib.idm.oclc.org/UsBusiness/Result/7e565695bea84086a9d24f7816890dec", 1, 21, 'IL')


# In[38]:


original_bot("http://www.referenceusa.com.chipublib.idm.oclc.org/UsBusiness/Result/4e9ec37a0e8a4b678b9296cc6d96a253", 37, 41, 'IL')


# In[2]:


import PIL
print("pillow version", PIL.__version__)


# In[3]:


import os
cwd = os.getcwd()
print(cwd)


# In[4]:


os.chdir('/Users/eric/Desktop/KVLR/captcha')


# In[5]:


import os
cwd = os.getcwd()
print(cwd)


# In[6]:


from PIL import Image 
image = Image.open('test1.jpg')
print(image.format)
print(image.mode)
print(image.size)


# In[7]:


from PIL import Image
from numpy import asarray
# load the image
image = Image.open('download-36.jpg')
# convert image to numpy array
data = asarray(image)
# summarize shape
print(data.shape)
# create Pillow image
image2 = Image.fromarray(data)
# summarize image details
print(image2.format)
print(image2.mode)
print(image2.size)


# In[8]:


conda-forge/osx-64::tesseract-4.1.1-haaf70cb_2


# In[9]:


pip install pytesseract


# In[10]:


import pytesseract
import cv2

print(pytesseract.image_to_string(Image.open("download-4.jpg"), lang ="eng"))


# In[11]:


text = pytesseract.image_to_string(Image.open('test.png'))
print(text)


# In[ ]:





# In[12]:


from PIL import Image
# load the image
image = Image.open('download-58.png')
# convert the image to grayscale
gs_image = image.convert(mode='L')
# save in jpeg format
gs_image.save('grey.png')
# load the image again and show it
image2 = Image.open('grey.png')
# show the image
image2.show()


# In[13]:


from matplotlib import image
from matplotlib import pyplot
# load image as pixel array
data = image.imread('download-7.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[14]:


print(pytesseract.image_to_string(Image.open('download-7.jpg')))


# In[15]:


data = image.imread('download-17.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[16]:


print(pytesseract.image_to_string(Image.open('download-17.jpg')))


# In[17]:


data = image.imread('download-23.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[18]:


print(pytesseract.image_to_string(Image.open('download-23.jpg')))


# In[19]:


data = image.imread('download-25.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[20]:


print(pytesseract.image_to_string(Image.open('download-25.jpg')))


# In[21]:


data = image.imread('download-26.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[22]:


print(pytesseract.image_to_string(Image.open('download-26.jpg')))


# In[23]:


data = image.imread('download-32.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[24]:


print(pytesseract.image_to_string(Image.open('download-32.jpg')))


# In[25]:


data = image.imread('download-34.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[26]:


print(pytesseract.image_to_string(Image.open('download-34.jpg')))


# In[27]:


data = image.imread('download-37.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[28]:


print(pytesseract.image_to_string(Image.open('download-37.jpg')))


# In[29]:


data = image.imread('download-43.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[30]:


print(pytesseract.image_to_string(Image.open('download-43.jpg')))


# In[31]:


data = image.imread('download-51.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[32]:


print(pytesseract.image_to_string(Image.open('download-51.jpg')))


# In[54]:


import cv2

img = cv2.imread('download-60.jpg')

print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))


# In[52]:



blue, green, red = cv2.split(img) # Split the image into its channels
image = Image.open('download-60.jpg')
# convert the image to grayscale
gs_image = image.convert(mode='L')
# save in jpeg format
gs_image.save('grey60.jpg')
# load the image again and show it
img = Image.open('grey60.jpg')
# show the image
image2.show()

pyplot.imshow(red) # Display the red channel in the image
pyplot.imshow(blue) # Display the red channel in the image
pyplot.imshow(green) # Display the red channel in the image

pyplot.imshow(img) 


# In[35]:


imgB = cv2.imread('image.png', 0)

# Perform binary thresholding on the image with T = 125
r, threshold = cv2.threshold(imgB, 125, 255, cv2.THRESH_BINARY)
pyplot.imshow(threshold)


# In[58]:


import numpy as np

# Adding salt & pepper noise to an image
def salt_pepper(prob):
      # Extract image dimensions
      row, col = img.shape

      # Declare salt & pepper noise ratio
      s_vs_p = 0.5
      output = np.copy(img)

      # Apply salt noise on each pixel individually
      num_salt = np.ceil(prob * img.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in img.shape]
      output[coords] = 1

      # Apply pepper noise on each pixel individually
      num_pepper = np.ceil(prob * img.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in img.shape]
      output[coords] = 0
      cv2_imshow(output)

      return output


# In[59]:


import cv2
sp_05 = salt_pepper(0.5)

pyplot.imwrite('sp_05.jpg', sp_05)


# In[63]:


img = Image.open('grey60.jpg')
img.shape()


# In[ ]:




