import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
   name='sticksGame',
   version='1.0',
   author='Jean Soler',
   author_email='jean.soler3108@gmail.com',
   description='Basic class to play the sticks Game from the french TV show Fort Boyard',
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/jean3108/sticksGame",
   packages=setuptools.find_packages(),
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)