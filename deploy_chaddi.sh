cd chaddibot
git pull
source src/.env/bin/activate
pip install -r requirements.txt
pytest
./kill_prod.sh
./run_prod.sh
ps aux | grep python