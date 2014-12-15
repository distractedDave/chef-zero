chef-zero
=========

Chef Zero provisioner plugin
Needed a betterway to deploy my chef
I use svn and checkout the cookbook repo to /tmp/chef-repo
I then pass /tmp/chef-repo through to the chroot.
I then cd to /tmp/chef-repo run a knife upload * -z
I then use that to run chef-client -z

The chef-payload option needs to be filled out, (but it is not used)
