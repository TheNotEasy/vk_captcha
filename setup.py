from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
with open("./requirements.txt") as req_file:
    requirements =[i.replace('\n', '').replace('\r', '') for i in req_file]


setup(
  name='vk_captcha_cyrillic',
  packages=['vk_captcha'],
  version='2.0.3',
  license='MIT',
  author='IMCorp',
#  description='Library to solve vk captcha async/sync.\nFree.\nHigh speed.',
  long_description_content_type='text/markdown',
  long_description=long_description,
  package_data={'vk_captcha': ['*.onnx']},
  url='https://github.com/TheNotEasy/vk_captcha',   # Provide either the link to your github or to your website
  keywords=['vk', 'captcha', 'vk_captcha', 'solver'],
  install_requires=requirements,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
