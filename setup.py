"""Boilerplate setup for a WECS-based game. 
STARTPROJECT: Change this long-form description.
"""

# from setuptools import setup, find_packages
# from os import path
# 
# 
# here = path.abspath(path.dirname(__file__))
# 
# setup(
#     description='',   # STARTPROJECT: Short package description
#     url='',  # STARTPROJECT
#     author='',  # STARTPROJECT: Your name
#     author_email='',  # STARTPROJECT: Your email
#     classifiers=[
#         'Development Status :: 3 - Alpha',  # STARTPROJECT: The current status of your project
#         # STARTPROJECT: More classifiers can be found at https://pypi.org/classifiers/
#     ],
#     keywords='',  # STARTPROJECT: Package keywords to help searching for the package
#     packages=find_packages(exclude=['tests']),
#     python_requires='>=3.7, <4',
#     install_requires=[
#         'wecs',
#         'panda3d',
#         'panda3d-keybindings',
#         'panda3d-stageflow',
#     ],
#     # Deployment
#     options = {
#         'build_apps': {
#             'include_patterns': [ # STARTPROJECT: Tailor this list to your needs.
#                 '**/*.bam',
#                 '**/*.png',
#                 '**/*.jpg',
#                 "**/*.ttf",
#                 "**/*.glsl",
#                 "fonts/*",
#                 '**/*.config',
#             ],
#             'exclude_patterns': [
#                 "dist/*",
#                 ".git/*",
#                 "*__pycache__*",
#                 "README.md",
#                 "requirements.txt",
#                 "setup.py"
#             ],
#             'include_modules': {
#                 '*': [
#                     'keybindings',
#                 ],
#             },
#             'gui_apps': {'game_name': 'main.py'},  # STARTPROJECT: Change game_name to name used by the desktop environment
#             'console_apps': {'game_name': 'main.py'}, # STARTPROJECT: Change game_name to console command name
#             'log_filename': '$USER_APPDATA/default_name/output.log',  # STARTPROJECT
#             'log_append': False,
#             'plugins': [
#                 'pandagl',
#                 'p3openal_audio',
#             ],
#             'platforms': [  # STARTPROJECT: Change selection
#                 'manylinux1_x86_64',
#                 #'macosx_10_6_x86_64',
#                 #'win_amd64',
#             ],
#             'package_data_dirs': {
#                 #'numpy': [('numpy.libs/*', '', {'PKG_DATA_MAKE_EXECUTABLE'})]
#             },
#         },
#     },
# )


from setuptools import setup

setup(
    name='wecs-null-project',  # STARTPROJECT: Package name
    version='0.1.0a0',
    py_modules = ['game'],
    options={
        'build_apps': {
            'include_patterns': [
                #"**/*.bam",
                #"**/*.ttf",
                #"**/*.glsl",
                #"fonts/*",
                "keybindings.config",
            ],
            'exclude_patterns': [
                "dist/*",
                ".git/*",
                "*__pycache__*",
                "README.md",
                "requirements.txt",
                "setup.py"
            ],
            'log_filename': '$USER_APPDATA/game_name/game.log',
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
            'console_apps': {'game_name': 'main.py'},
            'gui_apps': {'game_name': 'main.py'},
            'platforms': [
                'manylinux1_x86_64',
                #'win_amd64',
            ],
            'package_data_dirs': {
                #'numpy': [('numpy.libs/*', '', {'PKG_DATA_MAKE_EXECUTABLE'})]
            }
        },
    }
)
