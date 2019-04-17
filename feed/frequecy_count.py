from django.conf import settings

from typing import List
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm, LoginForm
from .models import Republic, Ndtv, Indiatoday, Hindustan, Thehindu, Zeenews,IndexTop10
import psycopg2
import nltk

from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist
from django.db.models import Q

headlines = ""

new_stop_words = ['says', 'khan', 'singh', "'s", "''",
                  'to', 'in', 'for', 'on', 'of', '``', 'and', 'the',
                  'a', 'after', '10', "n't", 'man', 'us', 'first', 'day', "'", '’', '‘', 'new', 'vs', 'india', 'top',
                  '...', 'life',
                  'gets', 'back', 'takes', 'rs', 'take'

                  ]


def getHeadLine(headline):
    global headlines
    for title in headline:
        headlines += title.headline


def main():
    global headlines
    headlines = ""
    republic_headline = Republic.objects.order_by('-date')[0:100]
    ndtv_headline = Ndtv.objects.order_by('-date')[0:100]
    hindstan_headline = Hindustan.objects.order_by('-date')[0:100]
    thehindu_headline = Thehindu.objects.order_by('-date')[0:100]
    zeenews_headline = Zeenews.objects.order_by('-date')[0:100]

    getHeadLine(republic_headline)
    getHeadLine(ndtv_headline)
    getHeadLine(hindstan_headline)
    getHeadLine(thehindu_headline)
    getHeadLine(zeenews_headline)
    fd = FreqDist()
    headlines_token = nltk.word_tokenize(headlines)
    stop_words = stopwords.words('english')
    for word in headlines_token:
        if word.lower() not in stop_words and word.lower() not in string.punctuation:
            if word.lower() not in new_stop_words and not word.isnumeric():
                fd[word.lower()] += 1
    pk = 0;
    for word, frequency in fd.most_common(11):
        update = IndexTop10(db_keyword=word, db_frequency=frequency)
        update.save()
        pk = pk + 1
