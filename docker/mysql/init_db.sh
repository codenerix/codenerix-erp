#!/bin/bash

mysql -u root --password="$MYSQL_ROOT_PASSWORD"  << EOF
USE ${MYSQL_DATABASE};
GRANT ALL PRIVILEGES ON  test_${MYSQL_DATABASE}.* TO '${MYSQL_USER}';
EOF
