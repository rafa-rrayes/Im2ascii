import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="im2ascii",
    version="0.0.1",
    author="Rafael Rayes",
    author_email="rafa@rayes.com.br",
    description="Display your images in form of ascii typed characters!",
    long_description="""
# Im2ascii
A small python project that transforms images into ascii text

First of all import the package with:
````
pip install im2ascii
````
now import the package to your code:
````
import im2ascii
````
Now lets use it!

The only function is asciify, see:
````
im2ascii.asciify("/full/path/to/image.png")
````
This will return your image except it is typed in ascii characters!

### Aditional Parameters
There are only two aditional paramters for the function, square and invert. 
The square parameter makes sure your image is returned squared and not a rectangle. This is activated by default on the function, to deactivate it just use:
````
asciify('image.png', square=False)
````

The invert parameter invert the tones on the result of the image. like so:
For white tones, a '.' will be added, and for darker tones, a '@' will be the result. if you use ``invert=True``, this will be inverted.


""",
    long_description_content_type="text/markdown",
    url="https://github.com/rrayes3110/Im2ascii",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
