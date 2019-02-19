all:

install_lib:
	 curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
	 python3 get-pip.py --user
	 pip3 install --user bs4 requests github3.py
	 
