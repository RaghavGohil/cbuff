name = 'cbuff'
version = '1.0.1'
description = 'A command buffer for terminals.'
author = 'RaghavGohil'
author_email = 'raghavgohil2004@gmail.com'
project_url = 'https://github.com/RaghavGohil/cbuff'
classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft',
]
entry_points = '''
        [console_scripts]
        cbuff=cbuff.main:main
    '''
exclude_packages = ('tests')
license = 'MIT LICENSE'
license_files = ('LICENSE.txt')
keywords = 'command buffer terminal storage windows linux macos '
install_requires = ['readme_renderer >= 21.0']
include_package_data = True
python_requires='>=3.0'