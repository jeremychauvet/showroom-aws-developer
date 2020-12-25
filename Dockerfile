FROM python:3.9
# Install security updates.
RUN pip install --upgrade pip
# Rootless mode.
RUN useradd -ms /bin/bash johndoe
USER johndoe
WORKDIR /home/johndoe
# Endless mode.
CMD ["tail", "-f", "/dev/null"]
