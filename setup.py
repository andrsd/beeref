from setuptools import setup
from beeref import constants
import platform
from glob import glob

main_script = 'beeref/__main__.py'
assets_dir = 'beeref/assets'

if platform.system() == 'Darwin':
    PLIST_INFO = {
        'CFBundleName': constants.APPNAME,
        'CFBundleDisplayName': constants.APPNAME,
        'CFBundleIdentifier': "org.beeref.app",
        'CFBundleVersion': str(constants.VERSION),
        'CFBundleShortVersionString': str(constants.VERSION),
        'CFBundleDocumentTypes': [{
            'CFBundleTypeRole': 'Viewer',
            'CFBundleTypeOSTypes': ['****', 'fold', 'disk'],
            'CFBundleTypeExtensions': ['bee'],
            'CFBundleTypeIconFile': 'logo.icns',
            'CFBundleTypeMIMETypes': 'application/octet-stream',
            'CFBundleTypeName': 'BeeRef Document'
        }]
    }

    extra_options = dict(
        setup_requires=['py2app'],
        app=[main_script],
        data_files=[
            ('assets', glob(assets_dir + '/*.png'))
        ],
        options={
            'py2app': {
                'argv_emulation': True,
                'plist': PLIST_INFO,
                'iconfile': 'beeref/assets/logo.icns',
                'packages': [
                    'PyQt6'
                ]
            }
        }
    )
elif platform.system() == 'win32':
    # TOOD
    pass
else:
    extra_options = dict(
        # Normally unix-like platforms will use "setup.py install" and install
        # the main script as such
        scripts=[main_script]
    )

setup(
    name='BeeRef',
    version='0.2.0',
    author='Rebecca Breu',
    author_email='rebecca@rbreu.de',
    url='https://github.com/rbreu/beeref',
    license='LICENSE',
    description='A simple reference image viewer',
    install_requires=[
        'pyQt6>=6.1,<=6.1.1',
        'pyQt6-Qt6>=6.1,<=6.1.1',
        'rectangle-packer>=2.0.1',
        'exif',
    ],
    packages=[
        'beeref',
        'beeref.actions',
        'beeref.assets',
        'beeref.documentation',
        'beeref.fileio',
    ],
    entry_points={
        'gui_scripts': [
            'beeref = beeref.__main__:main'
        ]
    },
    include_package_data=True,
    package_data={
        'beeref.assets': ['*.png'],
        'beeref': ['documentation/*.html'],
    },
    **extra_options
)
