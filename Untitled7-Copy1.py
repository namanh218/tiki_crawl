#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
try:
    BASE_URL = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=c.1789.hamburger_menu_fly_out_banner'
    response = requests.get(BASE_URL)
except Exception as err:
    print("Error")
    


# In[4]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text)


# In[5]:


div = soup.find_all('div', {"class":"product-item"})
len(div)


# In[140]:


div[0].find('span', class_='price-regular').text



# In[80]:


tiki_now = ['href', '', 'href']
tiki_now_boolean = []
for i in tiki_now:
    if i == 'href':
        tiki_now_boolean.append(1)
    else:
        tiki_now_boolean.append(0)
# tiki_now_boolean.append(i for i in tiki_now if i == 'href')
print(tiki_now_boolean)


# In[129]:


productID, sellerID, title, price, category, URL, image, tikinow, rating, review =[], [], [], [], [], [], [], [], [],[]
for product in div:

    try:
        productID.append(product['data-id'])
        sellerID.append(product['data-seller-product-id'])
        title.append(product['data-title'])
        price.append(product.find('span', class_='price-regular').text)
        category.append(product['data-category'])
        URL.append(product.a['href'])
        image.append(product.img['src'])
        tikinow.append(str(product.find('i', class_='tikicon icon-tikinow')))
        rating.append(product.find('span', class_= 'rating-content').span['style'].strip('width:%'))
        review.append(product.find('p', class_= 'review').text.strip('()'))
        

    except: 
        print('pass')
        
        
        


# In[130]:


tiki_bolean = []
for i in tikinow:
    if i == '<i class="tikicon icon-tikinow"></i>':
        tiki_bolean.append("tikinow")
        tiki_bolean.append("Không có tikinow")
print(tiki_bolean)        


# In[131]:


rating_score = []
for i in rating:
    if  int(i) > 90:
        rating_score.append("Xuất sắc")
    elif int(i) > 70:
        rating_score.append("Tốt")
    else:
        rating_score.append("Trung Bình")
print(rating_score)


# In[ ]:





# In[134]:


import json

d = list(zip(productID, sellerID, title, price, category, URL, image, tiki_bolean, rating_score, review))
with open('div.json', 'w') as file:
    json.dump(d, file)


# In[135]:


with open('div.json', 'r') as file:
    reloaded = json.load(file)
reloaded


# In[ ]:





# In[ ]:




