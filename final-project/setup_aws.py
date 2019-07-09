import os


def setup_common():
    os.system("sudo pip3 install tqdm")
    os.system("sudo pip3 install backports.weakref==1.0.post1")
    os.system("sudo pip3 install ChatterBot==0.7.6")
    os.system("sudo pip3 install enum34==1.1.6")
    os.system("sudo pip3 install funcsigs==1.0.2")
    os.system("sudo pip3 install gensim==3.1.0")
    os.system("sudo pip3 install jedi==0.11.0")
    # os.system("sudo pip3 install libarchive==0.4.4")
    os.system("sudo pip3 install mock==2.0.0")
    os.system("sudo pip3 install parso==0.1.0")
    os.system("sudo pip3 install pbr==3.1.1")
    os.system("sudo pip3 install regex==2017.11.9")


def setup_starspace():
    if not os.path.exists("/usr/local/bin/starspace"):
        os.system("wget https://dl.bintray.com/boostorg/release/1.63.0/source/boost_1_63_0.zip")
        os.system("unzip boost_1_63_0.zip && mv boost_1_63_0 /usr/local/bin")
        os.system("git clone https://github.com/facebookresearch/Starspace.git")
        os.system("cd Starspace && make && cp -Rf starspace /usr/local/bin")

def setup_project():
    #setup_common()
    setup_starspace()

if __name__ == "__main__":
    setup_project()
