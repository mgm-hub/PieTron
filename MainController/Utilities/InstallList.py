

class InstallList:
    def __init__(self):
        pass


    @staticmethod
    def basic_ubuntu_install():
        update = "sudo apt-get update"
        htop = "sudo apt-get install htop -y"
        dconf = "sudo apt-get install dconf-tools -y"
        return [update, htop, dconf]

    @staticmethod
    def basic_java_install():
        javafolder = "sudo add-apt-repository ppa:webupd8team/java -y"
        update = "sudo apt-get update"
        java_accept ="echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections"
        java_set = "echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections"
        java = "sudo apt-get install -y oracle-java8-installer"
        return [javafolder, update, java_accept, java_set, java]

    @staticmethod
    def basic_python_install():
        python = "sudo apt-get install python-dev -y"
        pip = "sudo apt-get install -y python-pip python-dev build-essential"
        soup = "sudo pip install beautifulsoup4"
        lib = "sudo apt-get install -y python-libxml2 libxslt-dev"
        pyzmq = "sudo apt-get install -y python-zmq"
        pyquery = "sudo apt-get install -y python-pyquery"
        return [python, pip, soup, lib, pyzmq, pyquery]

    @staticmethod
    def basic_locust_install():
        libevent = "sudo apt-get install -y libevent-dev"
        greenlet = "sudo easy_install greenlet"
        gevent = "sudo easy_install gevent"
        locust = "sudo easy_install locustio"
        return [libevent, greenlet, gevent, locust]

    @staticmethod
    def basic_ubuntu_desktop_install():
        dconf = "sudo apt-get install dconf-tools -y"
        desktop = "sudo apt-get install -y --no-install-recommends ubuntu-desktop"
        remove_light = "sudo apt-get remove lightdm -y"
        gdm = "sudo apt-get install gdm -y"
        vnc = "sudo apt-get install vnc4server -y"
        terminal = "sudo apt-get install gnome-terminal -y"
        firefox = "sudo apt-get install firefox -y"
        return [dconf, desktop, remove_light, gdm, vnc, terminal, firefox]

