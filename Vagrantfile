Vagrant.configure("2") do |config|
  config.vm.define "Django" do |config|
    config.vm.box = "debianwheezy"
    config.vm.hostname = "Django"
    config.vm.box_url = "https://dl.dropboxusercontent.com/u/4775364/vagrant/debian-6.0.9-amd64-plain-virtualbox.box"

    config.vm.network :"public_network", ip:"192.168.8.32"
#    config.vm.synced_folder "", "/var/www/Marisa"
     
    config.vm.provision :ansible do |ansible|
    ansible.playbook = "tasks/tasks.yml"
    end 
    
    #config.vm.provision "shell", inline: <<-SHELL

	
#  SHELL

   config.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 512]
      v.customize ["modifyvm", :id, "--name", "Django"]
    end
  end

end
