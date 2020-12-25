FROM python:3.9
# Install security updates.
RUN pip install --upgrade pip
# Rootless mode.
RUN adduser --home /home/johndoe johndoe
USER johndoe
WORKDIR /home/johndoe
# Endless mode.
CMD ["tail", "-f", "/dev/null"]
