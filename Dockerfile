# set base image (host OS)
FROM python:3.8-slim

# adding a non root user
RUN useradd --create-home --shell /bin/bash app_user

# working directory
WORKDIR /home/app_user

# copy the dependencies file to the working directory
COPY requirements.txt ./

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#changing user to non root user after dependencies instalation
USER app_user

COPY . .

CMD ["bash"]