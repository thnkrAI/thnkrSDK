from setuptools import setup, find_packages

setup(
   name = 'thnkrSDK',
   version = '0.1.0',
   
   description = 'Software Development Kit for connecting to the thnkrAPI',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   
   author = 'thnkrAI Inc.',
   author_email = 'contact@thnkrai.com',
   url='GITHUB REPO NOT YET PUBLIC - WILL UPDATE',
   
   packages = find_packages(),
   classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Operating System :: OS Independent',
   ],
   python_requires=">=3.6",
   install_requires = [
      'requests>=2.26.0',
   ],
   project_urls={
      'Source': 'GITHUB REPO NOT YET PUBLIC - WILL UPDATE',
      'Bug Reports': 'GITHUB REPO NOT YET PUBLIC - WILL UPDATE',
   },
)