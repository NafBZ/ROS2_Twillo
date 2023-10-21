from setuptools import find_packages, setup

package_name = 'twillo'

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
    maintainer='nafees',
    maintainer_email='zamannafees@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = twillo.publisher:main',
            'simple_subscriber = twillo.subscriber:main',
            'simple_parameter = twillo.parameters:main'
        ],
    },
)
