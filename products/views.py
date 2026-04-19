from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""
<h1>Welcome to Toriloshop</h1>
<p> Your one-stop online store for quality products at great prices.</P>
<a href='/products/'>Browse Products </a> | <a href='/about/'>About Us </a>""")



def product_list(request):
    return HttpResponse("""
<h1>Our products</h1>
<ul>
     <li>product 1 - premium Backpack - $49.99</li>                   
     <li>product 2 - wireless Headphone - $80.9</li>                   
     <li>product 3 - Running shoes - $129.99</li>                   
</ul>
<a href='/'>Back to Home </a>
    """)


def about(request):
    return HttpResponse("""
<h1>About Toriloshop</h1>
<p>Toriloshop was founded in 2026 with a mission to make online shopping easier for everyone</p>
<a href='/'>Back to Home </a>
""")


def custom_404(request, exception):
    return HttpResponse("""
        <h1>404 - Page Not Found </h1>
        <p>Oops! This page doesn't exist in ToriloShop.</p>
        <a href='/'>← Go Back Home</a>
    """, status=404)