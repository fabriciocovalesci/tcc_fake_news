

sudo apt-get update
sudo apt install python3-pip
sudo apt install nginx  # We'll need this to connect the API to the internet.

- Add the FastAPI configuration to NGINX's folder.
cd /etc/nginx/sites-enabled/

- Create a file called fastapi_nginx (like the one in this repository).
sudo vim fastapi_nginx

- And put this config into the file (replace the IP address with your EC2 instance's public IP):
server {
    listen 80;   
    server_name <YOUR_EC2_IP>;    
    location / {        
        proxy_pass http://127.0.0.1:8000;    
    }
}

- Start NGINX.
sudo service nginx restart

- Start FastAPI.
python3 -m uvicorn main:app

