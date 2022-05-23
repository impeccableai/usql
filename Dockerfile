FROM golang:1.18 as build

RUN apt-get update && apt-get install -y build-essential

ENV CGO_ENABLED=0
# TODO: enable sqlite3
RUN go install -installsuffix cgo -tags most,no_sqlite3 github.com/xo/usql@v0.10.0

FROM python:alpine as deploy

COPY --from=build /go/bin/usql /usql
COPY entrypoint.py /entrypoint.py

ENV USQL_SHOW_HOST_INFORMATION=false

ENTRYPOINT ["/entrypoint.py"]
