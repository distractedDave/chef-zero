from setuptools import setup, find_packages
setup(
    name = "aminatorplugins_chef_zero",
    version = "0.1",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', 'aminatorplugins.provisioner'),

    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminatorplugins.provisioner.chef_zero.yml']),
    ],

    entry_points = {
       'aminator.plugins.provisioner': [
           'chef-zero = aminatorplugins.provisioner.chef_zero:ChefProvisionerPlugin',
       ],
    },

    # metadata for upload to PyPI
    author = "David Owens",
    author_email = "dave@davetested.com",
    description = "Chef Zero provisioner for Netflix's aminator",
    license = "Apache 2.0",
    keywords = "aminator plugin chef-zero chef zero",
)
