import tkinter as tk
import nltk
from textblob import TextBlob
from  newspaper import Article

def summarize():

    url=utext.get('1.0', "end").strip()

    article=Article(url)
    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    Publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    title.insert('1.0',article.title)
     
    author.insert('1.0',article.authors)
 
    Publication.insert('1.0',article.publish_date)
    
    summary.insert('1.0',article.summary)
     
    analysis=TextBlob(article.text)

    sentiment.insert('1.0',f'sentiment: {"positive" if analysis.polarity > 0 else "negative"}')

    title.config(state='disabled')
    author.config(state='disabled')
    Publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

window = tk.Tk()
window.title("News summarize")
window.geometry('1200x620')

tlabel=tk.Label(window, text="Title", font=('Rama Gothic',12,'bold'))
tlabel.pack()

title=tk.Text(window,height=1,width=140, font=('arial',10))
title.config(state='disable',bg="#FFFFFF")
title.pack()
 

alabel=tk.Label(window, text="Author", font=('Rama Gothic',12,'bold'))
alabel.pack()

author=tk.Text(window,height=1,width=140, font=('arial',10))
author.config(state='disable',bg="#FFFFFF")
author.pack()
 

plabel=tk.Label(window, text="Publishing Date", font=('Rama Gothic',12,'bold'))
plabel.pack()

Publication=tk.Text(window,height=1,width=140, font=('arial',10))
Publication.config(state='disable',bg="#FFFFFF")
Publication.pack()
 

slabel=tk.Label(window, text="Summary", font=('Rama Gothic',12,'bold'))
slabel.pack()

summary=tk.Text(window,height=20,width=140, font=('arial',10))
summary.config(state='disable',bg="#FFFFFF")
summary.pack()
 

selabel=tk.Label(window, text="Sentiment Analysis", font=('Rama Gothic',12,'bold'))
selabel.pack()

sentiment=tk.Text(window,height=1,width=140, font=('arial',10))
sentiment.config(state='disable',bg="#FFFFFF")
sentiment.pack()

ulabel=tk.Label(window, text="URL", font=('Rama Gothic',12,'bold'))
ulabel.pack()
utext=tk.Text(window,height=1,width=140, font=('arial',10))
utext.pack()


btn=tk.Button(window, text="summarize", font=('Rama Gothic',12,'bold'),command=summarize)
btn.pack()

window.mainloop()