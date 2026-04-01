from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.xmlUpdate'
setup(name='enigma2-plugin-systemplugins-xmlupdate',
       version='3.0',
       description='xmlupdate...',
       package_dir={pkg: 'xmlUpdate'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE', 'LICENSE.GPLv2']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
