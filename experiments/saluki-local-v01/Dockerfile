FROM python:3.11-slim-bookworm AS build
RUN apt-get update && apt-get install -y --no-install-recommends git cmake g++ make ca-certificates && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/ggml-org/llama.cpp /llama && cd /llama && git checkout ead9f3205848f81ca079b4e760b76a01a6359f4b
RUN cmake -S /llama -B /llama/build -DGGML_NATIVE=OFF -DLLAMA_CURL=OFF -DLLAMA_BUILD_TESTS=OFF -DLLAMA_BUILD_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release && cmake --build /llama/build --target llama-server -j 4
FROM python:3.11-slim-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=build /llama/build/bin/ /opt/llama/
WORKDIR /app
COPY . /app
ENV LD_LIBRARY_PATH=/opt/llama PYTHONUNBUFFERED=1
CMD ["timeout","--signal=TERM","--kill-after=20s","3600s","python","cloud_run.py"]
