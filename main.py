# data types
from pyscript import display, document


def sample_function(e):
    document.getElementById('output1').innerHTML=" "
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    science  = document.getElementById('science').value
    math = document.getElementById('math').value
    english = document.getElementById('english').value
    filipino = document.getElementById('filipino').value
    ict = document.getElementById('ict').value
    pe = document.getElementById('pe').value

    average = [5, 5, 5, 3, 2, 1]
    science, math, english, filipino, ict, pe = average
    calculate = (science*5)+(math*5)+(english*5)+(filipino*3)+(ict*2)+(pe*1)/ (science+math+english+filipino+ict+pe)


    display(f'Name {fname}{lname} Science:{science} Math:{math} English:{english} Filipino:{filipino} ICT:{ict} PE:{pe}', target='output1')


def number_checker(e):
  num1 = int(document.getElementById('input1').value)

if num1 > 74 :
  display(f'You passed!', target='output')
else:
  display(f'You Failed..', target='output')



