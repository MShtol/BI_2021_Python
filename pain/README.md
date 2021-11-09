This is my awersome research on virtual environments. The article is available at doi:10.1111/1000-7 
With God's help you can reproduce my results by running scripts locally.
Please cite me!

Code runs on Python 3.9.5. My OS is Ubuntu 20.04.3 LTS

In order to run this code:

download this direectory and enter it

Be sure that you have appropriate version of python. If you don't have it, please install it. For example with
sudo apt-get install python3.9

create virtual environment with specified version po python
virtualenv --python=/usr/bin/python3.9 <env_name>

if you don't have virtualenv install it with
pip install virtualenv

start environment with
source ./venv/bin/activate

install all reqiered packages with
pip install -r requirements.txt

run script
python pain.py
