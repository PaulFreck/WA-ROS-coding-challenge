from setuptools import find_packages, setup

package_name = 'merge_arrays'

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
    maintainer='paul',
    maintainer_email='pfreck@wisc.edu',
    description='Merges 2 sorted arrays of topic /input/array1 and /input/array2 into 1 sorted array published to /outpu/array',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'merge_arrays_node = merge_arrays.publisher_member_function:main',
        ],
    },
)
