from setuptools import setup, find_packages

setup(
    name='image-color-sorter',
    version='1.0.0',
    description='A Python script to sort images into folders based on their dominant color.',
    author='Awa',
    author_email='alwalxed@proton.me',
    url='https://github.com/alwalxed/image-color-sorter',
    packages=find_packages(),
    install_requires=[
        'Pillow==9.1.1',
        'numpy==1.22.4',
        'scikit-learn==1.1.1'
    ],
    entry_points={
        'console_scripts': [
            'image-color-sorter=image_color_sorter.sorter:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)