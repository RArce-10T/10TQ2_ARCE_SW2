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

    

    display(f'Name {fname}{lname} Science:{science} Math:{math} English:{english} Filipino:{filipino} ICT:{ict} PE:{pe}', target='output1')
