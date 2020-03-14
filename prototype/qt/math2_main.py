'''
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

pageSource = """
             <html><head>
             <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML">                     
             </script></head>
             <body>
             Hello World
             <p><mathjax style="font-size:2.3em">$$u = \int_{-\infty}^{\infty}(awesome)\cdot du$$</mathjax></p>
             </body></html>
             """

app = QApplication(sys.argv)
webView = QWebEngineView()
webView.setHtml(pageSource)

webView.show()
sys.exit(app.exec_())
'''

pageSource1 = """
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <title></title>
  <style type="text/css">code{white-space: pre;}</style>
  <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML-full" type="text/javascript"></script>
</head>
<body>
<div id="TOC">
<ul>
<li><a href="#section-1">Section 1</a><ul>
<li><a href="#subsection-1.1">Subsection 1.1</a></li>
</ul></li>
</ul>
</div>
<h1 id="section-1">Section 1</h1>
<p>Equation 1:</p>
<p><span class="math display">\[I = \int \rho R^{2} dV\]</span></p>
<p>Equation 2:</p>
<span class="math display">\[\begin{align}
I = \int \rho R^{2} dV
\end{align}\]</span>
<p>Equation 3:</p>
<p><span class="math inline">\(e^x = \sum_{n=0}^\infty \frac{x^n}{n!} = \lim_{n\rightarrow\infty} (1+x/n)^n\)</span></p>
<p>Pandoc style equations/references:</p>
<ol class="example" style="list-style-type: decimal">
<li><span class="math inline">\(a^2 + b^2 = c^2\)</span></li>
</ol>
<p>As (1) says, ...</p>
<ol start="2" class="example" style="list-style-type: decimal">
<li><span class="math inline">\(e = x + y\)</span></li>
</ol>
<h2 id="subsection-1.1">Subsection 1.1</h2>
</body>
</html>

             """

pageSource = """
             <html>
             <body>
             Hello World
             </body></html>
             """

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
# use the QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import *
# start my_app
my_app = QApplication(sys.argv)
# open webpage
my_web = QWebEngineView()
my_web.setHtml(pageSource1)
my_web.show()
my_app.exec_()
# sys exit function