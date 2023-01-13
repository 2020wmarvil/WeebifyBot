echo "Usage: \$- chmod +x setup.sh && source setup.sh"

if [ -d "env" ]; then
  source env/bin/activate
else
  echo "Creating virtual environment..."
  python3 -m venv env
  source env/bin/activate

  echo "Installing requirements..."
  pip install -r requirements.txt
fi

echo "Setup successful. '\$- deactivate' to exit"
