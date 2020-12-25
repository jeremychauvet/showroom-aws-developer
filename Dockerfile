FROM python:3.9
# Install security updates.
RUN pip install --upgrade pip
# Rootless mode.
RUN adduser -D worker
USER worker
WORKDIR /home/worker
# Endless mode.
CMD ["tail", "-f", "/dev/null"]
