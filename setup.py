from setuptools import setup, find_packages

setup(
    name='ormedian_utils',
    packages=find_packages(exclude=['examples']),
    version='0.0.0.0',
    license='MIT',
    description='Utilities for Computer Vision Tasks',
    author='Samuel Adebayo',
    author_email='samuel@ormedian.com',
    url='https://github.com/exponentialR/ormedian_utils',
    keywords=['computer vision',
              'image resizer',
              'auto file mover',
              'save frames from videos',
              'save frames from camera'
              'ormedian utilities'
              ],
    install_requires=["Pillow >= 8.4.0", "opencv-python>=4.5.4.58", "matplotlib>=3.3.1", "tqdm >= 4.64.0"],

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8"],

)
