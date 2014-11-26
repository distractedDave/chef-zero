from setuptools import setup, find_packages
setup(
    name = "aminatorplugins_chef_zero",
    version = "0.1.1",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', 'aminatorplugins.provisioner'),

    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminator.plugins.provisioner.chef.yml']),
    ],

    entry_points = {
       'aminator.plugins.provisioner': [
           'chef = aminatorplugins.provisioner.chef:ChefProvisionerPlugin',
       ],
    },

    # metadata for upload to PyPI
    author = "David Owens",
    author_email = "dave@davetested.com",
    description = "Chef Zero provisioner for Netflix's aminator -- Hacked out of The Chef-solo provisioner Thanks to Asbjorn Kjaer ",
    license = "Apache 2.0",
    keywords = "aminator plugin chef-zero chef zero",
)
