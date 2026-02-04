from setuptools import find_packages, setup

package_name = 'limo_application'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='uc',
    maintainer_email='uc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'move_limo=limo_application.move_limo:main',
            'rotate_absolute=limo_application.rotate_absolute:main',
            'limo_stop=limo_application.limo_stop:main',
        ],
    },
)
