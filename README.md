# sc_tunnel_data.py

sc_tunnel_data. is a Python library for getting Sauce Labs Sauce Connect Data.

## Usage

in CMD line:

python sc_tunnel_data.py

Enter the Username of the tunnel owner.

If tunnels are running, select from the list of tunnels by hitting 'y' and if it is not a running tunnel, select 'n' and
input tunnel ID

It does not matter which DC the tunnel is using, it will return the data.  If there are not username/tunnel ID
combinations, then the script will exit.
