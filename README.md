# Send emails with python

Just a simple script I use on servers which do not have a configured email server, so normal `mail` does not work.

## Instructions

```shell
pip install -r requirements.txt
cp config/main.default.yaml config/main.yaml
# Change the config as you please and enter your email credentials
$EDITOR config/main.yaml

# See the parameters
./send_email.py --help
```