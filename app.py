#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/", methods=["GET","POST"])
def index():
        if request.method == "POST":
            rates=float(request.form.get("rates"))#rates 表示前端
            print(rates)
            model1=joblib.load("regression")
            r1=model1.predict([[rates]])
            model2=joblib.load("tree")
            r2=model2.predict([[rates]])
            return(render_template("index.html",result1=r1,result2=r2))
        else:
            return(render_template("index.html",result1="Waiting",result2="Waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




