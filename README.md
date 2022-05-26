# usql
Unofficial Docker image for [github.com/xo/usql](https://github.com/xo/usql)

Built image is available at dockerhub: [wookeshi/usql](https://hub.docker.com/r/wookeshi/usql)

## Usage

This image offers 2 ways to define database connection string.

### by arguments:

```docker run wookeshi/usql pg://user:password@address/db_name```

### by environment variables:

Second way is by setting environment variables, that can be used to define DSN.

This image supports all 3 patterns of DSNs used by usql:
```
driver+transport://user:password@host/dbname?options
driver:/path/to/file
/path/to/file
```

#### Environment Variables

| Environment Variable | Component     | Description                                                                                                |
|----------------------|---------------|------------------------------------------------------------------------------------------------------------|
| DRIVER               | driver        | driver scheme name                                                                                         |
| TRANSPORT            | transport     | `tcp`, `udp`, `unix` or driver name (for ODBC and ADODB)                                                   |
| USER                 | user          | database user                                                                                              |
| PASSWORD             | pass          | database user password                                                                                     |
| HOST                 | host          | database host                                                                                              |
| DB_NAME              | dbname        | database name                                                                                              |
| OPTIONS              | options       | additional database driver options as comma separated pairs of key value, i.e. `sslmode=disable,key=value` |
| DSN_PATH             | /path/to/file | path to file on disc                                                                                       |


