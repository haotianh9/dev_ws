from setuptools import setup

package_name = 'cv_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='pi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = cv_basics.webcam_pub:main',
            'img_subscriber = cv_basics.webcam_sub:main',
            'img_object_detection = cv_basics.webcam_od:main',
        ],
    },
)
