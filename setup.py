from setuptools import setup, find_packages

setup(
  name="canvas_lms_api",
  version="0.5.1.1",
  packages=find_packages(include=['canvas_lms_api', 'canvas_lms_api.*']),
  install_requires=["requests"]
)
