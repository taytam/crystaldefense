from distutils.core import setup
import py2exe
import glob

setup(name='Crystal Defense',
    version='1.0',
    author='Taylor Tamblin',
    author_email='opethiantaylor@gmail.com',
    py_modules=[ 'main', 'graphics', 'enemy', 'tower', 'towermenu',
				'projectile', 'towerradius', 'easymap', 'tower_stats', 'buttons',
				'mainmenu', 'player', 'wave', 'mediummap', 'hardmap'],
	data_files=[("Graphics", glob.glob("Graphics/*.png"))],
	options={"py2exe": {"optimize": 0,
			"bundle_files": 3,}},
	zipfile = None,
	console=['main.py'],
	#windows = [{"script": 'main.py'}],
	)