# Use an official Debian base image
FROM debian:bookworm

# Install necessary packages
RUN apt-get update -y && \
    apt-get install -y build-essential git cmake libcryptopp-dev python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /usr/src/app

# Copy benchmarking scripts and source code
COPY . /usr/src/app

# Build any necessary applications (if applicable)
# For now, we assume applications are built at runtime or separately

# Install Python packages for analysis (optional)
RUN pip3 install pandas matplotlib

# Set environment variables
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

# Default command
CMD ["bash"]

