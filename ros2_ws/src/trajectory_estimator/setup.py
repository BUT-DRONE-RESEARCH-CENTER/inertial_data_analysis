from setuptools import find_packages, setup

package_name = 'trajectory_estimator'

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
    maintainer='vitek',
    maintainer_email='vitek.zacek9@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "gps_pub = trajectory_estimator.gps_pub:main",
            "imu_pub = trajectory_estimator.imu_pub:main"
        ],
    },
)
