# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
    # Customize the amount of memory on the VM:
    vb.memory = "2048"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y build-essential git curl cmake libx11-dev \
                       libglu1-mesa-dev libxrandr-dev libxinerama-dev \
                       libxcursor-dev libxi-dev zlib1g-dev libasound2-dev \
                       libgtk2.0-dev libjack-jackd2-dev
    git clone https://github.com/Lewiscowles1986/Rack --depth=1
    cd Rack
    git checkout build-system
    git submodule update --init --recursive
    make dep -j4
    make -j4
  SHELL
end
